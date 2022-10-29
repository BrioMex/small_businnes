# small_businnes

Use requierements to install dependencies

Customers can make or cancel a reservation accessing http://127.0.0.1:8000/events

Business can use admin to manage rooms and events.

-There are N rooms with M capacity.
-There are two types of events: public and private.
-If the event is public, any customer can book a space.
-If the event is private, no one else can book a space in the room.
-A customer can book a space for an event, if the event is public and there is still space
available.
-A customer can cancel its booking and their space should be available again.
-A customer cannot book a space twice for the same event.

-The business can create a room with M capacity
-The business can create events for every room.
-The business can delete a room if said room does not have any events.
-A customer can book a place for an event.
-A customer can cancel its booking for an event.
-A customer can see all the available public events.

-For now, there is only one event per day.
-Each room has a different capacity.
-Think of each requirement as an endpoint for the API (a Django view).
