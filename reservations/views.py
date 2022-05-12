import json

from enum             import Enum
from django.views     import View
from django.http      import JsonResponse
from django.db.models import Sum, Q

from reservations.models import Reservation
from restaurants.models  import Restaurant
from core.decorator      import log_in_decorator

class ReservationStatus(Enum):
    SUBMITTED = 1
    CONFIRMED = 2
    CANCELLED = 3

class ReservationView(View):

    @log_in_decorator
    def post(self, request):
        data          = json.loads(request.body)
        user          = request.user
        restaurant_id = data['restaurant_id']
        date          = data['date']
        timeslot      = data['timeslot']
        visitor_count = data['visitor_count']

        restaurant = Restaurant.objects.get(id=restaurant_id)

        if Reservation.objects.filter(user_id=user.id, date=date, timeslot=timeslot).exclude(status_id=ReservationStatus.CANCELLED.value).exists():
            return JsonResponse({'message' : 'USER_HAS_ANOTHER_RESERVATION'}, status=409)

        reserved_slots = Reservation.objects.filter(restaurant_id=restaurant_id, date=date, timeslot=timeslot).exclude(status_id=ReservationStatus.CANCELLED.value)
        if reserved_slots.exists():
            reserved_count = reserved_slots.aggregate(reserved_count=Sum('visitor_count'))['reserved_count']
            
            if (int(visitor_count) + int(reserved_count)) > int(restaurant.max_capacity):
                return JsonResponse({'message' : 'INVALID_RESERVATION_REQUEST'}, status=409)

        Reservation.objects.create(
            user_id       = user.id,
            restaurant_id = restaurant_id,
            date          = date,
            visitor_count = visitor_count,
            timeslot      = timeslot,
            status_id     = ReservationStatus.SUBMITTED.value,
        )

        return JsonResponse({'message' : 'SUCCESS'}, status=201)

    def get(self, request):
        restaurant_id = request.GET.get('restaurant_id')
        date          = request.GET.get('date')

        max_count    = Restaurant.objects.get(id=restaurant_id).max_capacity
        reservations = Reservation.objects.filter(Q(restaurant_id=restaurant_id) & Q(date=date) & (Q(status_id=ReservationStatus.SUBMITTED.value) | Q(status_id=ReservationStatus.CONFIRMED.value)))
        
        visitor_count_per_timeslot      = reservations.values('timeslot').order_by('timeslot').annotate(total_visitor_count=Sum('visitor_count'))
        visitor_count_per_timeslot_list = list(visitor_count_per_timeslot)

        available_seats_list = [{
            "timeslot"        : visitor_count_per_timeslot_list[available_seat]['timeslot'],
            "remaining_seats" : max_count - visitor_count_per_timeslot_list[available_seat]['total_visitor_count']
        }for available_seat in range(len(visitor_count_per_timeslot_list))]

        return JsonResponse({"available_seats_list" : available_seats_list}, status=200)