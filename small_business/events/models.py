from datetime import datetime
from email.policy import default
from enum import unique
from time import timezone
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField('Customer First Name', max_length=64, null=True)
    last_name = models.CharField('Customer Last Name', max_length=64, null= True)
    email =models.EmailField('Customer Email', max_length=64, null= False, unique=True)

    def __str__(self):
        return self.email




class Room(models.Model):
    alias = models.CharField('Room Alias', max_length=16, null=True)
    capacity = models.PositiveSmallIntegerField('Capacity', null = False, unique= True)

    def __str__(self):
        return self.alias + ' have a capacity for ' + str(self.capacity)





class Event(models.Model):
    class Type_choices(models.TextChoices):
        private = "1", "PRIVATE"
        public  = "0", "PUBLIC"

    name = models.CharField('Event Name', max_length=64, blank= False, null= False)
    date = models.DateField('Event Date', blank=False, null= False, unique = True)
    time = models.TimeField('Event Time', blank=False, null= False)
    kind = models.CharField(max_length=9,choices=Type_choices.choices, null= False)
    description =models.TextField(blank=True)
    attendees = models.ManyToManyField(Customer, blank = True,related_name="attendees")
    room = models.ForeignKey(Room, blank= False, null=False, on_delete=models.PROTECT,related_name="event_room")

    def __str__(self):
        return self.name