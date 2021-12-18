### docker로 무중단 배포 환경을 조성해보았습니다.

```
EC2{
  Nginx{
    if app-1 running:
      port 80 -> 8000
    if app-2 running:
      port 80 -> 8010
  }
  Docker{
    django-app-1{
      8000:8000
    }
    django-app-2{
      8010:8000
    }
  }
}
```

### sudo python3 py_get_state.py

젠킨스의 빌드 명령입니다.

접속 주소는
http://honeycombpizza.link/admin/
입니다.

### 과정.

1.  py_get_state에서
    py_get_inform을 호출하여, shell exec에서
    실행된 명령의 결과를 가져옵니다.

    (컨테이너이름,ID,이미지이름,포트,IP를
    join하여 리스트형태로 만듭니다.)

2.  현재 실행되고 있는 컨테이너 중에 web으로 설정한
    컨테이너가 있으면 prev_con에 저장합니다.
3.  init파일들을 기준으로 새 도커,nginx파일들을 생성합니다.
4.  새 이미지와 컨테이너를 빌드합니다.
5.  빌드와 종료 시퀀스 사이에 테스트 코드를 넣을 수 있습니다.
6.  모든 빌드가 끝난 뒤 약 20초뒤에
7.  nginx의 포트를 새 포트로 바꾸고 리로드합니다.
8.  prev_con에 저장된 컨테이너 이름과, 이미지를 이용해
9.  shell exec에 도커 컨테이너, 이미지 삭제명령을 호출합니다.#

#
