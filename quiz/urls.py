from django.urls import include, path
from .views import QuizList, QuizDetail, QuestionRead
# from rest_framework.authtoken import views


urlpatterns = [
   path('', QuizList.as_view(), name='quiz-list'),
   path('<category>/', QuizDetail.as_view(), name='quiz-read'),
    path('<category>/<quiz>/', QuestionRead.as_view(), name='quiz-read'),
    
]
