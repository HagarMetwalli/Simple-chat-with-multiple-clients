import socket
import json
sok= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostname()
print("server will start on IP : ",IP)
port=8080
sok.bind((IP,port))
print("server done binding to IP and port sucessfully")
sok.listen(1)
print ("waiting for two connection from 2_clients to server")
conn,address_1 = sok.accept()
print ("client_1 has connected")
print ("waiting for second connection from client_2 to server")
conn_1,address_2 = sok.accept()
print("client_2 has connected")


if (conn and address_1 ):
    send_arr=[str(IP),"begin"]
    data=json.dumps({"in":send_arr})
    conn.send(data.encode())
    send_arr=[str(IP),"not_begin"]
    data=json.dumps({"in":send_arr})
    conn_1.send(data.encode())

elif (conn and address_2 ):
    send_arr=[str(IP),"begin"]
    data=json.dumps({"in":send_arr})
    conn_1.send(data.encode())
    send_arr2=[str(IP),"not_begin"]
    data=json.dumps({"in":send_arr})
    conn.send(data.encode())

sok.close()
