from config.settings import *
from features.Menu2.SelfbotMenu.Unfriender import UnfriendEveryone
from features.Menu2.SelfbotMenu.Messager import MessageEveryone
from features.Menu2.SelfbotMenu.DmCloser import CloseAllDms
from features.Menu2.SelfbotMenu.ServerLeaver import LeaveAllServers
from features.Menu2.SelfbotMenu.GroupLeaver import LeaveAllGroups
            
def MainSelfbot(Token):
    while True:
        os.system("cls")
        Slow(SelfbotBanner)
        Slow(SelfbotMenu)
        print("")

        Command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{Username}{Fore.GREEN})─[{Fore.WHITE}~/{System}/{PcName}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
        
        if Command == "1" or Command == "01":
            asyncio.run(UnfriendEveryone(HEADERS={"Authorization": Token}))
        elif Command == "2" or Command == "02":
            asyncio.run(MessageEveryone(HEADERS={"Authorization": Token}))
        elif Command == "3" or Command == "03":
            asyncio.run(CloseAllDms(HEADERS={"Authorization": Token}))
        elif Command == "4" or Command == "04":
            asyncio.run(LeaveAllGroups(HEADERS={"Authorization": Token}))
        elif Command == "5" or Command == "05":
            asyncio.run(LeaveAllServers(HEADERS={"Authorization": Token}))
        elif Command == "6" or Command == "06":
            asyncio.run(MessageEveryone(HEADERS={"Authorization": Token}))
            time.sleep(0.2)
            asyncio.run(UnfriendEveryone(HEADERS={"Authorization": Token}))
            time.sleep(0.2)
            asyncio.run(CloseAllDms(HEADERS={"Authorization": Token}))
            time.sleep(0.2)
            asyncio.run(LeaveAllGroups(HEADERS={"Authorization": Token}))
            time.sleep(0.2)
            asyncio.run(LeaveAllServers(HEADERS={"Authorization": Token}))
        elif Command == "7" or Command == "07":
            break

def RunMenu():
        os.system("cls")
        Slow(SelfbotBanner)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        time.sleep(0.05)
        print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2} {Fore.GREEN}Your token :{Style.RESET_ALL} {MyToken()}")
        time.sleep(0.05)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print("")
        RawToken = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Token -> {Style.RESET_ALL}")

        try:
            headers = {
                "Authorization": RawToken
            }

            r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)

            if r.status_code in SuccesStatus:
                Token = RawToken
            else:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid token{Style.RESET_ALL}")
                time.sleep(2)
                return

            MainSelfbot(Token=Token)
        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Error running selfbot{Style.RESET_ALL}")
            time.sleep(2)