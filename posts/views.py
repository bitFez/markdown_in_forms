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

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            list.author = request.user
            list.save()
            
            return redirect("posts:home") # should redirect to the homepage
        else:
            return render(request, "posts/partials/form.html", context={"form":form}) #?? should be list form?? may cause div repeat
    
    context = {'form':form}
    return render(request, 'booqmarqs/create_link.html', context)