import json

from django.views     import View
from django.http      import JsonResponse

from restaurants.models  import Restaurant

class MainView(View):
    def get(self,request):
        
        limit = int(request.GET.get('limit',8))

        main_list = Restaurant.objects.order_by('?')[:limit]

        restaurant_detail = [{
            'name': main.name,
            'address': main.address,
            'open_time':main.open_time,
            'close_time':main.close_time,
            'latitude':main.latitude,
            'longitude':main.longitude,
            'detail_image':main.detail_image,
            'category_id':main.category.name,
            'thumbnail_image' : main.thumbnail_image.thumbnail_image,
        }for main in main_list ]

        return JsonResponse({'restaurant_detail' : restaurant_detail}, status = 200)