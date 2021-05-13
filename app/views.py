from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from campaign.models import Project
from taggit.models import Tag

def home(request, tag_slug=None):
    projects = Project.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = projects.filter(tags__in=[tag])
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'projects': projects,
            'tag': tag,
        }
    )