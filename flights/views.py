from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
from django.utils import timezone

class FlightList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightListSerializer

class BookingList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=timezone.now())
	serializer_class = BookingListSerializer