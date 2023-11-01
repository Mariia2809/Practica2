from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# Дополнительные поля для пользовательского профиля

class Category(models.Model):
    name = models.CharField(max_length=100)
# Другие поля для категории

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
category = models.ForeignKey(Category, on_delete=models.CASCADE)
status = models.CharField(max_length=50)
# Другие поля для заявки