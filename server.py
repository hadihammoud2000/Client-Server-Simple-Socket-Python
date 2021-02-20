import time
import socket
import datetime
#NOTES:

#WE USE THE ENCODE DECODE PAIR TO GET PROPER UTF-8 STATEMENTS TO PRINT ON CONSOLE

#SOURCES USED:
#GEEKSFORGEEKS
#KITE
#PROGRAMIZ
#GITHUB

#USAGE OF DATETIME AND TIME MODULES AT THE SAME TIME MAY CAUSE INCONSISTENCIES WITH VALUES, BUT THEY COULD BE IGNORED
#SINCE THEY ARE AT A VERY SMALL SCALE
#WHAT MATTERS IS THE FOLLOWING:
#STARTTIME (CLIENT'S CODE) < DATETIME (SERVER CODE) < ENDTIME (CLIENT CODE IMMEDIATELY USED IN RTT ESTIMATION)




#getting the local host from the computer (source: kite.com)
hostname = socket.gethostname()

#creating a server socket using UDP (source: geeksforgeeks)
Mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = socket.gethostbyname(hostname)
port = 20001
receive_buffer_size = 1024


#binding the socket with the IP and the port using .bind() method
Mysocket.bind((IP, port))

print("server listening on address: ", IP, " and port: ",port)


while True:
    #receiving message and address from the client using the .recv() method in a list of two elements
    MessageAndAddress = Mysocket.recvfrom(receive_buffer_size)
    Message = MessageAndAddress[0]
    Address = MessageAndAddress[1]

    #printing the date and time of receiving using the datetime module (source: geeksforgeeks)
    print('Echo message ', Message.decode(), ' received at:', datetime.datetime.now(),' and being looped back')


    #sending the echo message back to client to complete the UDP echo client server process according to protocol
    sending = Mysocket.sendto(Message, Address)

