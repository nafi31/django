from django.db import models

class Title(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text