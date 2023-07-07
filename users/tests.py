from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUsersTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'nooooob',
            email = 'test@gmail.com',
            password = 'patwari_2_2_4',
        )
        
        self.assertEqual(user.username, 'nooooob')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'new superuser',
            email = 'supernoob@gmail.com',
            password = 'patwari_2_2_4',
        )
        self.assertEqual(user.username, 'new superuser')
        self.assertEqual(user.email, 'supernoob@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    