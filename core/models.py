from django.db import models

# Course Model
class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Student Model
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='students')
    
    def __str__(self):
        return self.name    
