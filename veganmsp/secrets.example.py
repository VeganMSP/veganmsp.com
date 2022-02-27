# Database Settings
#
DATABASE_NAME = 'django'
DATABASE_USER = 'django'
DATABASE_PASS = ''
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '5432'

# SMTP Settings
#
EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'django@example.com'
EMAIL_HOST_PASSWORD = 'hunter2'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[Django] '
# Enable if you use TLS (usually port 587)
# EMAIL_USE_TLS=True
# Enable the following if you use SSL (usually port 465)
# EMAIL_USE_SSL=True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = 'admin@example.com'
