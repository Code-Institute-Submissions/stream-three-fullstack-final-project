from django import forms
from django.test import TestCase
from .forms import UserLoginForm, UserRegisterForm

## TEST ACCOUNTS APP FORMS ##
class TestUserLoginForm(TestCase):
    
    def test_user_login_form(self):
        form = UserLoginForm({'username':'test_user',
                                'password':'testpassword'})

        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_fields(self):
        form = UserLoginForm({'username':'',
                                'password':''})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class TestUserRegisterForm(TestCase):

    def test_can_register_a_user(self):
        form = UserRegisterForm({'first_name': 'Test',
                                    'last_name': 'Test',
                                    'username':'testuser',
                                    'email':'testuser@user.com',
                                    'password1': 'password',
                                    'password2': 'password' })
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_fields(self):

        form = UserRegisterForm({'first_name': 'Test',
                                    'last_name': 'Test',
                                    'username':'',
                                    'email':'',
                                    'password1': '',
                                    'password2': '' })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        self.assertEqual(form.errors['email'], [u'This field is required.'])
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        self.assertEqual(form.errors['password2'], [u'This field is required.'])

