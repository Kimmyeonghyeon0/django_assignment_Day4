from importlib.resources import contents
from lib2to3.fixes.fix_input import context

# import Paginator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from blog.forms import BlogForm
from blog.models import Blog


#
def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")

    q = request.GET.get("q")
    if q:
        blogs = blogs.filter(Q(title__icontains=q) | Q(content__icontains=q))

        blogs = blogs.filter(content__icontains=q)

    paginator = Paginator(blogs, 10)
    page = request.GET.get("page")
    page_object = paginator.get_page(page)

    # Handle visit count with cookies
    visits = int(request.COOKIES.get("visits", 0)) + 1
    request.session["count"] = request.session.get("count", 0) + 1

    # Prepare context
    context = {
        # 'blogs': blogs,
        "object_list": page_object.object_list,
        "page_obj": page_object,
    }

    response = render(request, "blog_list.html", context)

    response.set_cookie("visits", visits)  # Set the updated visit count
    return response


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {"blog": blog}
    return render(request, "blog_detail.html", context)


@login_required()
def blog_create(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))

    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse("fb:detail", kwargs={"pk": blog.pk}))

    form = BlogForm()

    context = {"form": form}
    return render(request, "blog_form.html", context)


@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    # if request.user != blog.author:
    #     raise Http404

    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        blog = form.save()
        return redirect(reverse("fb:detail", kwargs={"pk": blog.pk}))

    context = {
        "blog": blog,
        "form": form,
    }
    return render(request, "blog_form.html", context)


@login_required()
@require_http_methods(["POST"])
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()

    return redirect(reverse("fb:blog_list"))
