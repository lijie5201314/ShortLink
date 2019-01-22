from django.db import models
import time
time.time()

class Links(models.Model):
    url = models.CharField(max_length=30)
    keyword = models.CharField(max_length=20)
    type = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'short_links'
        ordering = ['id']

    @classmethod
    def createLinks(cls, url, keyword, type=False, isDelete=False):
        link = cls(url=url, keyword=keyword, type=type, isDelete=isDelete)

        return link