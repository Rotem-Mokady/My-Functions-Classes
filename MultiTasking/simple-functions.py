num = 100000

def rotem():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotem": counter}


def rotemm():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotemm": counter == 123456789}


def rotemmo():
    counter = 0
    for i in range(num):
        counter += i
    return {"rotemmo": counter ** 0.5}


def rotemmok():
    counter = 0
    for i in range(num):
        counter -= i*2
    return {"rotemmok": counter}
