from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'posts/home.html', context)

def submit_post(request):
    form = PostForm(request.POST or None)
    context = {'form':form}
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect("posts:home") # should redirect to the homepage
        else:
            return render(request, "posts/partials/form.html", context) 
    
    return render(request, 'posts/post_form.html', context)