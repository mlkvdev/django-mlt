import logging

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Blog, Comment
from app.serializers import BlogSerializer, CommentSerializer

logger = logging.getLogger(__name__)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super(CommentViewSet, self).get_queryset().filter(author=self.request.user)


class TestAPIView(APIView):
    @staticmethod
    def get(request):
        return Response(data={"message": "Hello World!"})


class ErrorAPIView(APIView):
    @staticmethod
    def get(request):
        logger.error("Log1 on Webapp!")
        return Response(data={"hello": "world"})


class RaiseErrorAPIView(APIView):
    @staticmethod
    def get(request):
        logger.error("error raised")
        raise Exception("error raised")
