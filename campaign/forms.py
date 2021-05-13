from django import forms
from .models import Project, ProjectImage, Reward, Comment, News
from taggit.forms import TagWidget

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category', 'name', 'tags', 'description',
             'video', 'goal', 'expiration_date')
        widgets = {
            'category': forms.Select(attrs=
                                       {'class': 'form-control',
                                        'placeholder':'Category',
                                        }),
            'name': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder':'Name',
                                        }),
            'tags': TagWidget(attrs=
                              {'class': 'form-control',
                               'placeholder':'Tags',
                               }),
            'description': forms.Textarea(attrs=
                                          {'class': 'form-control',
                                           'placeholder':'Markdown Description',
                                              }),
            'video': forms.URLInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder':'YT video URL',
                                        }),
            'goal': forms.NumberInput(attrs=
                                      {'class': 'form-control',
                                       'placeholder':'goal',
                                        }),
            'expiration_date': forms.DateInput(attrs=
                                      {'class': 'form-control',
                                       'type': 'date',
                                        }),
            }

class ProjectImageAddForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ('image',)

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ('name', 'description', 'sum')
        widgets = {
            'name': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder':'Name',
                                        }),
            'description': forms.Textarea(attrs=
                                          {'class': 'form-control',
                                           'placeholder':'Description',
                                              }),
            'sum': forms.NumberInput(attrs=
                                      {'class': 'form-control',
                                       'placeholder':'goal',
                                        }),
            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs=
                                   {'class': 'form-control',
                                    'placeholder':'Write a comment',
                                    }),
            }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text', 'image')
        widgets = {
            'title': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder':'Title',
                                        }),
            'text': forms.Textarea(attrs=
                                          {'class': 'form-control',
                                           'placeholder':'Markdown Text',
                                              }),
            }