import subprocess, sys, os
from queue import Queue, Empty
#from threading import Thread, Event
import multiprocessing
import ctypes



class Command:
    def __init__(self, Name: str, Description: str, Callback):
        self.Name = Name
        self.Description = Description
        self.Callback = Callback

    def Run(self, Text: str):
        if Text.__contains__(self.Name):
            self.Callback()
        

class Console:
    def __init__(self, Server):
        self.Server = Server
        self.Active = False
        self.Commands = [
            Command("help", "shows command list", self.ShowHelp),
            Command("close", "close console", self.Close),
        ]
        self.Output = []

        self.ServerThread: multiprocessing.Process = None
        self.OutputThread: multiprocessing.Process = None

    def ShowHelp(self):
        print("Command List:")
        for command in self.Commands:
            print(f"{command.Name}: {command.Description}")

    def Send(self, Text: str):
        Ran = False
        for command in self.Commands:
            command.Run(Text)
            Ran = True

        if not Ran:
            self.Server.Process.stdin.write(Text + "\n")
            self.Server.Process.stdin.flush()
    
    def Close(self):
        #self.OutThread.join()
        self.Active = False
        print("Joining threads")
        self.OutputThread.terminate()
        self.ServerThread.terminate()
        print("Closed")


    def Open(self):
        self.Active = True

        self.Wrapper()
        '''
        self.Output = []

        def Out():
            while self.Active:
                Output = self.Server.Process.stdout.readline()
                if Output == '' and self.Server.Process.poll() is not None:
                    break
                if Output:
                    print(Output.strip(), flush=True)
                    self.Output.append(Output.strip())

        OutThread = Thread(target=Out)
        OutThread.start()
        '''

    def Wrapper(self):
        Process: subprocess.Popen = self.Server.Process

        def read_lines(stream, queue: Queue):
            while self.Active:
                queue.put(stream.readline())


        # terminal reading thread
        q = Queue()
        self.OutputThread = multiprocessing.Process(target=read_lines, args=(sys.stdin, q))
        self.OutputThread.daemon = True
        self.OutputThread.start()

        # server reading thread
        qs = Queue()
        self.ServerThread = multiprocessing.Process(target=read_lines, args=(Process.stdout, qs))
        self.ServerThread.daemon = True
        self.ServerThread.start()
        

        while Process.poll() == None and self.Active == True: # loop while the server process is running

            # get a user entered line and send it to the server
            try:
                line = q.get_nowait()
            except Empty:
                pass
            else:
                line = self.Send(line) # do something with the user entered line
                if line != None:
                    try:
                        Process.stdin.write('{}\n'.format(line).encode('utf-8'))
                
                    except TypeError: 
                        Process.stdin.write(line)
                    Process.stdin.flush()
            # just pass-through data from the server to the terminal output
            try:
                line = qs.get_nowait()
            except Empty:
                pass
            else:
                print(line.strip("\n"))
                sys.stdout.flush()
    
        