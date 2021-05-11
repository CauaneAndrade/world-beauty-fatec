from django.test import TestCase
from world_beauty.core.models import User


class UserTestCase(TestCase):

    def test_create_user(self):
        User.objects.create_user(email='projeto@incrivel.com', password='incrivelmesmo')
        self.assertEquals(User.objects.count(), 1)

    def test_if_user_isnot_superuser(self):
        user = User.objects.create_user(email='projeto@incrivel.com', password='incrivelmesmo')
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User.objects.create_superuser(email='projeto@superincrivel.com', password='superincrivelmesmo')
        self.assertEquals(User.objects.count(), 1)

    def test_if_superuser_is_superuser(self):
        user = User.objects.create_superuser(email='projeto@superincrivel.com', password='superincrivelmesmo')
        self.assertTrue(user.is_superuser)
