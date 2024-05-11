from django.shortcuts import render
from .models import Category, Thread , Post
from django.shortcuts import render, redirect
from .forms import ThreadForm , PostForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def create_thread(request):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        return redirect('/signin')
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.creator =user_conn
            thread.save()
            return redirect('forum_home')  # Redirect to the forum home page after thread creation
    else:
        form = ThreadForm()

    return render(request, 'forum/create_thread.html', {'form': form , 'user_conn': user_conn})

def forum_home(request):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None    
    categories = Category.objects.all()
    threads = Thread.objects.all()

    context = {
        'categories': categories,
        'threads': threads,
        'user_conn': user_conn
    }
    return render(request, 'forum/home.html', context)

def create_post(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.creator = request.user
            post.save()
            return redirect('view_thread', thread_id=thread_id)  # Redirect to the thread view after post creation
    else:
        form = PostForm()

    return render(request, 'forum/create_post.html', {'form': form, 'thread': thread})

def view_thread(request, thread_id):
    # Retrieve the thread object or return a 404 error if not found
    thread = get_object_or_404(Thread, id=thread_id)

    # Retrieve all posts associated with the thread
    posts = Post.objects.filter(thread=thread)

    # Check if the user is authenticated
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    # Handle post submission
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.creator = user_conn
            post.save()
            return redirect('view_thread', thread_id=thread_id)  # Redirect to the same thread page after posting

    else:
        form = PostForm()

    return render(request, 'forum/view_thread.html', {'thread': thread, 'posts': posts, 'form': form, 'user_conn': user_conn})


def threadPerCat(request,cat):
    user_pk = request.session.get('userconn')
    if user_pk:
        try:
            user_conn = Profile.objects.get(pk=user_pk)
        except Profile.DoesNotExist:
            user_conn = None
    else:
        user_conn = None
    category = get_object_or_404(Category, name=cat)
    
    # Filter threads based on the category
    threads = Thread.objects.filter(category=category)    
    return render(request, 'forum/threadPerCat.html', {'threads': threads,  'user_conn': user_conn})



