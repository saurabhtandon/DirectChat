#!/usr/bin/local/python
import thread, time, socket, sys

connections = {}
BUFFER_SIZE = 4096
CONNECTION_CMD = "connectme"	#connectme abc host port
EXIT_CMD = "exit"

def connectToSend(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.recv()
	return s

def connectToReceive(username):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostname(), 0))
	print "Receiver connected", s.getsockname()
	s.listen(5)
	connections[username] = s
	return s

def addConnections(message):
	messageArray = message.split(' ')
	s = connectToSend(messageArray[2], int (messageArray[3]))
	connections[messageArray[1]] = s
	return

def exitSystem():
	for con in connections:
		connections[con].close()
	return

def send():
	while True:
		message = raw_input()
		print message
		if message.find(CONNECTION_CMD) != -1:
			addConnections(message)			
		elif message == EXIT_CMD:
			exitSystem()
			break;
		else:
			name = s.split(':')[0]
			connections[name].send(message)
	return

def receive(c):
	message = c.recv(BUFFER_SIZE)
	user = message.split(':')[0]
	if user not in connections:
		connections[user] = c
	else:
		print c.recv(BUFFER_SIZE)
	return

def receiver(s):
	while True:
		c, addr = s.accept()
		print "connection received", c, addr
	return

def main():
	s = connectToReceive(sys.argv[1])
	thread.start_new_thread(send, ())
	receiver(s)
	return

if __name__ == '__main__':
	main()

'''
def server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostname(), 0))
	print s.getsockname()
	s.listen(1)
	while True:
		c, addr = s.accept()
		print c.recv(1024)
		message = raw_input()
		if message == 'exit':
			c.close()
			s.close()
			break
		#c.send(message)
	return

def client():
	#print "client", s.getsockname()
	message = raw_input()
	if message == 'exit':
		s.close()
	s.send(message)
	s.close()
	return
'''