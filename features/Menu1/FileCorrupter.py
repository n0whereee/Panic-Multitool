from config.settings import *

def CorruptFile():
        os.system("cls")
        Slow(FileBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}File corrupter{Style.RESET_ALL}")
        print("")
        Raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}File -> {Style.RESET_ALL}")

        FilePath = CleanPath(Raw)

        try:
            if not os.path.isfile(FilePath):
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} File not found :{Style.RESET_ALL} {FilePath}")
                time.sleep(2)
                return

            RandomBytes = os.urandom(1_000_000)

            with open(FilePath, "wb") as f:
                f.write(RandomBytes)

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Corrupting file... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} File corrupted :{Style.RESET_ALL} {FilePath}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} File could not be corrupted{Style.RESET_ALL}")
            time.sleep(2)
        