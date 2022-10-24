import can
import time 


flag = 0
count = 0
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

canmsg = bus.recv()
while True:
    if flag == 0:
        msgA0 = can.Message(arbitration_id=0xA0, data=[
            0xF1, 0], extended_id=False)
        bus.send(msgA0)
        msgA5 = can.Message(arbitration_id=0xA5, data=[
            count, 0x11, 0, 0, 0, 0, 0, 0], extended_id=False)
        bus.send(msgA5)
        count += 1
        if count == 255:
            count = 0
    if flag == 1:
        msgA5 = can.Message(arbitration_id=0xA5, data=[count, 0x11, 0, 0, 0, 0, 0, 0], extended_id=False)
        bus.send(msgA5)
        count += 1
        if count == 255:
            count = 0
        msgA1 = can.Message(arbitration_id=0xA1, data=[0, 0, 0, 0, 100, 0, 0, 0], extended_id=False)
        bus.send(msgA1)
    if flag == 2:
        print("OK")
        break
    canmsg = bus.recv()
    if canmsg.arbitration_id == 0x10:
        mylist = list(format(canmsg.data[3],'08b'))
        if int(mylist[5]) == 1:
            flag = 1
        if int(mylist[0]) == 1:
            flag = 2

    time.sleep(0.002)

    while True:
        print(count)
        msgA5 = can.Message(arbitration_id=0xA5, data=[
            count, 0x11, 0, 0, 0, 0, 0, 0], extended_id=False)
        bus.send(msgA5)
        count += 1
        if count == 255:
            count = 0
        # 0~62
        # 127~65
        x = 40
        y = 0
        msgA1 = can.Message(arbitration_id=0xA1, data=[
            x, y, 0, 0, 100, 0, 0, 0], extended_id=False)
        bus.send(msgA1)
        time.sleep(0.2)

