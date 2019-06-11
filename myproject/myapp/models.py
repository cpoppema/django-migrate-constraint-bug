from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.CharField(unique=True, max_length=15)


class Call(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               to_field='code',
                               db_column='clientcode')
