### docker로 무중단 배포 환경을 조성해보았습니다.

```
EC2{
  Nginx{
    app-1 80 -> 8000,
    app-2 80 -> 8010
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
