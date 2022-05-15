from django.test import TestCase, Client
TestCase.maxDiff = None

from restaurants.models import Restaurant, Category, Restaurant_Image

class RestaurantTest(TestCase):
    def setUp(self):
        Category.objects.bulk_create([
            Category(
                id   = 1,
                name = "korean"
            ),
            Category(
                id   = 2,
                name = "japanese"
            ),
            Category(
                id   = 3,
                name = "chinese"
            )
        ])
        Restaurant_Image.objects.bulk_create([
            Restaurant_Image(
                id              = 1,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 2,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 3,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 4,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 5,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 6,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 7,
                thumbnail_image = "thumbnail_image.jpg"
            ),
            Restaurant_Image(
                id              = 8,
                thumbnail_image = "thumbnail_image.jpg"
            )
        ])
        Restaurant.objects.bulk_create([
            Restaurant(
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
            ),
            Restaurant(
                id                 = 2,
                name               = "식당2",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 1,
                thumbnail_image_id = 2,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 3,
                name               = "식당3",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 2,
                thumbnail_image_id = 3,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 4,
                name               = "식당4",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 2,
                thumbnail_image_id = 4,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 5,
                name               = "식당5",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 1,
                thumbnail_image_id = 5,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 6,
                name               = "식당6",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 1,
                thumbnail_image_id = 6,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 7,
                name               = "식당7",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 1,
                thumbnail_image_id = 7,
                max_capacity       = 20
            ),
            Restaurant(
                id                 = 8,
                name               = "식당8",
                address            = "서울특별시 강남구",
                latitude           = "37.536881",
                longitude          = "126.999538",
                open_time          = "12:00",
                close_time         = "20:00",
                detail_image       = "image.jpg",
                category_id        = 1,
                thumbnail_image_id = 8,
                max_capacity       = 20
            )
        ])

    def tearDown(self):
        Restaurant.objects.all().delete()
        Category.objects.all().delete()
        Restaurant_Image.objects.all().delete()

    def test_success_get_restaurant_data_all(self):
        client   = Client()
        response = client.get('/restaurants')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {'message' : 'SUCCESS',
            'restaurant_detail' : [
                    {
                        'id'              : 1,
                        'name'            : "식당1",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 2,
                        'name'            : "식당2",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 3,
                        'name'            : "식당3",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 2,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 4,
                        'name'            : "식당4",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 2,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 5,
                        'name'            : "식당5",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 6,
                        'name'            : "식당6",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 7,
                        'name'            : "식당7",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 8,
                        'name'            : "식당8",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 1,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    }
                ]})

    def test_success_get_restaurant_data_through_category_filter(self):
        client   = Client()
        response = client.get('/restaurants?category_id=2')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {'message' : 'SUCCESS',
            'restaurant_detail' : [
                    {
                        'id'              : 3,
                        'name'            : "식당3",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 2,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    },
                    {
                        'id'              : 4,
                        'name'            : "식당4",
                        'address'         : "서울특별시 강남구",
                        'open_time'       : "12:00",
                        'close_time'      : "20:00",
                        'latitude'        : "37.536881",
                        'longitude'       : "126.999538",
                        'detail_image'    : "image.jpg",
                        'category_id'     : 2,
                        'thumbnail_image' : 'thumbnail_image.jpg',
                    }
            ]}
        )

    def test_success_get_restaurant_data_in_random_order(self):

        client   = Client()
        response = client.get('/restaurants?order=random')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['restaurant_detail']), 8)

    def test_fail_get_restaurant_data_in_invalid_category(self):
        client   = Client()
        response = client.get('/restaurants?category_id=7')

        self.assertEqual(response.json(), {'message' : 'INVALID_CATEGORY'})

    def test_fail_get_restaurant_data_in_invalid_order(self):
        client   = Client()
        response = client.get('/restaurants?order=ascending')

        self.assertEqual(response.json(), {'message' : 'INVALID_ORDER'})