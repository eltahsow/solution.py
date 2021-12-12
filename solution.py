from socket import *
import ssl
import base64



def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message is to say hello"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    #recv = clientSocket.recv(1024).decode()
    #print(recv)
    # if recv[:3] != '220':
      #  print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    
    email = "es5754@nyu.edu \r\n"     #my nyu email addr
    
    # Send MAIL FROM command and print server response.
    mailFROM = "Mail From: "+ email
    clientSocket.send(mailFROM.encode())
    recv2 = clientSocket.recv(1024).decode()
 #   print(recv2)
 #   if recv2[:3] != '250':
 #      print('250 reply not recived from the server')
  

    # Send RCPT TO command and print server response.
    rcptTO = "RCPT TO: " + email
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
   # print(recv3)
   # if recv3[:3] != '250':
   #     print('250 reply not received from server')

    # Send DATA command and print server response.

    dataCOMMAND = 'DATA\r\n'
    clientSocket.send(dataCOMMAND.encode())
    recv4 = clientSocket.recv(1024).decode()
   # print(recv4)
   # if recv4[:3] != '250':
   #     print('250 reply not recived from the server')

    # Send message data.
   # messageDATA = "Message: Hi  \r\n\r\n"
   # clientSocket.send(messageDATA.encode())
    clientSocket.send(msg.encode())
   # clientSocket.send(endmsg.encode())
   # recv5 = clientSocket.recv(1024).decode()
   # print(recv5)
   # if recv5[:3] != '250':
   #     print('250 reply not recived from the server')
    


    # Message ends with a single period.
    # Fill in start
  #  messageDATA2 = "."
  #  clientSocket.send(messageDATA2.encode())
  #  clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
   # print(recv6)
    #if recv6[:3] != '250':
     #   print('250 reply not recived from the server')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
  #  print(recv7)
  #  if recv7[:3] != '221':
  #      print('221 reply not recived from the server')
    # Fill in end
   # clientSocket.close()
    
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
