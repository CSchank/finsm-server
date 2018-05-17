from django.db import models

# Create your models here.
class LaTeXExpr(models.Model):
        expression = models.CharField(max_length=256)
        create_date = models.DateTimeField('date created')
        accesses = models.BigIntegerField('number of accesses')
        svg_file = models.FileField(upload_to='latex_cache')
