from django.contrib.auth.models import User
from django.db import models

class RegularActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exp = models.IntegerField(default=0)
    parts_quantity = models.IntegerField()

class DailyActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exp = models.IntegerField(default=0)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    regular_activity = models.ForeignKey(RegularActivity, on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='daily')
    daily_activity = models.ForeignKey(DailyActivity, on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='regular')

    def __str__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=1)
    skills = models.ForeignKey(Skill, on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='skills')

    def __str__(self):
        return self.name
