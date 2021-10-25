SECRET_KEY="l*)iay+2c832qx$2gv@uc#(k-pi&d-f1$$_++4%k+p+uyf_bn%"
DEBUG=False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sunlab_db',
        'USER': 'octopus',#octopus
        'PASSWORD': 'miyou0209',#octopus2021@! 
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# # CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
SERVER_EMAIL = 'octopus.emailing@gmail.com'
EMAIL_HOST_USER = 'octopus.emailing@gmail.com'
EMAIL_HOST_PASSWORD = 'miyou0209'

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SENTRY_DSN="https://04d0ac627cc74480948a1a1a425506e0@o1038371.ingest.sentry.io/6006665"
