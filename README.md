
# This has NOT “settings.py”. Add content to your “settings.py” file as follows:

add ‘Main’, ‘blog’, ‘poll’ before 'django.contrib.admin' in INSTALLED_APPS. 

INSTALLED_APPS = [
    'main',
    'blog',
    'poll',
    …
]

add Redirection Url After Login

LOGIN_REDIRECT_URL = '/'
