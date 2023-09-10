from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('mainpage/itemlist.html',views.itemlist, name='itempage'),
    # Other URL patterns can be added here
    path('getstarted/',views.getstarted, name='getstarted')
]
