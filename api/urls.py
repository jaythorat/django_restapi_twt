from django.urls import path,include
from . import views

urlpatterns = [
    path('blogposts/',views.BlogPostListCreate.as_view(),name="blogpost-view-create-view"),
    path('blogposts/<int:pk>/',views.BlogPostRetriveUpdateDestroy.as_view(),name="updateAndDelete"),
    path("customblogs/",views.BlogPostList.as_view(),name="customview")

]