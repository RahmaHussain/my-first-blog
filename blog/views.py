# from django.utils import timezone
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post
# from .forms import PostForm


# # Create your views here.
# def post_list(request):
#     posts = Post.objects.order_by("created_date")

#     return render(request, "blog/post_list.html", {"posts": posts})


# def post_view(request):
#     return render(request, "blog/post_view.html", {})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})


# def post_new(request):
#     form = PostForm(instance=post)

#     return render(request, "blog/post_edit.html", {"form": form})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect("post_detail", pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, "blog/post_edit.html", {"form": form})


# if request.method == "POST":
#     form = PostForm(request.POST)
# else:
#     form = PostForm()

#     if form.is_valid():
#     post = form.save(commit=False)
#     post.author = request.user
#     post.published_date = timezone.now()
#     post.save()
# # return redirect('post_detail', pk=post.pk)


# # def post_new(request):
# #     if request.method == "POST":
# #         form = PostForm(request.POST)
# #         if form.is_valid():
# #             post = form.save(commit=False)
# #             post.author = request.user
# #             post.published_date = timezone.now()
# #             post.save()
# #             return redirect('post_detail', pk=post.pk)
# #     else:
# #         form = PostForm()
# #     return render(request, 'blog/post_edit.html', {'form': form})
# # form = PostForm(request.POST, instance=post)


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})


from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.order_by("created_date")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_view(request):
    return render(request, "blog/post_view.html", {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})
