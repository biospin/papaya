<h2>구글앱엔진 시작하기</h2>

<h5> 1. 구글 클라우드 SDK 설치 </h5> 

<https://cloud.google.com/appengine/>

구글앱엔진 사이트에 들어가서 "지금 사용해 보기" 클릭

프로젝트명 짓고, '예제 프로젝트' 를 다운로드 해놓자.

일단 이 예제 프로젝트를 실행해보고 배포해보자.

그리고 구글 클라우드 sdk 설치

```
$ curl https://sdk.cloud.google.com/ | bash
```

CA 문제로 인해 위 명령어가 실행이 안된다면,

<https://cloud.google.com/sdk/> 에서 압축파일을 받아서 

```
sdk 폴더 $ ./install.sh
```
로 설치하면 된다.


<h5> 2. 로컬에서 띄워보기 </h5> 

프로젝트 폴더가 보이는 터미널 위치에서 실행한다.

```
$ dev_appserver.py <폴더명>
```


<h5> 3. 배포하기 </h5>

마찬가지로, 프로젝트 폴더가 보이는 터미널 위치에서 

```
$ appcfg.py -A <할당받은 app-id> update <폴더명>
```

app-id : 구글앱엔진에서 프로젝트 생성시 할당받은 application id 



<h5> 4. hello 변경해서 다시 배포해보자. </h5>


예제 프로젝트로 django, flask, bottle 등등 

인덱스의 hello 문자를 변경하고 한번 더 배포한다음 제대로 적용됬는지 확인해보자.