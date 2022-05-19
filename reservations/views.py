import json

from enum             import Enum
from django.views     import View
from django.http      import JsonResponse

from django.db        import IntegrityError
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
        try:
            data          = json.loads(request.body)
            user          = request.user
            restaurant_id = data['restaurant_id']
            date          = data['date']
            timeslot      = data['timeslot']
            visitor_count = data['visitor_count']

            restaurant = Restaurant.objects.get(id=restaurant_id)

            if Reservation.objects.filter(user_id=user.id, date=date, timeslot=timeslot).exclude(status_id=ReservationStatus.CANCELLED.value).exists():
                return JsonResponse({'message' : 'USER_HAS_ANOTHER_RESERVATION'}, status=400)

            reserved_slots = Reservation.objects.filter(restaurant_id=restaurant_id, date=date, timeslot=timeslot).exclude(status_id=ReservationStatus.CANCELLED.value)
            
            if reserved_slots.exists():
                reserved_count = reserved_slots.aggregate(reserved_count=Sum('visitor_count'))['reserved_count']
                
                if (int(visitor_count) + int(reserved_count)) > int(restaurant.max_capacity):
                    return JsonResponse({'message' : 'INVALID_RESERVATION_REQUEST'}, status=400)

            else:
                if int(visitor_count) > int(restaurant.max_capacity):
                    return JsonResponse({'message' : 'INVALID_RESERVATION_REQUEST'}, status=400)

            Reservation.objects.create(
                user_id       = user.id,
                restaurant_id = restaurant_id,
                date          = date,
                visitor_count = visitor_count,
                timeslot      = timeslot,
                status_id     = ReservationStatus.SUBMITTED.value,
            )

            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except IntegrityError: 
            return JsonResponse({"Message" : "WRONG_DATA_INPUT"}, status=400)


    def get(self, request):
        restaurant_id = request.GET.get('restaurant_id', None)
        date          = request.GET.get('date', None)

        if not restaurant_id or not date:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

        restaurant_filter = Q()
        restaurant_filter &= Q(restaurant_id=restaurant_id)
        restaurant_filter &= Q(date=date) 
        restaurant_filter &= (~Q(status_id=ReservationStatus.CANCELLED.value))

        max_count    = Restaurant.objects.get(id=restaurant_id).max_capacity
        reservations = Reservation.objects.filter(restaurant_filter).values('timeslot').annotate(total_visitor_count=Sum('visitor_count'))

        available_seats_list = [{
            "timeslot"        : available_seat['timeslot'],
            "remaining_seats" : max_count - available_seat['total_visitor_count']
        }for available_seat in reservations]

        return JsonResponse({"available_seats_list" : available_seats_list}, status=200)