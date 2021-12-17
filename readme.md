### docker로 무중단 배포 환경을 조성해보았습니다.

무중단을 구현하려 했지만 nginx를 같이 올려서 껐다켜지는 시간
3~5초정도의 딜레이가 있습니다.
EC2에 올린다면 nginx를 도커밖으로 빼서
systemctl restart nginx로 더 시간을 줄일 수 있을 것 같습니다.

### python get_state.py

도커컴포즈업 명령입니다.
이후 get_state할 때마다 nginx 가 :8000과 8010으로 연결을 바꿉니다.

접속 주소는
http://localhost:2000/
입니다.
