import json

from django.http        import JsonResponse
from django.views       import View

from restaurants.models import Restaurant

class RestaurantView(View):
    def get(self,request,category_id):
        try:
            limit  = int(request.GET.get('limit',10))
            offset = int(request.GET.get('offset',0))

            if category_id == 7:
                restaurants = Restaurant.objects.all()[offset:offset+limit]
            else:
                restaurants = Restaurant.objects.filter(category_id=category_id)

            result = [{
                'name'            : restaurant.name,
                'address'         : restaurant.address,
                'thumbnail_image' : restaurant.thumbnail_image.thumbnail_image,
                'open_time'       : restaurant.open_time.strftime('%H:%M'),
                'close_time'      : restaurant.close_time.strftime('%H:%M'),
                'categorty'       : restaurant.category.name,
                'latitude'        : restaurant.latitude,
                'longitude'       : restaurant.longitude,
            } for restaurant in restaurants]

            return JsonResponse({'result':result},status=200)
        except ValueError:
            return JsonResponse({'message':'valueError'},status=400)