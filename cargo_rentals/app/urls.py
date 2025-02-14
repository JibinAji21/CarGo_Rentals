from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('shop_home',views.shop_home),
    path('add_car',views.add_car),
    path('budget_cars/<id>',views.budget_cars),
    # path('medium_cars/<id>',views.medium_cars),

]