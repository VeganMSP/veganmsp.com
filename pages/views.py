from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from blog.models import Post
from .models import Page


class PageView(TemplateView):
    template_name = 'pages/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = context['view'].request.path.strip('/')
        if path == '':
            # index is special
            path = 'index'
            context['recent_posts_list'] = Post.objects.order_by(
                '-date_created'
            )[:5]
            self.template_name = 'pages/index.html'
        context['page'] = get_object_or_404(Page, path=path)
        return context
