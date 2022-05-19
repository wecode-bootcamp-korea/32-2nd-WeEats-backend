from django.views import View
from django.http import JsonResponse,HttpResponse

from core.decorator import log_in_decorator 
from reservations.models import Reservation

class MyPageView(View):
    @log_in_decorator
    def get(self,request):
        user = request.user
        reservations = Reservation.objects.filter(user_id=user.id)
        
        user_info = {
            'name' : user.name,
            'profile_image' : user.profile_image
        }

        reservation_info = [{
            'id'            : reservation.id,
            'dete'          : reservation.date,
            'timeslot'      : reservation.timeslot,
            'visitor_count' : reservation.visitor_count,
            'name'          : reservation.restaurant.name,
            'status'        : reservation.status.status
        }for reservation in reservations]

        return JsonResponse({
            'user_info'        : user_info,
            'reservation_info' : reservation_info
        },status=200)

    def delete(self,request,reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)

        reservation.delete()

        return HttpResponse(status=204)