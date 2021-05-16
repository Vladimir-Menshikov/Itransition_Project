from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from campaign.models import Project, Category
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from datetime import date
from .forms import OrderByForm

def home(request, category_slug=None, tag_slug=None):
    projects = Project.objects.filter(expiration_date__gt=date.today())
    categories = Category.objects.all()
    tags = Tag.objects.all()

    category = None
    tag = None
    query = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = projects.filter(tags__in=[tag])
    
    if 'query' in request.GET:
        query = request.GET.get('query')
        search_vector = SearchVector('name', weight='A') + \
            SearchVector('description_rendered', weight='B')
        search_query = SearchQuery(query)
        projects = projects.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

    order_by_form = OrderByForm(request.GET)
    if order_by_form.is_valid():
        projects = projects.order_by(order_by_form.cleaned_data['order_by'])

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'projects': projects,
            'categories': categories,
            'tags': tags,
            'category': category,
            'order_by_form': order_by_form
        }
    )