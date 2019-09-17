from django.db import models

# Something that will create a database table
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

