from django.db import models
from datetime import datetime

class Personal_List(models.Model):
    title = models.CharField(default='null',max_length=200)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    description = models.TextField(null=True) #models.CharField(max_length=200)
    #image = models.ImageField(upload_to='Dowmloads/')
    order = models.IntegerField(default=0)
    #priority = models.Foreignkey(Priority)
    #state = models.Foreignkey(State)
        

'''class Priority(models.Model):

    def __init__(self):
        number_priority = odels.IntegerField(default=0)
        description_priority = models.CharField(max_length=200)


class State(models.Model):

    def __init__(self):
        number_state = odels.IntegerField(default=0)
        description_state = models.CharField(max_length=200)'''

#create a list model
#title
#pub_date
#body
#image

#add the list app to the setting

#create a migration

#Migrate

#Add to the admin