def make_compose(name, web_port, connect_port):
    static = open("./init/init_compose", "r", encoding='utf8')
    dynamic = open(f"{name}-compose.yml", "w", encoding='utf8')

    for i in static:
        if "_color" in i:
            i = i.replace("_color", name)
        if "_ports" in i:
            i = i.replace("_ports", f"{web_port}")
        if "_connect" in i:
            i = i.replace("_connect", f"{connect_port}")
        dynamic.write(i)
    static.close()
    dynamic.close()
