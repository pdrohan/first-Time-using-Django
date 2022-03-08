from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Blogg
from django.shortcuts import get_object_or_404

# Create your views here.
class BlogListView(ListView):
    # template_name = 'blog/blog_listview.html'
    template_name = 'blog/blog-home-1.html'
    queryset = Blogg.objects.all()

class BlogDetailView(DetailView):
    # template_name = 'blog/detailview.html'
    template_name = 'blog/blog-post.html'
    queryset = Blogg.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Blogg, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'title'
        return context
