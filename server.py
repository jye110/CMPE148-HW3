from socket import *
import ssl,base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 465)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
 
username="yezhongling1@gmail.com"
password="rebornreborn"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
mailFrom="MAIL FROM:<yezhongling1@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv=clientSocket.recv(1024).decode()
print(recv)

# Send RCPT TO command and print server response.
rcptTo="RCPT TO:<zhongling.ye@sjsu.edu>\r\n"
clientSocket.send(rcptTo.encode())        
recv=clientSocket.recv(1024).decode()
print(recv)

# Send DATA command and print server response.
clientSocket.send("DATA\r\n".encode())  
recv=clientSocket.recv(1024).decode()
print(recv)

# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n" 
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())  
# Message ends with a single period.
clientSocket.send(endmsg.encode())  
recv=clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())        
recv=clientSocket.recv(1024).decode()
print(recv)
clientSocket.close()