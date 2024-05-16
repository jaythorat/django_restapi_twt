from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


    # Overwriting generic views
    def delete(self,request,*args,**kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


# Creating Custom views
class BlogPostList(APIView):
    def get(self,request,format=None):
        title = request.query_params.get("title","")

        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)