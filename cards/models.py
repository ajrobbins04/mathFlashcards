from django.db import models

"""
Stores all the mathematical expressions 
that will be used to create flashcards. 
"""

# smallest row corresponds to 1 + 1 = 2
# largest row corresponds to 25 + 25 = 50
class Add(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

# smallest row corresponds to 1 - 1 = 0
# largest row corresponds to 25 - 25 = 0
class Subtract(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

# smallest row corresponds to 1 * 1 = 1
# largest row corresponds to 12 * 12 = 144
class Multiply(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)

# smallest row corresponds to 1 / 1 = 0
# largest row corresponds to 144 / 12 = 12
class Divide(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    result = models.IntegerField()
    operator = models.CharField(max_length=1)