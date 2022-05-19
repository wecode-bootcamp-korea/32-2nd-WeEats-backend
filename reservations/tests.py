import json
import jwt

from django.test   import TestCase, Client

from my_settings        import SECRET_KEY, ALGORITHM
from .models            import Reservation, ReservationStatus
from restaurants.models import Restaurant, Category, Restaurant_Image
from users.models       import User

class ReservationTest(TestCase):
    def setUp(self):
        User.objects.create(
            id            = 1,
            name          = "민석",
            kakao_id      = 123456789,
            profile_image = "http://test.jpg"
        )
        ReservationStatus.objects.create(
            id     = 1,
            status = "예약접수"
        )
        Category.objects.create(
            id   = 1,
            name = "korean"
        )
        Restaurant_Image.objects.create(
            id              = 1,
            thumbnail_image = "thumbnail_image.jpg"
        )
        Restaurant.objects.create(
            id                 = 1,
            name               = "식당1",
            address            = "서울특별시 강남구",
            latitude           = "37.536881",
            longitude          = "126.999538",
            open_time          = "12:00",
            close_time         = "20:00",
            detail_image       = "image.jpg",
            category_id        = 1,
            thumbnail_image_id = 1,
            max_capacity       = 20
        )
        Reservation.objects.create(
            user_id       = 1,
            restaurant_id = 1,
            date          = "2022-06-05",
            visitor_count = 4,
            timeslot      = 4,
            status_id     = 1,
        )

    def tearDown(self):
        User.objects.all().delete()
        Reservation.objects.all().delete()
        Restaurant.objects.all().delete()
        Category.objects.all().delete()
        Restaurant_Image.objects.all().delete()
        ReservationStatus.objects.all().delete()

    def test_success_post_reservations(self):
        client  = Client()
        token   = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        headers = {'HTTP_Authorization':token}

        reservation = {
            'user_id'       : 1,
            'restaurant_id' : 1,
            'date'          : '2022-06-05',
            'timeslot'      : 3,
            'visitor_count' : 1
        }
        
        response = client.post('/reservations',
            json.dumps(reservation), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
            {
                'message' : 'SUCCESS'
            }
        )
    
    def test_fail_post_duplicate_reservations(self):
        client  = Client()
        token   = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        headers = {'HTTP_Authorization':token}

        reservation = {
            'user_id'       : 1,
            'restaurant_id' : 1,
            'date'          : '2022-06-05',
            'timeslot'      : 4,
            'visitor_count' : 1
        }
        
        response = client.post('/reservations',
            json.dumps(reservation), content_type='application/json', **headers)

        self.assertEqual(response.json(),
            {
                'message' : 'USER_HAS_ANOTHER_RESERVATION'
            }
        )

    def test_fail_post_invalid_reservations(self):
        client  = Client()
        token   = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        headers = {'HTTP_Authorization':token}

        reservation = {
            'user_id'       : 1,
            'restaurant_id' : 1,
            'date'          : '2022-06-08',
            'timeslot'      : 4,
            'visitor_count' : 100
        }
        
        response = client.post('/reservations',
            json.dumps(reservation), content_type='application/json', **headers)

        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_RESERVATION_REQUEST'
            }
        )
    
    def test_success_get_reservations(self):

        client = Client()
        response = client.get('/reservations?restaurant_id=1&date=2022-06-05')

        available_seats_list = [{
            "timeslot"        : 4,
            "remaining_seats" : 16
        }]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'available_seats_list' : available_seats_list
            }
        )
    
    def test_fail_get_reservations_keyerror_date(self):

        client = Client()
        response = client.get('/reservations?restaurant_id=1')
        
        self.assertEqual(response.status_code, 400)

    def test_fail_get_reservations_keyerror_restaurant_id(self):

        client = Client()
        response = client.get('/reservations?date=2022-06-02')
        
        self.assertEqual(response.status_code, 400)