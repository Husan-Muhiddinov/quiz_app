from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=150)


    def __str__(self):
        return self.name
    


class Test(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    maximum_attemps=models.PositiveBigIntegerField()
    start_date=models.DateTimeField(default=timezone.now)
    end_date=models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=10)))
    pass_percentage=models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
    

class Question(models.Model):
    test=models.ForeignKey(Test,on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    a=models.CharField(max_length=150)
    b=models.CharField(max_length=150)
    c=models.CharField(max_length=150)
    d=models.CharField(max_length=150)
    true_answer=models.CharField(max_length=150,help_text="E.x: a")



    def __str__(self):
        return self.question
