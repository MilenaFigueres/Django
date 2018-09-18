from django.db import models
from datetime import datetime


class Priority(models.Model):
    PRIORITY = (
        ('Urgent' , 'Urgent'), 
        ('Hight' , 'Hight' ),
        ('Normal' , 'Normal' ),
    )
    number_priority = models.CharField(max_length=3, choices=PRIORITY, default='3')
    description_priority = models.CharField(max_length=200, null=True)


class State(models.Model):
    STATE = (
        ('Pending' , 'Pending'), 
        ('Done' , 'Done' ),
    )
    number_state = models.CharField(max_length=3, choices=STATE, default='1')
    description_state = models.CharField(max_length=200, null=True)

    

class Personal_List(models.Model):
    title = models.CharField(default='',max_length=200)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    description = models.TextField(null=True) #models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    priority = models.ForeignKey(Priority)
    state = models.ForeignKey(State)

#create a list model
#title
#pub_date
#body
#image

#add the list app to the setting

#create a migration

#Migrate

#Add to the admin