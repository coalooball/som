from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post, Review
from .forms import ReviewForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    searchTerm = request.GET.get('searchPost')
    if searchTerm:
        posts = Post.objects.filter(title__icontains=searchTerm)
    else:
        posts = Post.objects.all()
    return render(request, 'home.html',
        {'searchTerm':searchTerm, 'posts': posts})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

# def signup(request):
#     email = request.GET.get('email')
#     return render(request, 'signup.html', {'email':email})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    reviews = Review.objects.filter(post = post)
    return render(request, 'detail.html',
        {'post':post, 'reviews': reviews}
        )

@login_required
def createreview(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == 'GET':
        return render(request, 'createreview.html',
            {'form':ReviewForm(), 'post':post})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.post = post
            newReview.save()
            return redirect('detail', newReview.post.id)
        except ValueError:
            return render(request,
                'createreview.html',
                {'form':ReviewForm(),'error':'bad data passed in'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html',
            {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('detail', review.post.id)
        except ValueError:
            return render(request,
                'updatereview.html',
                {'review': review,'form':form,
                'error':'Bad data in form'}
                )

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.post.id)