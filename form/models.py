from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    # name = models.CharField(max_length=120)
    #email = models.EmailField()
    #product = models.ForeignKey(Product)
    feedbacks = models.TextField()
    #happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.feedbacks