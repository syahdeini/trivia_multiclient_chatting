# trivia_multiclient_chatting

A trivia project. server-multiclient chatting application.

--------------------------------------------------------------------------------------
multi-client chatting system (socket)
client : parrarel process to read incoming packet and write to another client
-------------------------------------------------------------------------------------
Server
	-------------------
	|1. Server running|	    |
	-------------------
	     |	
	     | ------ [ 2. incoming connection from client ]
	     v
	3. server accepting connection -
        4. get client id and save socket object in dictionary 
	 	           saving socket object in list
	5. Creating a new thread 
	      |  |
	      |  |   
	      |  v
	      |	thread for each clients
	      |	------------------------------------
	      |	| 6. waiting for incoming packet from client
	      |	| 7. translate packet: message type [client ID] message
	      |	| 	1 sending to another client: 1 'client ID' message
	      |	| 	2 broadcast message: 2 message
	      |	----------------------------------------
	      v
	6. waiting for another client

------------------------------------------------------------------
Client
 	1. asking for ID
	2. connect to server
	3. sending client ID
	4. creating a new thread
	   |	|
	   |	|	
	   |	v
	   |	  5. waiting for server packet
	   |
           |
           V
	   5. asking for user input
	   6. sending to server	
