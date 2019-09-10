from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
class puple(models.Model):

    fname = models.CharField(max_length = 150, db_index = True)
    lname = models.CharField(max_length=150, db_index = True)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    grade_index = models.CharField(max_length = 1)
    genderf = models.ManyToManyField('gender', related_name='gender_relname')

    def __str__(self):
        return '{}'.format(str(self.grade) + self.grade_index + self.fname)

class gender(models.Model):
    gend = models.CharField(max_length = 50)

    def __str__(self):
        return self.gend
