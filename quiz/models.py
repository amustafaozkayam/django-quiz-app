
from django.db import models

class Category(models.Model):

    CATEGORY_NAME = [
        ('Frontend','Frontend'),
        ('Backend', 'Backend'),
        ('Aws', 'Aws-Devops'),
        ('Datascience', 'Datascience'),
        ('Mobile','Mobile'),
    ]

    name = models.CharField(max_length=20, choices=CATEGORY_NAME, default='Backend')
    createdDate = models.DateField()
    
    def __str__(self):
        return self.name

class Quiz(models.Model):
    category = models.ForeignKey(Category,
    on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add = True)
    createdDate = models.DateField()
    

    def __str__(self):
        return f'{self.category} - {self.title}'

class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.TextField(max_length=100)
    DIFFICULTY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('E', 'Expert'),
    ]
       
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='low')
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz} - {self.title}'

    class Meta:
        verbose_name_plural = 'Questions'

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')

    answer_text = models.TextField(max_length=200)
    is_right = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Answers'