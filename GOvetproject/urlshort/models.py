from django.db import models


class URLData(models.Model):  # Every write to the database, write as a text field
    URLID = models.CharField(max_length=1000)  # Max length of original URL
    ShortURL = models.CharField(max_length=12)  # Max length of short URL

    def __str__(self):
        template = '{0.URLID}, {0.ShortURL}'  # Return both original URL ID and short URL
        return template.format(self)
