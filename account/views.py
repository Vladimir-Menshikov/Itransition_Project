from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserEditForm
from campaign.models import Project

@login_required
def my_rewards(request):
    return render(request,
                  'account/my_rewards.html',
                  {'title': 'My Rewards'})

@login_required
def my_projects(request):
    if request.method == 'POST' and 'delete_project' in request.POST:
        Project.objects.get(id = request.POST.get('delete_project')).delete()
    return render(request,
                  'account/my_projects.html',
                  {'title': 'My Projects'})

@login_required
def my_profile(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)
    return render(request,
                  'account/my_profile.html',
                  {'form': form,
                   'title': "My account"})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user,
                           'title': "Registered"},
                          )
    else:
        form = RegistrationForm()
        return render(request,
                      'account/register.html',
                      {'form': form,
                        'title': 'Registration'},
                     )