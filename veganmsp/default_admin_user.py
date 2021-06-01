from django.db import IntegrityError
from django.contrib.auth.models import User


SU_NAME = 'admin'
SU_PASS = 'admin'
SU_MAIL = ''

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
except Exception as e:
	print(e)
