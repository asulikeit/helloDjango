from unicodedata import name
from django.test import TestCase
from apps.peoples.domains import ClubUser, SignForm

class SmallTest(TestCase):

    def test01(self):
        sign_form = SignForm()
        sign_form.name = 'name'
        sign_form.description = 'desc'
        club_user = ClubUser(sign_form)
        user_dict = club_user.to_dict()
        self.assertEqual(user_dict['name'], sign_form.name)
        self.assertEqual(user_dict['description'], sign_form.description)
