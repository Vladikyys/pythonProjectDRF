from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Announcement, CustomUser


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo123456xc', status='Customer')
        self.assertEqual(user.email, 'normal@user.com', 'error')
        self.assertEqual(user.status, 'Customer')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)


class AnnouncementsTests(TestCase):

    def test_create_announcement(self):
        user = CustomUser.objects.create_user(email='example1@gmail.com', password='example123string')
        announcement = Announcement.objects.create(title='firstTest', description='string',
                                                   body='string',
                                                   owner=user)
        self.assertEqual(announcement.title, 'firstTest')
        self.assertEqual(announcement.description, 'string')
        self.assertEqual(announcement.body, 'string')
        self.assertEqual(announcement.owner, user)



