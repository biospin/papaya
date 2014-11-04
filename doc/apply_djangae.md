<h2> djangae 적용해서 구글앱엔진에 배포하기</h2>

<h5> 1. 해당 장고 프로젝트 내에 app. yaml 생성하기 </h5> 

```
application: <앱-id>
version: 1
runtime: python27
api_version: 1
threadsafe: true

handlers:

- url: /_ah/(mapreduce|queue|warmup).*
  script: <프로젝트 앱>.wsgi.application
  login: admin

- url: /.*
  script: <프로젝트 앱>.wsgi.application
```


<h5> 2. 해당 프로젝트 root 에 django, djangae 설치 </h5> 
프로젝트 루트 폴더에서 아래 명령어를 실행

```
$ pip install django==1.6 djangae -t .
```
-t 옵션 : 라이브러리 설치 위치 <br>

구글앱엔진은 sandbox 같은 환경에서 실행되기 때문에 
일부 지원하지 않는 라이브러리는 패키지 내에 가지고 있어야 한다.

-t 옵션에 . 을 넣으면 현재 폴더에 설치하라는 의미이다. <br>
따라서 현재 터미널 위치가 해당 프로젝트 루트 폴더가 아니라면 
. 대신 경로를 넣으면 된다.

<h5> 3. setting.py 파일 수정 </h5>

```
# 파일 최상단에 아래 import 줄 추가
from djangae.settings_base import *

...

# 앱명단에 djangae 추가  
INSTALLED_APPS = (
                  ...,
                  'djangae',
)

... 

# 미들웨어 수정 (필수사항은 아님)
MIDDLEWARE_CLASSES = (
    # 제일 첫번째에 djangae 추천하는 보안관련 라이브러리를 적음
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    ...
    ... 
    # 만약 장고 1.7 로 프로젝트 생성시 아래 두개는 주석처리 필요
    # (흠... 장고 1.6 프로젝트 생성으로 하길 추천 -_- 나중에 무슨 문제가 발생할지 모름;)
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    ...
    # 아직 ssl 세팅 (보안 인증 관련)을 안했을 경우 일단 주석처리로 해놓고 돌려보자
    # 'django.middleware.csrf.CsrfViewMiddleware’,
	...
)

...

# DB 부분 주석처리
# DATABASES = {...}

...
```

<h5> 4. managa.py 파일 수정 </h5>

```
if __name__ == "__main__":    
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")    
	
	from djangae.core.management import execute_from_command_line 
	
	execute_from_command_line(sys.argv)
```

<h5> 5. wsgi.py 파일 수정 </h5>

```
from django.core.wsgi import get_wsgi_application

from djangae.wsgi import DjangaeApplication

application = DjangaeApplication(get_wsgi_application())
```

<h5> 6. urls.py 에 다음을 추가 </h5> 

```
url(r'^_ah/', include('djangae.urls'))
```

여기까지 하면 '디버그' 모드로 ssl 사용없이 앱을 실행할 준비가 완료된 상태
로컬에서 실행해보고,
구글앱엔진에 배포해보자.