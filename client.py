import socket
import time
import datetime


"""
IP = '127.0.0.1'
port = 20001
Echo = "This is an ECHO message"
"""

receive_buffer_size = 1024
#IP port and echo message input
IP = input("enter IP: ")
port = int(input("enter Port: "))
Echo = input("enter echo message: ")


#list containing the RTT of the messages, used to compute statistics
avgRTT=[]

#connecting to client socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#for loop to send 5 requests
for i in range(5):
    
    
    #computing time before sending the message to server
    startTime = time.time()


    #sending the message using method sendto()
    sending = ClientSocket.sendto(Echo.encode('utf-8'),(IP,port))


    #receiving the message back from server (following echo protocol)
    MessageAndAddress = ClientSocket.recvfrom(receive_buffer_size)
    Message = MessageAndAddress[0]


    #substracting current time(now) from startTime to get RTT (round trip)
    RTT = time.time()-startTime


    #converting to microseconds (easier on the eyes) and rounding it to up to 4 digits
    RTT = round(RTT*(10**6),4)


    avgRTT.append(RTT)
    print(Message.decode())
    print("RTT of Echo Message ",i+1, " : ", RTT, "microseconds")



#displaying the average RTT of the 5 messages
MeanRTT = round(sum(avgRTT)/len(avgRTT),4)
print("average RTT of the 5 Echo messages sent: ", MeanRTT, " microseconds")





