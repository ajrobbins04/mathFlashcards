from django.db import models

"""
Stores all mathematical computations that
will be used to create flashcards. The
lhs and rhs values will span from 1 - 12.
"""
class Add(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

class Subtract(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

class Multiply(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

class Divide(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)