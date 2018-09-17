from django.db import models
from datetime import datetime


class Priority(models.Model):
    #priority_id = models.IntegerField(default=0, null=True, blank=True)
    number_priority = models.IntegerField(default=0, null=True, blank=True)
    description_priority = models.CharField(max_length=200, null=True)

    options = {1 : 'Urgent', 2 : 'High', 3 : 'Normal' }

    def __str__(self):
        return self.number_priority



class State(models.Model):
    number_state = models.IntegerField(default=0, null=True)
    description_state = models.CharField(max_length=200, null=True)

    options = {1 : 'Pending', 2 : 'Done' }

    def __str__(self):
        return self.number_state


class Personal_List(models.Model):
    title = models.CharField(default='',max_length=200)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    description = models.TextField(null=True) #models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    priority = models.ForeignKey(Priority)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.title


#create a list model
#title
#pub_date
#body
#image

#add the list app to the setting

#create a migration

#Migrate

#Add to the admin