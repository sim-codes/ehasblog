from django.urls import path
from .feeds import LastestPostsFeed
from .views import (
    BlogCreateView,
    PostUpdateView,
    PostDeleteView,
    post_list,
    post_detail,
    user_post_list,
    post_comment,
)

urlpatterns = [
    path("", post_list, name="post_list"),
    path("stories", user_post_list, name="user_post_list"),
    path("new", BlogCreateView.as_view(), name="post_new"),
    path("<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"
    ),
    path(
        "<int:post_id>/comment/",
        post_comment,
        name="post_comment",
    ),
    path(
        "tag/<slug:tag_slug>/",
        post_list,
        name="post_list_by_tag",
    ),
    path("feed/", LastestPostsFeed(), name="post_feed"),
]

handler404 = "blog.views.page_not_found_view"
