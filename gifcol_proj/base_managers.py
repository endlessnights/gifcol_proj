from django.db import models


class PublishedManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(published=True)
