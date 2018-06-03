from django.db import models

# Create your models here.
class LaTeXExpr(models.Model):
        expression = models.CharField('LaTeX Expression', max_length=256)
        create_date = models.DateTimeField('date created', auto_now_add=True)
        accesses = models.BigIntegerField('number of accesses', default=0)
        svg_data = models.TextField('SVG Data', default="")