from django.urls import path
from . import views

urlpatterns = [path('',views.index,name='index'),
              path('profile',views.profile,name='profile'),
              path('chennai',views.chennai,name='chennai'),
              path('dishes',views.dishes,name='dishes')
]
