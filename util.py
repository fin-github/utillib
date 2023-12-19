import subprocess
from os import system as cmd
from sys import argv as args
from time import sleep as wait

class Utilclass:
    def set_title(self, title:str):
        cmd(f"TITLE {title}")
    def clr(self):
        cmd("cls")
    def get_args(self):
        newargs = args
        newargs.pop(0)
        return newargs
    def get_raw_args(self):
        return args
    def wait(self, time:float):
        wait(time)
    def run_command(self, cmd:str):
        cmd(cmd)
    def run_powershell(self, cmd:str):
        res = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        return res.stdout
    def create_file(self, path:str):
        with open(path, "w") as file:
            file.write("")
    def read_file(self, path:str):
        with open(path,'r') as file:
            return file.read()
    def write_file(self, path:str, txt:str):
        with open(path, "w") as file:
            file.write(txt)
    def append_file(self, path:str, txt:str):
        with open(path, "a") as file:
            file.write(txt)
    def raw_append_file(self, path:str, txt:str):
        bfr = self.read_file()
        afr = bfr + txt
        self.write_file(path, afr)
