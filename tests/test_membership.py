from rest_framework import status
from rest_framework.test import APITestCase

class JustTest(APITestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test01_membership(self):
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
        self.assertEqual(len(resp.data), 2)
