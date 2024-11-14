from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Blog
from django.db.models import Q


class BlogListView(ListView):
    # model = Blog
    queryset = Blog.objects.all().order_by('-created_at')
    template_name = 'blog_list.html'
    paginator = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )

            return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     return queryset.filter(id__lte=50)
    #
    # def get_object(self, queryset=None):
    #     object = super().get_object()
    #     object = self.model.objects.get(pk=self.kwargs.get('pk'))
    #     return object
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['test'] = 'CBV'
    #     return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ['title', 'content']
    # success_url = reverse_lazy('cb_blog_detail', kwargs={'pk': object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse_lazy('cb_blog_detail', kwargs={'pk': self.object.pk})


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ['title', 'content']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.author != self.request.user:
    #         raise Http404
    #     return self.object

    # def get_success_url(self):
    #     return reverse_lazy('cb_blog_detail', kwargs={'pk': self.object.pk})
