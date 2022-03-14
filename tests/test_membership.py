from rest_framework import status
from rest_framework.test import APITestCase

from tests.test_base import test_people

class JustTest(APITestCase):

    def test01_membership_crud(self):
        membership_list = [
            {'name': 'academy', 'description': 'academy membership'},
            {'name': 'school', 'description': 'school membership'},
        ]
        resp = self.client.post("/memberships", membership_list, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        data = { 'memberships': membership_list }
        resp = self.client.post("/memberships", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 2)

        req_id = str(resp.data[0])
        resp = self.client.get(f"/memberships/{req_id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('name'), 'academy')

        resp = self.client.get("/memberships/0/")
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

        resp = self.client.get("/memberships/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['data']), 2)

    def test02_membership(self):
        people_ids = test_people(self)

        membership_list = [
            {'name': 'club', 'description': 'club membership'},
            {'name': 'academy', 'description': 'academy membership'},
            {'name': 'party', 'description': 'party membership'},
        ]

        data = { 'memberships': membership_list }
        resp = self.client.post("/memberships", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 3)
        membership_ids = resp.data

        data = {
            'memberships' : [
                membership_ids[0], membership_ids[1]
            ]
        }
        resp = self.client.post(f'/peoples/{people_ids[0]}', data=data)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        resp = self.client.get(f'/peoples/{people_ids[0]}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data.get('memberships')), 2)

        data = {
            'memberships' : [
                membership_ids[1], membership_ids[2]
            ]
        }
        resp = self.client.post(f'/peoples/{people_ids[1]}', data=data)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)


        resp = self.client.get(f'/memberships/{membership_ids[1]}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data.get('peoples')), 2)
        