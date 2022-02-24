from django.db import models
from django.conf import settings
from homestay.models import Destination
from django.urls import reverse_lazy


# # # Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    # amount = models.IntegerField()
    # currency = models.CharField(max_length=10)
    # receipt  = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.user} have booked {self.destination} from {self.check_in} to {self.check_out}'

    def get_cancel_booking_url(self):
        return reverse_lazy('booking:CancelBookingView', args=[self.pk,])
