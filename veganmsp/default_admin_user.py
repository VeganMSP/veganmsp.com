import os

from django.db import IntegrityError
from django.contrib.auth.models import User

SU_NAME = 'admin'
SU_PASS = 'admin'
SU_MAIL = ''


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veganmsp.settings')
    try:
        superuser = User.objects.create_superuser(
            username=SU_NAME,
            password=SU_PASS,
            email=SU_MAIL,
            first_name='admin',
            last_name='admin',
        )
        superuser.save()
    except IntegrityError:
        print(f'Super user with {SU_NAME} already exists.')
    except Exception as e:  # pylint: disable=broad-except
        print(e)


if __name__ == '__main__':
    main()
