from django.db import models


# Create your models here.
class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    addr = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "student"
