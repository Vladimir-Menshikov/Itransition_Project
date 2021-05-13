from django.urls import path, include
from . import views

urlpatterns = [
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<slug:slug>/<int:id>/', views.edit_project, name='edit_project'),
    path('add_project_image/<slug:slug>/<int:id>/', views.add_project_image, name='add_project_image'),
    path('delete_project_image/', views.delete_project_image, name='delete_project_image'),
    path('edit_reward/<int:id>/', views.edit_reward, name='edit_reward'),
    path('add_reward/<slug:slug>/<int:id>/', views.add_reward, name='add_reward'),
    path('delete_reward/', views.delete_reward, name='delete_reward'),
    path('rewards/<slug:slug>/<int:id>/', views.rewards, name='rewards'),
    path('add_news/<slug:slug>/<int:id>/', views.add_news, name='add_news'),
    path('edit_news/<int:id>/', views.edit_news, name='edit_news'),
    path('news/<int:id>/', views.news, name='news'),
    path('<slug:slug>/<int:id>/', views.project, name='project')
]