from socket import *
from time import *
from random import *
import ast



seed_timing = int(input("seed_for_random_number_generator_for_timing = "))
number_of_packets = int(input("number_of_packets= "))
seed_ACK_NACK = int(input("The seed for the random number generator used for determining if ACKs or NACKs= "))
probability = float(input("The probability that an ACK or NACK has been corrupted. Between [0 and 1) = "))

#PACKET_CREATOR
def make_packet(seq):
	data = randint(0, 4294967296)
	ACK = 0
	NACK = 0
	packet = [data, seq, ACK, NACK]
	return packet

#RANDOM_NUMBER_GENERATOR
def Random_number_generator(x,y):
	seed(y)
	random_number = random() * x
	return random_number



#SOCKET CREATED
serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_DGRAM)




seq = 0;
i = 1;

#MAIN PROCESS OF SENDING THE PACKETS
while i <= number_of_packets:
	packet = make_packet(seq)

	current_time = time()
	expected_arrival_time = current_time

	



	print('\nA packet with sequence number  ' + str(seq) + '  about to be sent')
	print('Packet to send contains:  data = ' +  str(packet[0]) + ' seq = ' +  str(packet[1]) + ' ack = ' + str(packet[2]) +' nack = ' + str(packet[3]))



	clientSocket.sendto( str(packet).encode(), (serverName, serverPort))
	random_time_in_seconds = int(round(Random_number_generator(5, seed_timing)))
	expected_arrival_time = expected_arrival_time + random_time_in_seconds 
	

	check = time()
	if check < expected_arrival_time:
		delay = expected_arrival_time - check
		sleep(delay)
	

	print ('message sent')
	print('\nThe sender is moving to state WAIT FOR ACK OR NACK \n')
	modifiedMessage, severAddress = clientSocket.recvfrom(2048)
	packet_received = ast.literal_eval(modifiedMessage.decode())
	

	random_number_for_ACK_NACK = Random_number_generator(1, seed_ACK_NACK)

	if random_number_for_ACK_NACK < probability:
		print('A Corrupted ACK or NACK packet has just been received ')
		print('\nThe sender is moving back to state WAIT FOR ACK OR NACK\n')
		
		if seq == 0:
			print('\nThe sender is moving back to state WAIT FOR CALL 0 FROM ABOVE \n')
		else:
			print('\nThe sender is moving back to state WAIT FOR CALL 1 FROM ABOVE\n')


	else:

		

		if packet_received[2] == 1:
			print('An ACK packet has just been received')
		else:
			print('A NACK packet has just been received')
			
		print('Packet received contains: data = ' + str(packet_received[0]) + ' seq = '  + str(packet_received[1]) + ' ack = ' + str(packet_received[2]) +' nack = ' +  str(packet_received[3]) + '\n')


	if seq == 0:
		print('\nThe sender is moving to state WAIT FOR CALL 1 FROM ABOVE \n')
	else:
		print('\nThe sender is moving to state WAIT FOR CALL 0 FROM ABOVE \n')

	seq = 1 - seq;
	i += 1





#SOCKET CLOSED
clientSocket.close()






