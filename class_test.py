class cfg:
    a = 1

print(cfg.a)

def aaxx():
    global cfg
    cfg.a = 12

print(cfg.a)