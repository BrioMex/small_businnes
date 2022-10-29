from django.urls import path
from . import views 


urlpatterns = [
    #path('', views.home, name = "home"), #first: defining url in browser, second: function or class name, third name assigned ofr easy calling
    path('', views.all_public_events, name= "events-list"),
    path('book/', views.show_book, name= "show-book"),
    path('update_book/', views.update_book, name= "update-book"),
    path('cancel_book/', views.cancel_book, name= "cancel-book"),
    
]





# {% extends 'events/base.html' %}

# {% block content %}
#     <center>
#         {{event}}

#         <form class="d-flex" method= POST action= {% url 'update-customer' %} role="search">
#             {% csrf_token %}
#             <input class="form-control me-2" type="search" placeholder="Search Customer" aria-label="Your email" name="searched">
#             <button class="btn btn-outline-secondary" type="submit">Search</button>
#         </form>
        
#     </center>

# {% endblock content %}