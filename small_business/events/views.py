import email
from typing import Type
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Event, Customer

from calendar import HTMLCalendar


def all_public_events(request):
    events_list = Event.objects.filter(kind=Event.Type_choices.public)
    return render(request, 'events/events_list.html', {'events_list': events_list
                                                    })


def show_book(request):
    if request.method == "POST":
        email = request.POST['email']
        event_id = request.POST['event_id']
        customer_booked= False
        if email:
            try:
                customer = Customer.objects.get(email = email)
                customer_id=customer.id
                customer_id=customer.id
            except:
                customer = Customer(email=email)
                customer.save()
                customer_id=customer.id
            
            event=Event.objects.get(pk=event_id)
            try:
                event.attendees.get(pk = customer_id)
                customer_booked = True
            except:
                pass

            return render(request, 'events/show_book.html',{'event': event, 'customer': customer, 'booked' : customer_booked})
    else:
        return render(request, 'events/events_list.html',{})


def update_book(request):
    if request.method == "POST":
        #import ipdb; ipdb.set_trace()
        customer_id = request.POST['customer_id']
        event_id = request.POST['event_id']
        customer = Customer.objects.get(pk = customer_id)
        event=Event.objects.get(pk=event_id)
        event.attendees.add(customer)
        events_list = Event.objects.filter(kind=Event.Type_choices.public)
        return render(request, 'events/events_list.html', {'events_list': events_list
                                                    })


def cancel_book(request):
    if request.method == "POST":
        customer_id = request.POST['customer_id']
        event_id = request.POST['event_id']
        customer = Customer.objects.get(pk = customer_id)
        event=Event.objects.get(pk=event_id)
        event.attendees.remove(customer)
        events_list = Event.objects.filter(kind=Event.Type_choices.public)
        return render(request, 'events/events_list.html', {'events_list': events_list
                                                    })