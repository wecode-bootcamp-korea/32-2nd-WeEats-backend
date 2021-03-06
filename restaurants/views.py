from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from core.utils          import validate_category, validate_order_random
from restaurants.models  import Restaurant
from reservations.models import Reservation

class RestaurantView(View):
    def get(self, request):
        try:
            offset      = int(request.GET.get('offset', 0))
            limit       = int(request.GET.get('limit', 8))
            category_id = request.GET.get('category_id', None)
            order       = request.GET.get('order', None)
            
            if order:
                validate_order_random(order)
                restaurants = Restaurant.objects.order_by('?')[:limit]
                
            elif category_id:
                validate_category(category_id)
                restaurants = Restaurant.objects.filter(category_id=category_id)
                
            else:
                restaurants = Restaurant.objects.all()[offset:offset+limit]

            restaurant_detail = [{
                'id'              : restaurant.id,
                'name'            : restaurant.name,
                'address'         : restaurant.address,
                'open_time'       : restaurant.open_time.strftime('%H:%M'),
                'close_time'      : restaurant.close_time.strftime('%H:%M'),
                'latitude'        : restaurant.latitude,
                'longitude'       : restaurant.longitude,
                'detail_image'    : restaurant.detail_image,
                'category_id'     : restaurant.category.id,
                'thumbnail_image' : restaurant.thumbnail_image.thumbnail_image,
            }for restaurant in restaurants]

            return JsonResponse({'message': 'SUCCESS', 'restaurant_detail' : restaurant_detail}, status = 200)
            
        except ValidationError as error:
            return JsonResponse({'message' : error.message}, status=error.code)


class RestaurantDetailView(View):
    def get(self, request, restaurant_id):
        try:

            restaurant = Restaurant.objects.get(id=restaurant_id)

            restaurant_detail = [{
                'id'              : restaurant.id,
                'name'            : restaurant.name,
                'address'         : restaurant.address,
                'open_time'       : restaurant.open_time.strftime('%H:%M'),
                'close_time'      : restaurant.close_time.strftime('%H:%M'),
                'latitude'        : restaurant.latitude,
                'longitude'       : restaurant.longitude,
                'detail_image'    : restaurant.detail_image,
                'category_id'     : restaurant.category.id,
                'thumbnail_image' : restaurant.thumbnail_image.thumbnail_image,
            }]

            reservations = Reservation.objects.filter(restaurant_id=restaurant_id)

            reserved_slots = [{
                'date'     : reservation.date,
                'timeslot' : reservation.timeslot
            } for reservation in reservations]

            return JsonResponse({'restaurant_detail' : restaurant_detail, 'reserved_slots' : reserved_slots}, status=200)

        except Restaurant.DoesNotExist:
            return JsonResponse({'message' : 'RESTAURANT_DOES_NOT_EXIST'}, status=404)