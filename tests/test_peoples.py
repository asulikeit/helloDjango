from rest_framework import status
from rest_framework.test import APITestCase

class JustTest(APITestCase):

    def test01_peoples(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
            {'name': 'yunghui', 'description': 'Lee Young-hui'},
        ]
        resp = self.client.post("/peoples/", people_list, follow=True, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        # Create
        data = { 'peoples': people_list }
        resp = self.client.post("/peoples/", data, follow=True, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 2)

        # Read
        req_id = str(resp.data[0])
        resp = self.client.get(f"/peoples/{req_id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('description'), 'Kim Chul-su')

        # Update
        update_data = {
            'description': 'Park Chul-su'
        }
        resp = self.client.post(f"/peoples/{req_id}/", update_data)
        self.assertEqual(resp.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(resp.data.get('description')[0], 'Park Chul-su')

        resp = self.client.get("/peoples/0")
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

        # List
        resp = self.client.get("/peoples/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['data']), 2)

        # Delete
        req_id = str(resp.data['data'][0]['id'])
        header = {'HTTP_X_HTTP_METHOD_OVERRIDE': 'DELETE'}
        resp = self.client.post(f'/peoples/{req_id}', **header)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        resp = self.client.get("/peoples/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['data']), 1)