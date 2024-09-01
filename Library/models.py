from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    available = models.BooleanField()

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['author']
        unique_together = (('isbn'),)
