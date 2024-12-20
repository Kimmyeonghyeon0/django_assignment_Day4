"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import include, path
# from users import views as users_views
# from users.views import todo_list, todo_info

# from users import todo_list, todo_info, sign_up
# from blog import views

# from member import views as member_views
# urlpatterns = [
#     # path('todo/', todo_list, name='todo_list'),
#     # path('todo/<int:todo_id>/', todo_info, name='todo_info'),
#     # path('admin/', admin.site.urls),
#     # path('accounts/', include('django.contrib.auth.urls')),
#     # path('accounts/login/', users_views.login, name='login'),
#     # path('accounts/signup/', users_views.sign_up, name='signup')

from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import include, path
from django.views import View
from django.views.generic import RedirectView, TemplateView

from blog import cb_views, views
from member import views as member_views

# class AboutView(TemplateView):
#     template_name = 'about.html'
#
# class TestView(View):
#     def get(self, request):
#         return render(request, 'test_get.html')
#
#     def post(self, request):
#         return render(request, 'test_post.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    # FBV blog
    path("", include("blog.urls")),
    path("fb/", include("blog.fbv_urls")),
    path("cb/", cb_views.BlogListView.as_view(), name="cb_blog_list"),
    path("cb/<int:pk>/", cb_views.BlogDetailView.as_view(), name="cb_blog_detail"),
    path("cb/create/", cb_views.BlogCreateView.as_view(), name="cb_blog_create"),
    path(
        "cb/<int:pk>/update/", cb_views.BlogUpdateView.as_view(), name="cb_blog_update"
    ),
    path("<int:pk>/delete/", cb_views.BlogDeleteView.as_view(), name="blog_delete"),
    # auth
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", member_views.sign_up, name="signup"),
    path("login/", member_views.login, name="login"),  # 추가
    # path('about', AboutView.as_view(), name='about'),
    # path('redirect/', RedirectView.as_view(pattern_name='about'), name='redirect'),
    # # path('redirect2/', lambda req: redirect('about')),
    # path('test/', TestView.as_view(), name='test'),
]
