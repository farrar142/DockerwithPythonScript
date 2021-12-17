import sys
import os
# 아직은 스크립트형으로 실행시키지만
# 진행상황에 따라서 함수형으로 만들어야됨.


def port_change(port, color):

    # 운영체제 확인
    if os.name == "nt":
        path = "./location"  # 테스트용
    else:
        path = "/etc/nginx/location.d"

    # 경로가 존재하지 않으면 경로를 만듦
    if not os.path.isdir(path):
        os.mkdir(path)

    try:
        # 파일이 존재하지 않으면
        test = open("./_location.conf", "r")
        test.close()
    except:
        # 만들어야됨.
        _tmp = open("./_location.conf", "w")
        _tmp.write("location / {\n" +
                   "    proxy_pass http://honeycombpizza.link:_port;\n" +
                   "}")
        _tmp.close()
        # 복사될 파일
        tmp = open(f"{path}/location.conf", "w")
        tmp.close()

    static = open("./_location.conf", "r", encoding='utf8')
    dynamic = open(f"{path}/location.conf", "w", encoding='utf8')
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

    # nginx 재실행 시킴.
