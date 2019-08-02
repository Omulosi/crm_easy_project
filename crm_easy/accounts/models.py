from django.db import models
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField


class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'accounts'
        ordering = ['created_on']

    def __str__(self):
        return "{}".format(self.name)

    @models.permalink
    def get_absolute_url(self):
        return 'accounts:account_detail', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'accounts:account_delete', [self.uuid]
