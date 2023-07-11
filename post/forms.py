from django.forms import ModelForm, Textarea
from .models import Review, Post

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
                            {'class': 'form-control'})

    class Meta:
        model = Review
        fields = ['text']    
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']