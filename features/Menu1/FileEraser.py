from config.settings import *

def EraseFile():
        os.system("cls")
        Slow(FileBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}File eraser{Style.RESET_ALL}")
        print("")
        Raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}File -> {Style.RESET_ALL}")

        FilePath = CleanPath(Raw)

        try:
            if not os.path.isfile(FilePath):
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} File not found :{Style.RESET_ALL} {FilePath}")
                time.sleep(2)
                return
            
            Size = os.path.getsize(FilePath)

            with open(FilePath, "r+b") as f:
                    for _ in range(3):
                        f.seek(0)
                        f.write(os.urandom(Size))
                        f.flush()
                        os.fsync(f.fileno())

            os.remove(FilePath)

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Erasing file... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} File erased :{Style.RESET_ALL} {FilePath}")
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

        except Exception as e:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} File could not be erased{Style.RESET_ALL}")
            time.sleep(2)
        