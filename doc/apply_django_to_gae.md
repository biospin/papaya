<h2>장고 프로젝트 구글앱엔진에 배포하기 </h2>
(DB model 수정을 제외한 버전)

<h5> 1. 장고 프로젝트 내에 app. yaml 추가 </h5> 

```
application: <앱-id>
version: 1
runtime: python27
api_version: 1
threadsafe: true

libraries:
- name: django
  version: "latest"

builtins:
- django_wsgi: on

env_variables:
  DJANGO_SETTINGS_MODULE: '<프로젝트명>.settings'
```

<h5> 2. setting.py 파일 수정 </h5>

```
... 

# 미들웨어 수정 (필수사항은 아님)
MIDDLEWARE_CLASSES = (
    ...
    # 아직 ssl 인증서 준비가 안됬으니 일단 주석처리 
    # 'django.middleware.csrf.CsrfViewMiddleware',
    
    # 만약 장고 1.7 로 프로젝트 생성시 아래 기능 주석처리 필요
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    ...
)

...

# DB 부분 주석처리
# DATABASES = {...}

...
```

<h5> 3. 로컬에서 돌려보기 </h5>

해당 프로젝트가 포함된 폴더에서 명령어를 통해 로컬에서 띄워보자.

```
$ ls
myapp 

$ dev_appserver.py myapp
...
INFO     2014-11-03 12:50:45,326 dispatcher.py:186] Starting module "default" running at: http://localhost:8080
INFO     2014-11-03 12:50:45,331 admin_server.py:117] Starting admin server at: http://localhost:8000
```

localhost:8080 으로 들어가서 확인해보자.

<h5> 4. 배포하기 </h5>

```
$ ls 
myapp

... appcfg.py -A <구글엡엔진 앱id> update <프로젝트폴더>

$ appcfg.py -A myappengine-id update myapp
```
