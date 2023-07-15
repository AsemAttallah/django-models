from django.urls import path
from .views import HomeView, SnacksListView, SnacksDetailsView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('snacks/',SnacksListView.as_view(),name='snacks_list'),
    path('<pk>/',SnacksDetailsView.as_view(),name='snacks_details')
]