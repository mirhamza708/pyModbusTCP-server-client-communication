from pyModbusTCP.client import ModbusClient
from time import sleep
# import threading
client = ModbusClient('localhost', 550)


# def server_monitor():
#     while True:
#         # Check if server has responded
#         if not client.is_open:
#             print("Server not responding. Client closed.")
#             client.close()
#             break

# # Start the server monitor thread
# monitor_thread = threading.Thread(target=server_monitor)
# monitor_thread.daemon = True  # Daemonize the thread so it terminates when the main thread terminates
# monitor_thread.start()

try:
    client_state = client.open()
    data = [0]
    if client_state == True:
        print("Client online")
        while True:
            if not client.is_open:
                print("Server not responding. Client shutdown.")
                client.close()
                break

            if data != client.read_holding_registers(0):
                data =  client.read_holding_registers(0)
                print("The value in reg 0 of server is" +str(client.read_holding_registers(0)))
            # sleep(0.5)    
    else:
        print("Client can't connect to server")
except:
    print("client shutown")
