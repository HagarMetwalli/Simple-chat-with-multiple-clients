import socket
import json


sok=socket.socket()
sok1=socket.socket()
IP = socket.gethostname()
port=8080
sok.connect((IP,port))
print("connected to chat ")
incoming_msg=sok.recv(1024)
incoming_msg=incoming_msg.decode()
incoming_msg=json.loads(incoming_msg)
In=incoming_msg.get("in")
IP=In[0]
flag=In[1]

if(flag=="begin"):

    sok1.bind((IP , port))
    sok1.listen(1)
    conn,address=sok1.accept()

    while 1:


        send_msg = input(str(">>"))
        send_msg=send_msg.encode()
        conn.send(send_msg)
        print("massage has been send")
        print("")
        incoming_msg=conn.recv(1024)
        incoming_msg=incoming_msg.decode()
        print("CLIENT2:",incoming_msg)
        print("")

elif(flag=="not_begin"):

    sok1.connect((IP ,port))
    while 1:

        incoming_msg=sok1.recv(1024)
        incoming_msg=incoming_msg.decode()
        print("CLIENT2:",incoming_msg)
        print("")
        send_msg = input(str(">>"))
        send_msg=send_msg.encode()
        sok1.send(send_msg)
        print("massage has been send")
        print("")

