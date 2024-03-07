from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

server = ModbusServer('localhost', 550, True)

try:
    print("Server starting...")
    server.start()
    print("Server online")
    state = [0]
    while True:
        server.data_bank.set_holding_registers(0, [int(uniform(0, 100))])
        print("the value of reg 0 is" +str(server.data_bank.get_holding_registers(0)))
        
        if state != server.data_bank.get_holding_registers(1, 1):
            state = server.data_bank.get_holding_registers(1, 1)
            print("value of reg 1 has changed to" +str(state))
        
        sleep(0.5)
except:
    print("Server shutdown...")
    server.stop()
    print("Server offline")
