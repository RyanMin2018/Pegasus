
# This has NOT “settings.py”. Add content to your “settings.py” file as follows:




<p>add ‘Main’, ‘blog’, ‘poll’ before 'django.contrib.admin' in INSTALLED_APPS.</p>

<pre>
INSTALLED_APPS = [
    'main',
    'blog',
    'poll',
    …
]
</pre>

<p>add Redirection Url After Login</p>

<pre>
LOGIN_REDIRECT_URL = '/'
</pre>
