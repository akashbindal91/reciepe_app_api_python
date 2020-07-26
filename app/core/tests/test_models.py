from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_sucessful(self):
        """ Text creating a new user with email is successful """
        email = 'rootAdmin@gmail.com'
        password = 'empire123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test user email is normalized """
        # email = 'rootADMIN@gmail.com'
        email = 'rootadmin@gmail.com'
        user = get_user_model().objects.create_user(email, 'empire123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating new user without email raises error value akash """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'empire123')
            # get_user_model().objects.create_user('akash@gmail.com', 'empire123')

    def test_new_superuser(self):
        """ Test creating new Super User """
        user = get_user_model().objects.create_superuser('test@gmail.com', 'test123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
