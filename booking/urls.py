from django.urls import path
from . import views
from .views import BookingList, DestinationDetailView,CancelBookingView

app_name='booking'

urlpatterns = [    
    path('booking_list/', BookingList.as_view(), name='BookingList'),    
    path('destination/<name>', DestinationDetailView.as_view(), name='DestinationDetailView'),
    path('cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
]