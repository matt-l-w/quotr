from django.contrib import admin
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('quotes:detail-book', args=(self.pk,))

class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    page = models.PositiveIntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('quotes:detail-quote', args=(self.pk,))

admin.site.register(Book)
admin.site.register(Quote)
