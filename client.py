import socket
from threading import Thread
from tkinter import *

ip_address='127.0.0.1'
port=8002

# nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip_address,socket))

print('Server connection Successful')

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("login")

        self.go = Button(self.login,
                 text = "CONTINUE",
                 font = "Helvetica 14 bold",
                 command = lambda: self.goAhead(self.entryName.get()))

def goAhead(self, name):
    self.login.destroy()
    # self.name = name
    self.layout(name)
    rcv = Thread(target = self.receive)
    rcv.start()

def layout(self, name):
    self.name = name
    self.window.deconify()
    self.window.title('CHATROOM')
    self.window.resizeable(witdh = False, height = False)
    self.window.configure(width = 470, height = 550, bg = "#1702A")

def sendButton(self,msg):
    self.textCons.config(state = DISABLED)
    self.msg=msg
    self.entryMsg.delete(0, END)
    snd = Thread(target = self.write)
    snd.start()

def show_message(self,message):
    self.textCons.config(state = NORMAL)
    self.textCons.insert(END, message+"\n\n")
    self.textCons.config(state = DISABLED)
    self.textCons.see(END)

def write(self):
    self.textCons.config(state = DISABLED)
    while True:
        message = (f"{self.name}: {self.msg}")
        client.send(message.encode('utf-8'))
        self.show_message(message)






def recieve(self):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(self.name.encode('utf-8'))
            else:
                self.show_message(message)
        except:
            print("An error occured!")
            client.close()
            break

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()