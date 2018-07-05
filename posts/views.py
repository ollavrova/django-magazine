from django.views.generic import TemplateView
from posts.models import Post


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(approved=True).order_by('-created')
        return context


index = Index.as_view()
