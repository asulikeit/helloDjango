from rest_framework import status
from rest_framework.test import APITestCase

from tests.test_base import test_people

class JustTest(APITestCase):

    def test01_membership_paging(self):
        membership_list = [
            {'name': 'academy', 'description': 'academy membership'},
            {'name': 'school', 'description': 'school membership'},
        ]

        for i in range(1, 11):
            membership_list.append({'name': 'membership' + str(i), 'description': 'test' + str(i)})

        data = { 'memberships': membership_list }
        resp = self.client.post("/memberships", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 12)

        resp = self.client.get("/memberships?page=1&size=10")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data.get('data')), 10)

        resp = self.client.get("/memberships?page=2&size=10")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data.get('data')), 2)
