from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(blank=True, default=False)

class Task_Form(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
