import json
import bcrypt

from django.test import TestCase, Client

from .models import Reservation

class ReservationTest(TestCase):
    def setUp(self):
        Reservation.objects.create(
            user_id       = user.id,
            restaurant_id = restaurant_id,
            date          = date,
            visitor_count = visitor_count,
            timeslot      = timeslot,
            status_id     = 1,
        )
    def tearDown(self):
        Reservation.objects.all().delete()


    def test_reservationview_post_success(self):
        client = Client()
        reservation = {
            'user_id' : '1',
            'restaurant_id' : '1',
            'date' : '"2022-06-01',
            'timeslot' : '1',
            'visitor_count' : '4'
        }
        response = client.post('/reservations', json.dumps(reservation, content_type='application/json'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
            {
                'message' : 'SUCCESS'
            }
        )
    
    def test_reservationview_get_success(self):
        client = Client()
        response = client.get('/reservations',
            {
                'restaurant_id' : '1',
                'date' : '"2022-06-01',
            }
        )


        client = Client()
        reservation = {
            'user_id' : '1',
            'restaurant_id' : '1',
            'date' : '"2022-06-01',
            'timeslot' : '1',
            'visitor_count' : '4'
        }
        response = client.post('/reservations', json.dumps(reservation, content_type='application/json'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
            {
                'message' : 'SUCCESS'
            }
        )