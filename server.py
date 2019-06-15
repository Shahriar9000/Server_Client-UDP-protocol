import sys
import ast
from socket import *
from time import *
from random import *
import ast


print (sys.version)




seed_ACK_NACK_r = int(input("The seed for the random number generator used for determining if ACKs or NACKs is corrupted= "))
probability_r = float(input("The probability that an ACK or NACK has been corrupted. Between [0 and 1) = "))

def Random_number_generator(x):
    seed(seed_ACK_NACK_r)
    random_number = random() * x
    return random_number


def make_packet(seq, x):
    data = 0

    if x == 0:
        ACK = 0
        NACK = 1
    else:
        ACK = 1
        NACK = 0

    packet = [data, seq, ACK, NACK]
    return packet


serverHost = "127.0.0.1"
serverPort = 50007
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(( serverHost, serverPort))
print ( 'The server is ready to receive ' )





while True:
        sentence, clientAddress = serverSocket.recvfrom(1024)
        print("Message received: ",sentence ) 
        s= sentence.decode()
        packet_received = ast.literal_eval(s)
        seq = packet_received[1]



        random_number_for_ACK_NACK = Random_number_generator(1) 
        if random_number_for_ACK_NACK < probability_r:
            print ("A Corrupted packet has just been received\n")
            print("A NACK is about to be sent")
            print("Packet to send contains: data = 0 seq = " + str(seq) + " ack = 0 nack = 1")
            C =0

            print("The receiver is moving back to state WAIT FOR 1 FROM BELOW ")


            

        else:
            print ("A packet with sequence number " + str(packet_received[1]) + " has been received \n ")
            print ("Packet received contains: data = " + str(packet_received[0]) +" seq = " + str(packet_received[1]) + " ack = " + str(packet_received[2]) + "nack = " + str(packet_received[3]) + "\n")
            print("An ACK is about to be sent")
            print("Packet to send contains: data = 0 seq = " + seq + " ack = 1 nack = 0")
            C = 1
            if seq == 0:
                print("The receiver is moving back to state WAIT FOR 1 FROM BELOW ")

            if seq == 1:
                print("The receiver is moving back to state WAIT FOR 0 FROM BELOW ")
                



        response_packet = make_packet(seq, C)
        serverSocket.sendto(str(response_packet).encode(), clientAddress)

        if (C == 1) and (packet_received[1] == 0):
              print("The receiver is moving to state WAIT FOR 1 FROM BELOW ")

        if (C == 1) and (packet_received[1] == 1):
             print("The receiver is moving to state WAIT FOR 0 FROM BELOW ")

        
        
        
       


        

        



            


    