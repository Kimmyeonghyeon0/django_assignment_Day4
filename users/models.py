from django.db import models


class Todo(models.Model):
    title = models.CharField('오늘 할일', max_length=100)
    description = models.TextField('본문', max_length=100)
    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    due_date = models.DateTimeField('기간')

    def __str__(self):
        return self.title
