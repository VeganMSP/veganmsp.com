from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import PostModelForm
from .models import Post, Category


class IndexView(ListView):
	queryset = Post.objects.filter(status=1).order_by('-date_created')
	template_name = 'blog/index.html'


def category_detail(request, category_id):
	if request.method == 'GET':
		current_category = Category.objects.get(pk=category_id)

		children = current_category.get_children()
		ancestors = current_category.get_ancestors()
		posts = current_category.posts.all()

		context = {
			'categories': children,
			'current_category': current_category,
			'ancestors': ancestors,
			'posts': posts,
		}
	print(context)
	return render(request, 'blog/category_detail.html', context)


class PostDetail(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'


@login_required
def post_create(request):
	if request.method == 'POST':
		form = PostModelForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog:post_detail', post.slug)
	form = PostModelForm()
	return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, slug):
	post = get_object_or_404(Post, slug=slug)
	form = PostModelForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		return redirect('blog:post_detail', slug)

	return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		post.delete()
		return redirect('blog:index')
	return render(request, 'blog/post_delete.html', {'post': post})
