from rest_framework import status
from rest_framework.test import APITestCase

from apps.peoples.models import PhoneNumber

class JustTest(APITestCase):

    def test01_numbers_crud(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
        ]
        data = { 'peoples': people_list }
        resp = self.client.post("/peoples/", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 1)
        people_id = resp.data[0]

        pnumber_list = [ '010-1234-5678', '010-2345-6789' ]
        data = { 'phonenumbers': pnumber_list}
        resp = self.client.post(f'/peoples/{people_id}/phonenumbers', data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
