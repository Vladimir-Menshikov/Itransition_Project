from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('shop:product_list_by_category',
    #                   args=[self.slug])

class Project(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='projects',
                                 on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                                 related_name='projects',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    tags = TaggableManager()
    description = MarkdownField(rendered_field='description_rendered', validator=VALIDATOR_STANDARD, blank=True)
    description_rendered = RenderedMarkdownField()
    video = models.URLField(blank=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    collected_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expiration_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    backers = models.PositiveIntegerField(default=0)
    rate = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0
        )
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project',
                       args=[self.slug, self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.video = self.video.replace('youtu.be', 'www.youtube.com/embed').replace('watch?v=', 'embed/')
        super(Project, self).save(*args, **kwargs)

    def days_left(self):
        return (self.expiration_date - date.today()).days

class ProjectImage(models.Model):
    project = models.ForeignKey(Project,
                                related_name='images',
                                on_delete=models.CASCADE)
    image = CloudinaryField('image')

class Reward(models.Model):
    project = models.ForeignKey(Project,
                                related_name='rewards',
                                on_delete=models.CASCADE)
    users = models.ManyToManyField(User,
                                   related_name='rewards',
                                   blank=True)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    project = models.ForeignKey(Project,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                                 related_name='comments',
                                 on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class News(models.Model):
    project = models.ForeignKey(Project,
                             on_delete=models.CASCADE,
                             related_name='news')
    title = models.CharField(max_length=200, db_index=True)
    text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD, blank=True)
    text_rendered = RenderedMarkdownField()
    image = CloudinaryField('image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def get_absolute_url(self):
        return reverse('news',
                       args=[self.id])