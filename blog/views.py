from dal.autocomplete import Select2QuerySetView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import PostModelForm
from .models import Post, Category


class IndexView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'blog/index.html'


def category_detail(request, slug):
    if request.method == 'GET':
        current_category = Category.objects.get(slug=slug)

        posts = current_category.posts.all()

        context = {

            'current_category': current_category,
            'posts': posts,
        }
    return render(request, 'blog/category_detail.html', context)


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostDetailByDate(DetailView):
    template_name = 'blog/post_detail.html'

    def get(self, request, year, month, day, slug, *args, **kwargs):
        post = Post.objects.get(
            slug=slug,
            date_created__year=year,
            date_created__month=month,
            date_created__day=day
        )
        return render(
            request,
            self.template_name,
            {
                'post': post
            })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(
                'blog:post_detail_by_date',
                post.date_created.year,
                post.date_created.strftime("%m"),
                post.date_created.strftime("%d"),
                post.slug
            )
    form = PostModelForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect(
            'blog:post_detail_by_date',
            post.date_created.year,
            post.date_created.strftime("%m"),
            post.date_created.strftime("%d"),
            post.slug
        )

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/post_delete.html', {'post': post})


class CategoryAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Filter out results depending on login state
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
