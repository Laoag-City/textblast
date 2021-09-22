import serial, serial.tools.list_ports

comports = [comport.device for comport in serial.tools.list_ports.comports()]
cominfo =serial.tools.list_ports.comports()
# modem = serial.Serial(baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1, xonoff=False, rtscts=False, dsrdtr=False)

for i in range(len(comports)):
    # print(cominfo[i].name)
    print(cominfo[i].description)
    print(cominfo[i].hwid)
    print(cominfo[i].vid)
    print(cominfo[i].pid)
    print(cominfo[i].serial_number)
    print(cominfo[i].location)
    print(cominfo[i].manufacturer)
    print(cominfo[i].product)
    print(cominfo[i].interface)

    # print(i)
    # modem.port='i'
    # modem.open()
    # cmd="AT\r"
    # modem.write(cmd.encode())
    # msg=modem.read(64)
    # print(msg)
    # modem.close()
