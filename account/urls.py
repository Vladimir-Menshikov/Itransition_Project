from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views, forms


urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='account/login.html',
             authentication_form=forms.LoginForm,
             extra_context=
             {
                 'title': 'Log in',
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('my_rewards/', views.my_rewards, name='my_rewards'),
    path('my_projects/', views.my_projects, name='my_projects'),
    path('my_profile/', views.my_profile, name='my_profile'),
]

    
