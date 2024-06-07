from django.shortcuts import render, redirect
from posts import forms
from posts.models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url='/author/login/')
def addPost(request):
    if request.method == "POST":
        form = forms.addPost(request.POST)
        if form.is_valid():
            # form.cleaned_data['author'] = request.user
            form.instance.author = request.user
            form.save()
            return redirect('addPost')
    else:
        form=forms.addPost()
    return render(request, 'addPost.html', {'form': form })
        
@login_required(login_url='/author/login/')
def editPost(request, id):
    post = Post.objects.get(pk=id)
    form = forms.addPost(instance=post)
    if request.method == "POST":
        form = forms.addPost(request.POST, instance=post)
        if form.is_valid():
            # form.instance.author = request.user
            form.save()
            return redirect('home')
    return render(request, 'addPost.html', {'form': form })    

@login_required(login_url='/author/login/')
def deletePost(request , id):
     post = Post.objects.get(pk=id)
     post.delete()
     return redirect('home')