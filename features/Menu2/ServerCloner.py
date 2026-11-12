from config.settings import *
from features.Menu2.CloneFunctions.RoleCloner import *
from features.Menu2.CloneFunctions.ChannelCloner import *
from features.Menu2.CloneFunctions.NameEditor import *

def CloneServer():
        os.system("cls")
        Slow(DiscordBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Server cloner{Style.RESET_ALL}")
        print("")
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

            TargetID = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}ID to clone server -> {Style.RESET_ALL}")
            CloneID = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}ID to apply clone -> {Style.RESET_ALL}")
            
            headers = {
                "Authorization": Token,
                "Content-Type": "application/json"
            }
            
            TargetRes  = requests.get(f"{BaseUrl}/guilds/{TargetID}", headers=headers)
            CloneRes  = requests.get(f"{BaseUrl}/guilds/{CloneID}", headers=headers)

            if TargetRes.status_code not in SuccesStatus:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid clone ID{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            if CloneRes.status_code not in SuccesStatus:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid apply ID{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            if TargetID == CloneID:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Apply and target ID cant be the same{Style.RESET_ALL}")
                time.sleep(2)
                return

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Cloning server... {Style.RESET_ALL}")
            time.sleep(1.5)

            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            EditName(TargetID, CloneID, headers)
            CurrentRoleMap = asyncio.run(CloneRoles(TargetID, CloneID, headers))
            asyncio.run(CloneChannels(TargetID, CloneID, headers, CurrentRoleMap))
            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            print("")
            print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Main Menu{Style.RESET_ALL}")
            print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Exit{Style.RESET_ALL}")
            print("")

            Command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{Username}{Fore.GREEN})─[{Fore.WHITE}~/{System}/{PcName}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")

            if Command == "1" or Command == "01":
                pass
            elif Command == "2" or Command == "02":
                sys.exit()
            else:
                pass

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Error while cloning server{Style.RESET_ALL}")
            time.sleep(2)