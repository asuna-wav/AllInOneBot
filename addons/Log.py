from datetime import datetime
from colorama import Fore

class bstyle():
    G = Fore.LIGHTBLACK_EX
    O = Fore.LIGHTYELLOW_EX
    P = Fore.LIGHTMAGENTA_EX
    C = Fore.CYAN
    B = Fore.LIGHTBLUE_EX
    R = Fore.RESET

class Logger():
    def __init__(self):
        self.style = bstyle
    
    def log(self, text: str, module: str | None = "Info"):
        trenner = self.style.P + " ::  "
        trenner2 = self.style.C + " || "
        now = datetime.now()
        uhrzeit = now.strftime("%d/%m/%Y %H:%M:%S")

        print(self.style.G + uhrzeit + self.style.O + " BOT" + trenner + self.style.C + module + trenner2 + self.style.B + text + self.style.R)

        