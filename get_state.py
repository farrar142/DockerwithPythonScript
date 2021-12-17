from get_informs import *
from compose_changer import *
from port_changer import *
from wait_changer import *
import os
import time
# 초기 세팅값들
host_port = 8000
red_port = 8000
green_port = 8010
# 배포시에 실행되고 있는 웹 컨테이너가 있다면.current에 저장.
current_running = []
# 현재 인스턴스 구하기
status = get_informs()
for i in status:
    # print(i)
    if (len(current_running) == 0):
        if ("red" in i[0]):
            con_name = "red"
            current_running = i
            break
        elif("green" in i[0]):
            con_name = "green"
            current_running = i
            break
print(current_running)
container_port = 0
# 비교 시퀀스
if current_running:
    if "red" in current_running[0]:
        print("현재 레드. 그린을 빌드합니다.")
        make_compose("green", green_port, host_port)
        make_wait(green_port)
        container_port = green_port
        cur_name = "green"
    else:
        print("현재 그린, 레드을 빌드합니다.")
        make_compose("red", red_port, host_port)
        make_wait(red_port)
        container_port = red_port
        cur_name = "red"
else:
    print("컨테이너 없음 그린을 빌드합니다.")
    make_compose("green", green_port, host_port)
    make_wait(green_port)
    container_port = green_port
    cur_name = "green"

port_change(container_port, cur_name)
# 빌드 시퀀스
os.system(f'docker-compose -f {cur_name}-compose.yml up -d')
# 종료시퀀스
try:
    time.sleep(20)
    os.system(f'docker rm -f {current_running[1]}')
    os.system(f"docker rmi {current_running[2]}")
    os.system('docker --remove-orphans')
except:
    print("알맞은 명령어가 아니에요")
#os.system("docker ps -a")
