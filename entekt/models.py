from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


class Course(models.Model):
    objects = None
    owner = models.ForeignKey(User,
                            related_name='courses_created',
                            on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                            related_name='courses',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course,
                            related_name='modules',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
         return self.title

class Quest(models.Model):
    module = models.ForeignKey('Module', related_name='quests', on_delete=models.CASCADE, null=True)
    qno = models.IntegerField(null=True, blank=True)
    question = models.CharField(max_length=100, null=True)
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question}'

class Option(models.Model):
    quest = models.ForeignKey('Quest', related_name='options', on_delete=models.CASCADE)
    option_letter = models.CharField(max_length=1, blank=True, null=True)  # Field for the option letter
    option = models.CharField(max_length=100, blank=True, null=True)  # Field for the option text

    def __str__(self):
        return f'{self.option_letter}: {self.option}'

class CorrectAnswer(models.Model):
    quest = models.ForeignKey(Quest, related_name='correct_answers', on_delete=models.CASCADE)
    correct_option = models.ForeignKey(Option, related_name='correct_for_question', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Correct answer for Question No.{self.quest.qno}'


