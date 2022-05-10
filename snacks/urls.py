from django.urls import  path 
from .views import SnackView , SnackDescrptionView

urlpatterns = [
    path('Snack_list',SnackView.as_view(), name='Snack_list'),
    path('snack-view/<int:pk>',SnackDescrptionView.as_view(), name='Snack_detail'),

]
