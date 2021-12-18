### docker로 무중단 배포 환경을 조성해보았습니다.
EC2{
  Nginx{
  }
  Docker{
    django-app-1{
    
    }
    django-app-2{
    
    }
  }
}
### python py_get_state.py

도커컴포즈업 명령입니다.
이후 get_state할 때마다 nginx 가 :8000과 8010으로 연결을 바꿉니다.

접속 주소는
http://honeycombpizza.link/admin/login/?next=/admin/
입니다.
