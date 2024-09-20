from django.db import models


class Question(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('elementary', 'Elementary'),
        ('intermediate', 'Intermediate'),
        ('pre-intermediate', 'Pre-Intermediate'),
        ('upper-intermediate', 'Upper-Intermediate'),
    ]
    text = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    correct_answer = models.ForeignKey('Answer', related_name='correct_for', on_delete=models.CASCADE, null=True,
                                       blank=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
