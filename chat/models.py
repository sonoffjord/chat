from django.db import models


class Massage(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    
    def __str__(self):
        return str(self.date)