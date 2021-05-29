from django.views.generic import DetailView, ListView

from .models import Post


class IndexView(ListView):
	queryset = Post.objects.filter(status=1).order_by('-date_created')
	template_name = 'blog/index.html'


class PostDetail(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
