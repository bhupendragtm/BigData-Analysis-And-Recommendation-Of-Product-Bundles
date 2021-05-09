
#we are sending emails through Django
# this is the example.... create a local_settings.py file and copy this

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email id to send email'
EMAIL_HOST_PASSWORD = 'your password'