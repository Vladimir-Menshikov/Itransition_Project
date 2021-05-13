from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProjectImageAddForm, RewardForm, CommentForm, NewsForm
from .models import Project, ProjectImage, Reward, Comment, News
from cloudinary.forms import cl_init_js_callbacks     
import decimal

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            form.save_m2m()
            return redirect('edit_project', slug = new_project.slug, id = new_project.id)
    else:
        form = ProjectForm()
    return render(request,
                  'campaign/add_project.html',
                  {'form': form,
                   'title': 'New Project'})

@login_required
def edit_project(request, slug, id):
    project = get_object_or_404(Project, slug = slug, id = id)
    if request.user.id == project.user.id:
        if request.method == 'POST':
            form = ProjectForm(instance=project,
                                     data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(project)
        else:
            form = ProjectForm(instance=project)
        return render(request,
                      'campaign/edit_project.html',
                      {'form': form,
                       'title': 'Edit Project',
                       'project': project})
    else:
        return redirect('home')

def project(request, slug, id):
    project = get_object_or_404(Project, slug = slug, id = id)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.project = project
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'campaign/project.html',
                  {'project': project,
                  'title': project.name,
                   'new_comment': new_comment,
                   'comment_form': comment_form,})

@login_required
def add_project_image(request, slug, id):
    project = get_object_or_404(Project,slug = slug, id = id)
    if request.user.id == project.user.id:
        if request.method == 'POST':
            form = ProjectImageAddForm(request.POST, request.FILES)
            if form.is_valid():
                new_project_image = form.save(commit=False)
                new_project_image.project = project
                new_project_image.save()
                form.save()
                return redirect('edit_project', slug = project.slug, id = project.id)
        else:
            form = ProjectImageAddForm()
        return render(request, 'campaign/add_project_image.html',
                      {'form': form,
                       'title': 'Add Image'})
    else:
        return redirect('home')

@login_required
def delete_project_image(request):
    id = request.POST.get('delete_image')
    ProjectImage.objects.get(id=id).delete()
    project = Project.objects.get(id=request.POST.get('project'))
    return redirect('edit_project', slug = project.slug, id = project.id)

@login_required
def add_reward(request, slug, id):
    project = get_object_or_404(Project,slug = slug, id = id)
    if request.user.id == project.user.id:
        if request.method == 'POST':
            form = RewardForm(request.POST)
            if form.is_valid():
                new_reward = form.save(commit=False)
                new_reward.project = project
                new_reward.save()
                return redirect('edit_project', slug = project.slug, id = project.id)
        else:
            form = RewardForm()
        return render(request,
                      'campaign/add_reward.html',
                      {'form': form,
                       'title': 'Add Reward'})
    else:
        return redirect('home')

@login_required
def edit_reward(request, id):
    reward = get_object_or_404(Reward, id = id)
    if request.user.id == reward.project.user.id:
        if request.method == 'POST':
            form = RewardForm(instance=reward,
                                     data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('edit_project', slug = reward.project.slug, id = reward.project.id)
        else:
            form = RewardForm(instance=reward)
        return render(request,
                      'campaign/edit_reward.html',
                      {'form': form,
                       'title': 'Edit Reward',
                       'reward': reward})
    else:
        return redirect('home')

@login_required
def delete_reward(request):
    id = request.POST.get('delete_reward')
    Reward.objects.get(id=id).delete()
    project = Project.objects.get(id=request.POST.get('project'))
    return redirect('edit_project', slug = project.slug, id = project.id)

@login_required
def rewards(request, slug, id):
    project = get_object_or_404(Project, slug=slug, id=id)
    if request.method == 'POST':
        if 'reward' in request.POST:
            reward_id=request.POST.get('reward')
            reward = Reward.objects.get(id=reward_id)
            reward.users.add(request.user)
            sum = reward.sum  
        elif 'sum' in request.POST:
            sum = decimal.Decimal(request.POST.get('sum'))
        project.backers += 1
        project.collected_sum += sum
        project.save()
        return render(request,
                      'campaign/pledged.html',
                      {'title': 'pledged',
                       'sum': sum})
    return render(request,
                      'campaign/rewards.html',
                      {'title': 'Rewards',
                       'project': project})


@login_required
def add_news(request, slug, id):
    project = get_object_or_404(Project,slug = slug, id = id)
    if request.user.id == project.user.id:
        if request.method == 'POST':
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.project = project
                news.save()
                form.save()
                return redirect('news', id = news.id)
        else:
            form = NewsForm()
        return render(request, 'campaign/add_news.html',
                      {'form': form,
                       'title': 'Add News'})
    else:
        return redirect('home')

@login_required
def edit_news(request, id):
    news = get_object_or_404(News, id = id)
    if request.user.id == news.project.user.id:
        if request.method == 'POST':
            form = NewsForm(instance=news,
                                     data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect(news)
        else:
            form = NewsForm(instance=news)
        return render(request,
                      'campaign/edit_news.html',
                      {'form': form,
                       'title': 'Edit News',
                       'news': news})
    else:
        return redirect('home')

def news(request, id):
    news = get_object_or_404(News, id = id)
    if request.method == 'POST' and 'delete_news' in request.POST:
        project = news.project
        News.objects.get(id = id).delete()
        return redirect(project)
    return render(request,'campaign/news.html',
                  {'news': news,
                  'title': news.title,
                   })