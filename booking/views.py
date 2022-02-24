from django.shortcuts import render, redirect
# from django.contrib import messages, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from .models import Booking
from homestay.models import Destination
from .forms import AvailabilityForm
from .booking_function import availability
from booking.booking_function.availability import check_availability
from django.urls import reverse, reverse_lazy
from lib2to3.tests import data

import razorpay


# Create your views here.


class BookingList(ListView):
    model = Booking
    template_name="booking_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class DestinationDetailView(View):
    def get(self, request, *args, **kwargs):
        destination_ima = self.kwargs.get('ima', None)
        destination_name = self.kwargs.get('name', None)
        destination_desc = self.kwargs.get('desc', None)
        destination_price = self.kwargs.get('price', None)
        destination_amt = self.kwargs.get('price', None)
        destination_address = self.kwargs.get('address', None)
       
        form = AvailabilityForm()
        destination_list = Destination.objects.filter(name=destination_name)
        
        
        if len(destination_list) > 0:
            destination = destination_list[0]
            context={
                'destination_ima': destination.ima,
                'destination_name': destination.name,
                'destination_desc': destination.desc,
                'destination_price': destination.price,
                'destination_address': destination.address, 
                'destination_amt': destination.price*100,
                'form': form,
            }
            return render(request, 'destination_detail_view.html', context)
        else:
            
            return render(request, "No_dest.html")
        

    def post(self, request, *args, **kwargs):
        client = razorpay.Client(auth=("rzp_test_YMotQikULPyely", "0it5KxnQusQ62v8jPLRTkYD2"))
        
        destination_name = self.kwargs.get('name', None)
        destination_list = Destination.objects.filter(name=destination_name)
        
        
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data        

        Available_destinations = []
        for destination in destination_list:
            if check_availability(destination, data['check_in'], data['check_out']):
                Available_destinations.append(destination)

        if len(Available_destinations)>0:
            destination = Available_destinations[0]
            booking = Booking.objects.create(
                user = self.request.user,
                destination = destination,
                check_in = data['check_in'],
                check_out = data['check_out']
                
            )
            # paydata=Booking.objects.create(
            #     amount=320,
            #     currency='INR',
            #     receipt='test1'
            # )
            payment=client.order.create({'amount':50000,'currency':'INR','payment_capture':'1'})
            booking.save()
            context = {'msg':booking}
            return render(request, "success.html", context)
        else:
            return render(request, "unsuccess.html")
            



        
class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('booking:BookingList')