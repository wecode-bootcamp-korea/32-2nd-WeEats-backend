import jwt
import json
import requests

from django.http      import JsonResponse
from django.views     import View

from core.utils       import KakaoAPI
from users.models     import User
from we_eats.settings import SECRET_KEY,ALGORITHM
from datetime         import datetime, timedelta
from core.decorator   import log_in_decorator

class KakaoSignIn(View):
    def post(self, request):
        try:
            access_token  = request.headers['Authorization']
            kakao_service = KakaoAPI(access_token)
            user_info     = kakao_service.get_kakao_user()

            kakao_id      = user_info['id']
            nickname      = user_info['properties']['nickname']
            profile_image = user_info['properties']['profile_image']

            if not User.objects.filter(kakao_id=kakao_id).exists():
                User.objects.create(
                    kakao_id      = kakao_id,
                    name          = nickname,
                    profile_image = profile_image,
                )
            
            if User.objects.get(kakao_id=kakao_id).profile_image != profile_image:
                user         = User.objects.get(kakao_id=kakao_id)
                user.profile = profile_image

            user_id      = User.objects.get(kakao_id=kakao_id).id
            access_token = jwt.encode({'id':user_id, 'exp':datetime.utcnow() + timedelta(days=1)}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'access_token' : access_token}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @log_in_decorator
    def get(self,request):
        user          = request.user
        name          = user.name
        profile_image = user.profile_image

        return JsonResponse({
            'id'            : user.id,
            'name'          : name,
            'profile_image' : profile_image,
        }, status=200)