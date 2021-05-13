"""
Definition of urls for Project.
"""

from django.urls import path, include
from django.contrib import admin
from app import views


urlpatterns = [
    path('tag/<slug:tag_slug>/', views.home, name='projects_by_tag'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('campaign/', include('campaign.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]