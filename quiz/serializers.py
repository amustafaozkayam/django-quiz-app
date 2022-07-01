from rest_framework import serializers
from .models import Category, Answers, Questions, Quiz

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

class AnswersSerializer(serializers.ModelSerializer):

    question_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Answers
        fields = ('answer_text', 'is_right','question_id')

class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, required=False)
    quiz_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Questions
        fields = ('quiz_id','title', 'answers', 'difficulty')

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Questions.objects.create(**validated_data)
        for answer in answers_data:
            answer["question_id"] = question.id
            question.answers.add(Answers.objects.create(**answer))
        question.save()
        return question


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, write_only=True)
    questions_count = serializers.SerializerMethodField(read_only=True)
    publish_time = serializers.SerializerMethodField()


    class Meta:
        model = Quiz
        fields = ('title','questions', 'questions_count','publish_time',)
    
    def get_questions_count(self, object):
        return object.questions.count()

    def get_publish_time(self, obj):
        now= datetime.now()
        pub_date = obj.createdDate
        time_delta = timesince(pub_date, now)
        return f'{time_delta} ago'


class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField(read_only=True)
    publish_time = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count', 'quizzes','publish_time' )

    def get_quiz_count(self, object):
        return object.quizzes.count()

    def get_publish_time(self, obj):
        now= datetime.now()
        pub_date = obj.createdDate
        time_delta = timesince(pub_date, now)
        return f'{time_delta} ago'
       

    

