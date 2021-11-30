import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(username='user_test',
                                    email='user@test.com',
                                    password='123123')

    assert user.username == 'user_test'
    assert user.email == 'user@test.com'
    assert user.password != '123123'
    assert user.is_active == True
    assert user.is_staff == False
    assert user.is_superuser == False


def test_create_superuser():
    user2 = User.objects.create_superuser(username='superuser_test',
                                              email='admin@test.com',
                                              password='123123')

    assert user2.username == 'superuser_test'
    assert user2.email == 'admin@test.com'
    assert user2.password != '123123'
    assert user2.is_active == True
    assert user2.is_staff == True
    assert user2.is_superuser == True
