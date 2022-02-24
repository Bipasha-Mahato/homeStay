import datetime
from homestay.models import Destination
from booking.models import Booking


def check_availability(destination, check_in, check_out):
    Available_destinations=[]
    booking_list = Booking.objects.filter(destination=destination)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            Available_destinations.append(True)
        else:
            Available_destinations.append(False)
    return all(Available_destinations)
