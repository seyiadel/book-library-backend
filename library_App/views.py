from django.shortcuts import render
from rest_framework.views import APIView, Response
from library_App.serializers import UserSerializer, LogInUserSerializer, BookSerializer

from rest_framework import status
from knox.views import LoginView
from django.contrib.auth import login
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from rest_framework.authentication import TokenAuthentication
from library_App.models import Book
from knox.auth import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class SignUpUser(APIView):

    @swagger_auto_schema(request_body=UserSerializer())
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LogInUser(LoginView):

    permission_classes=(AllowAny,)

    @swagger_auto_schema(request_body=LogInUserSerializer())
    def post(self, request):
        serializer = LogInUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)


class AllBooks(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(BookSerializer(many=True))
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreateBook(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=BookSerializer())
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['uploaded_by'] = self.request.user
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleBook(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(BookSerializer())
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BookSerializer())
    def put(self, request, pk):
        book = Book.objects.filter(id=pk)
        serializer = BookSerializer(book, instance=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       