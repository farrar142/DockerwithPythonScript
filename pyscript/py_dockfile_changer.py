def dockfile_change(port):
    static = open("./init/init_dockerfile", "r", encoding='utf8')
    dynamic = open("Dockerfile", "w", encoding='utf8')

    for i in static:
        if "_port" in i:
            i = i.replace("_port", f"{port}")
        dynamic.write(i)
    static.close()
    dynamic.close()
