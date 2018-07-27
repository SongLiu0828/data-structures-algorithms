from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    s = Queue()
    for name in namelist:
        s.enqueue(name)

    while s.size() > 1:
        for i in range(num):
            s.enqueue(s.dequeue())

        s.dequeue()

    return s.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
