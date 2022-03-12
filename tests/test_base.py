from rest_framework import status


def test_people(this):
    people_list = [
        {'name': 'chulsu', 'description': 'Kim Chul-su'},
        {'name': 'yunghui', 'description': 'Lee Young-hui'},
        {'name': 'mansu', 'description': 'Park Man-su'},
    ]
    data = { 'peoples': people_list }
    resp = this.client.post("/peoples/", data, format='json')
    this.assertEqual(resp.status_code, status.HTTP_201_CREATED)
    this.assertEqual(len(resp.data), 3)
    return resp.data
