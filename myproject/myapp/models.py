from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.PositiveIntegerField(unique=True)


class Call(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               to_field='code',
                               related_name='+',
                               db_column='clientcode')
