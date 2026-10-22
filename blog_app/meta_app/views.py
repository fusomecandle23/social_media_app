from django.shortcuts import render         
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import*
from .serializers import Userserializers, postserializers, commentserializers, likeserializers
from .permissions import IsOwner

class AddUser(CreateAPIView):
    serializer_class = Userserializers


class UserPostView(CreateAPIView, RetrieveAPIView):
    serializer_class = postserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostList(ListAPIView):
    serializer_class = postserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()


class UserPostRetreiveView(UpdateAPIView, DestroyAPIView):
    serializer_class = postserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()


class CommentView(CreateAPIView, ListAPIView):
    serializer_class = commentserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeView(CreateAPIView):
    serializer_class = likeserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner_obj=self.request.user)