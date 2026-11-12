from features.Menu1.IpLookup import *
from features.Menu1.PhoneLookup import *
from features.Menu1.MetadataExtractor import *
from features.Menu1.OsintFramework import *
from features.Menu1.FileCorrupter import *
from features.Menu1.ImageCorrupter import *
from features.Menu1.FileEraser import *
from features.Menu1.AntiScreenCapture import *
from features.Menu1.PasswordGenerator import *
from features.Menu1.PasswordChecker import *
from features.Menu2.DiscordSelfbot import *
from features.Menu2.ServerCloner import *
from features.Menu2.StealerConfig import *

#Menu 2
def MainMenu2():
    while True:
        os.system("cls")
        Slow(Banner)
        print("")
        Slow(Menu2)
        
        Command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{Username}{Fore.GREEN})─[{Fore.WHITE}~/{System}/{PcName}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
        
        if Command == "11":
            RunMenu()
        elif Command == "12":
            CloneServer()
        elif Command == "13":
            ConfigStealer()
        elif Command == "+":
            Main()

#Menu 1
def Main():
    while True:
        os.system("cls")
        Slow(Banner)
        print("")
        Slow(Menu)
        
        Command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{Username}{Fore.GREEN})─[{Fore.WHITE}~/{System}/{PcName}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
                
        if Command == "1" or Command == "01":
            IPLookup()
        elif Command == "2" or Command == "02":
            LookupPhone()
        elif Command == "3" or Command == "03":
            ExtractMetadata()
        elif Command == "4" or Command == "04":
            OpenOsintFramwork()
        elif Command == "5" or Command == "05":
            CorruptFile()
        elif Command == "6" or Command == "06":
            CorruptImage()
        elif Command == "7" or Command == "07":
            EraseFile()
        elif Command == "8" or Command == "08":
            AntiCapture()
        elif Command == "9" or Command == "09":
            GeneratePassword()
        elif Command == "10":
            CheckPassword()
        elif Command == "+":
            MainMenu2()
Main()