from django.db import models
todo_status = [
    ('yes', 'Yes'),
    ('no', 'No'),
]
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.TextField(choices=todo_status)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title