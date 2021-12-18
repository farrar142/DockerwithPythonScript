from pyscript.py_get_informs import *
from pyscript.py_compose_changer import *
from pyscript.py_port_changer import *
from pyscript.py_dockfile_changer import *
import os
import time


def revise_files(color, web_port, connect_port):
    global container_port, cur_name
    _color = "red" if color == "green" else "green"
    print(f"현재 {_color}. {color}을 빌드합니다.")
    make_compose(color, web_port, connect_port)
    dockfile_change(web_port)
    container_port = web_port
    cur_name = color


def get_current_container(containers):
    for i in containers:
        # print(i)
        if (len(containers) == 0):
            return i
        elif("green" in i[0]):
            return i
        elif("red" in i[0]):
            return i
    return []


# 초기 세팅값들
connect_port = 8000
red_port = 8000
green_port = 8010
# 배포시에 실행되고 있는 웹 컨테이너가 있다면.current에 저장.
# 현재 인스턴스 구하기
prev_con = get_current_container(get_informs())
print(prev_con)
container_port = 0
# 비교 시퀀스
if prev_con:
    if "red" in prev_con[0]:
        revise_files("green", green_port, connect_port)
    else:
        revise_files("red", red_port, connect_port)
else:
    revise_files("green", green_port, connect_port)

port_change(container_port, cur_name)
# 빌드 시퀀스
os.system(f'docker-compose -f {cur_name}-compose.yml up -d')
# 종료시퀀스#
try:
    time.sleep(20)
    os.system(f'docker rm -f {prev_con[1]}')
    os.system(f"docker rmi -f {prev_con[2]}")
    #os.system('docker --remove-orphans')
    os.system('systemctl reload nginx')
except:
    print("알맞은 명령어가 아니에요")
# os.system("docker ps -a")
