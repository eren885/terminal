import platform
import subprocess
import sys
import asyncio
import websockets
import random
import socket
import json
import time
import os

system = platform.platform()
release = platform.release()
version = platform.version()

def systemcheck():
    if 'system' == cmd:
        system()

def system():
    print (platform.machine())
    print (platform.platform())

def fullosnamecheck():
    if 'fullosname' == cmd:
        fullosname()

def fullosname():
    print (platform.uname())

def exits():
    exit()

def exitcheck():
    if 'exit' == cmd:
        exits()

def textcheck():
    if 'text' == cmd:
        textc()

def pythonversion():
    print (platform.python_version())

def textc():
    print ('write text that you want as file name')
    texti = input()
    my_file = open(texti,"w+")
    print ("write the thing that you want to write")
    texts = input()
    my_file = open(texti,"w+")
    my_file.write(texts)
    print ("done")

def help():
    print ('commands:')
    time.sleep(0.4)
    print ('fullosname')
    time.sleep(0.4)
    print ('exit')
    time.sleep(0.4)
    print ('system')
    time.sleep(0.4)
    print ('help')
    time.sleep(0.4)
    print ('text')
    time.sleep(0.4)
    print ('pythonver')
    time.sleep(0.4)
    print ('execute')
    time.sleep(0.4)
    print ('evalpy')
    print ('   ')

def executes():
    print ("input the command that you want to execute")
    command = input()
    os.system(command)
    print ('command executed')

def executescheck():
    if 'execute' == cmd:
        executes()
def pythonversioncheck():
    if 'pythonver' == cmd:
        pythonversion()
def win_edition():
    print(platform.win32_edition())

def helpcheck():
    if 'help' == cmd:
        help()

def win32_editioncheck():
    if 'winedition' == cmd:
        if 'Windows' == platform.system():
            win_edition()
        else:
            print("ERROR this isnt windows os")

def creditcheck():
    if 'credits' == cmd:
        creditst()

def creditst():
    print("credits:")
    time.sleep(0.5)
    print ("takipsizad 2020")
    
def evscheck():
    if 'evalpy' == cmd:
        evals()

def evals():
    print('write the thing that you want to execute as python code')
    evalcmd = input()
    print(eval(evalcmd))

def ipcheck():
    if 'ip' == cmd:
        ipprint()

def ipprint():
    os.system('ipconfig')

def pipinstall():
    print ('write the packet that you want to install into python')
    p = input()
    os.system('pip install' ,p)

def pipinstallcheck():
    if 'pipinstall' == cmd:
        pipinstall()

while True:
    cmd = input()
    systemcheck()
    fullosnamecheck()
    exitcheck()
    textcheck()
    helpcheck()
    pythonversioncheck()
    executescheck()
    win32_editioncheck()
    creditcheck()
    evscheck()
    ipcheck()
    pipinstallcheck()