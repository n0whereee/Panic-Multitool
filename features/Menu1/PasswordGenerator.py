from config.settings import *

def GeneratePassword():
        os.system("cls")
        Slow(PasswordBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Password generator{Style.RESET_ALL}")
        print("")

        try:
            Length = int(input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Number of characters -> {Style.RESET_ALL}"))
        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid number{Style.RESET_ALL}")
            time.sleep(2)
            return

        try:
            Uppercase = string.ascii_uppercase
            Lowercase = string.ascii_lowercase
            Numbers = string.digits
            SpecialCharacters = "!#$%&'()*+,-.:<=>?@\_|"

            AllCharacters = Uppercase + Lowercase + Numbers + SpecialCharacters

            Password = "".join(random.choice(AllCharacters) for _ in range(Length))

            if Length > 100:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{bracketclosed} {Fore.GREEN}Maximum 100 characters{Style.RESET_ALL}")
                time.sleep(2)
                return
            elif Length < 1:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{bracketclosed} {Fore.GREEN}Minimum 1 character{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Generating password... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Password :{Style.RESET_ALL} {Password}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to generate password{Style.RESET_ALL}")
            time.sleep(2)
        