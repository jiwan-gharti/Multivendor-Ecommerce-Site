from django.db import models
from django.db.models.query import QuerySet

class OrderItemManager(models.Manager):
    def get_total(self,user):
        queryset = self.filter(
            user=user, ordered = False
        )
        return queryset