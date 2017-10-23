from __future__ import unicode_literals

from django.db import models

class Activity(models.Model):
    # class Meta:
    #     verbose_name_plural = 'activities'
    name = models.CharField(max_length=80, help_text='activity name')
    
    def __unicode__(self):
        return self.name