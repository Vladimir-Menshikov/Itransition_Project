from django.contrib import admin
from .models import Category, Project, ProjectImage, Reward, Comment, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'user', 'goal', 'collected_sum',
                  'expiration_date', 'backers', 'rate', 'created', 'updated']
    list_filter = ['name', 'category', 'user', 'goal', 'collected_sum',
                  'expiration_date', 'backers', 'rate', 'created', 'updated']
    fields = ('user', 'category', 'name', 'tags', 'description',
             'video', 'goal', 'expiration_date')

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'sum']
    list_filter = ['name', 'project', 'sum']
    fields = ('name', 'description', 'sum')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'created',)
    list_filter = ('user', 'project', 'created',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created',)
    list_filter = ('title', 'project', 'created',)

admin.site.register(ProjectImage)