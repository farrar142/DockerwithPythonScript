import sys
import os
# 아직은 스크립트형으로 실행시키지만
# 진행상황에 따라서 함수형으로 만들어야됨.


def port_change(port, color):

    # 운영체제 확인
    if os.name == "nt":
        path = "./nginx"  # 테스트용
    else:
        path = "/etc/nginx"
    sub_path = "location"

    # 경로가 존재하지 않으면 경로를 만듦
    if not os.path.isdir(f"{path}/{sub_path}"):
        os.mkdir(f"{path}")
        os.mkdir(f"{path}/{sub_path}")

    static = open("./init/init_config", "r", encoding='utf8')
    dynamic = open(f"{path}/location/location.conf", "w", encoding='utf8')
    for i in static:
        try:
            if "port" in i:
                i = i.replace("port", str(port))
            if "_color" in i:
                i = i.replace("_color", color)
            dynamic.write(i)
        except:
            pass
    static.close()
    dynamic.close()

    config = open("./init/init_nginx.conf", "r", encoding='utf-8')
    target = open(f"{path}/nginx.conf", "w", encoding='utf-8')
    for i in config:
        target.write(i)
    config.close()
    target.close()
    # nginx 재실행 시킴.
