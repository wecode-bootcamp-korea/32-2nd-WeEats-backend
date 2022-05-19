import re
import requests

from django.core.exceptions import ValidationError
from django.http            import JsonResponse


REGEX_CATEGORY = '[1-6]'
REGEX_ORDER    = '^random$'
class KakaoAPI:
    def __init__(self, access_token):
        self.access_token   = access_token
        self.kakaologin_url = 'https://kapi.kakao.com/v2/user/me'
        self.kakaomap_url   = 'https://kapi.kakao.com/v2/user/kakaomap'

    def get_kakao_user(self):
        headers            = {'Authorization':f'Bearer ${self.access_token}'}
        user_info_response = requests.get(self.kakaologin_url,headers=headers, timeout=5)
        user_info          = user_info_response.json()

        return user_info

def validate_category(category_id):
    if not re.match(REGEX_CATEGORY, category_id):
        raise ValidationError('INVALID_CATEGORY', code=400)

def validate_order_random(category_id):
    if not re.match(REGEX_ORDER, category_id):
        raise ValidationError('INVALID_ORDER', code=400)

class KakaoAPI:
    def __init__(self, access_token):
        self.access_token   = access_token
        self.kakaologin_url = 'https://kapi.kakao.com/v2/user/me'
        self.kakaomap_url   = 'https://kapi.kakao.com/v2/user/kakaomap'

    def get_kakao_user(self):
        headers            = {'Authorization':f'Bearer ${self.access_token}'}
        user_info_response = requests.get(self.kakaologin_url,headers=headers, timeout=5)
        user_info          = user_info_response.json()

        return user_info
