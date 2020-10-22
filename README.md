# Server_Client
Python socket programs to exchange packets using UDP protocol. Packet containsfour values:

• Field 1:  Packet contents: a 32 bit integer.  The integer cannot be assumed to follow any patternPacket contents for an ACK or NACK packets is 0  

• Field 2:  Sequence Number: a Boolean Value is True if sequence number is 1  Value is False if sequence number is 0 

• Field 3: Is this an ACK?   Boolean True if the packet is an ACK, False if the packet is not an ACK

• Field 4: Is this a NACK?  Boolean True if the packet is a NACK, False if the packet is not a NACK  For ACK and NACK packets the values in Field1 should be 0 


Requirements:
You will write two Python (compatible with v3.5) socket programs to implement a slightly modified version of the protocol illustrated in figures 3.11 and 3.12 (rdt2.1) in your text.  These two processes will exchange simple packets that are used to implement the protocol.  Please note that the form of the packets has been changed from the example in your textbook.  This means that the arguments of the makepkt function in the figures must be  changed  to  a  list  of  the  variables  in  the  fields  of  the  packets  described  below.  The arguments of makepkt should be in the order Field1, Field2, Field3, Field4.  

