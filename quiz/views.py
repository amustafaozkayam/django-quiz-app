from django.shortcuts import render
from .models import Answers, Category, Questions, Quiz
from .serializers import AnswersSerializer, QuestionsSerializer, QuizSerializer, CategorySerializer

from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated

from .pagination import *
from .permission import *

class QuizList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizDetail(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category = self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name=category)

class QuestionRead(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["difficulty"]
    pagination_class = SmallPageNumberPagination
    permission_classes = (IsStuffOrReadOnly,)

    def get_queryset(self):
        quiz = self.kwargs['quiz'].capitalize()
        return Questions.objects.filter(quiz__title=quiz)
