from django.shortcuts import render, redirect,get_object_or_404
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)


@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form =   UserUpdateForm(data=request.POST,instance=request.user)
        """  p_form =   ProfileUpdateForm(data=request.POST,files=request.FILES,instance=request.user.profile) """
        if u_form.is_valid() : #and p_form.is_valid():
            u_form.save()
            #p_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return 
            redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        """        p_form =         Prof ileUpdateForm(instance=request.user.profile) """

    context = {
        'u_form':u_form,
        #'p_form':p_form,
    }
    return render(request, 'blog/profile.html', context)
