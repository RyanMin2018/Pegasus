<p>아직 완성도는 40% 수준이니, 함부로 데리고 가지 않습니다.</p>

<p>먼저 앱 루트에서</p>

<pre>
$ python manage.py startapp main
$ python manage.py startapp blog
$ python manage.py startapp poll
</pre>

<p>를 실행 한 후에 "settings.py"를 아래와 같이 수정</p>

<hr />

<p>INSTALLED_APPS에 ‘main’, ‘blog’, ‘poll’를 'django.contrib.admin' 앞에넣어주시고,</p>

<pre>
INSTALLED_APPS = [
    'main',
    'blog',
    'poll',
    …
]
</pre>

<p>로그인 후 리다이랙션될 url을 settings.py 문서 맨마지막에 추가합니다.</p>

<pre>
LOGIN_REDIRECT_URL = '/'
</pre>
