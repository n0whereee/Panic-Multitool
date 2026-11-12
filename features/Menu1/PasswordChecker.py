from config.settings import *

def CheckPassword():
        os.system("cls")
        Slow(PasswordBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Password checker{Style.RESET_ALL}")
        print("")
        Password = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Password -> {Style.RESET_ALL}")

        try:
            CharSize = 0
            if any(c.islower() for c in Password):
                CharSize += 26
            if any(c.isupper() for c in Password):
                CharSize += 26
            if any(c.isdigit() for c in Password):
                CharSize += 10
            if any(c in string.punctuation for c in Password):
                CharSize += len(string.punctuation)
            if CharSize == 0:
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid password{Style.RESET_ALL}")

            Combinations = int(CharSize ** len(Password))
            GuessesPerSec = int(10000)
            Seconds = Combinations / GuessesPerSec
            
            if Seconds < 60:
                TimeEstimate = f"{Seconds:.2f} Seconds to bruteforce"
            elif Seconds < 3600:
                TimeEstimate = f"{Seconds/60:.2f} Minutes to bruteforce"
            elif Seconds < 86400:
                TimeEstimate = f"{Seconds/3600:.2f} Hours to bruteforce"
            elif Seconds < 31536000:
                TimeEstimate = f"{Seconds/86400:.2f} Days to bruteforce"
            else:
                TimeEstimate = f"{Seconds/31536000:.2f} Years to bruteforce"

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Checking password... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Time to bruetforce :{Style.RESET_ALL} {TimeEstimate}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to check password{Style.RESET_ALL}")
            time.sleep(2)
        