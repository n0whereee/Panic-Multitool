from config.settings import *

def IPLookup():
        os.system("cls")
        Slow(MapBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}IP lookup{Style.RESET_ALL}")
        print("")
        TargetIp = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Ip -> {Style.RESET_ALL}")

        try:
            Response = requests.get(f"http://ip-api.com/json/{TargetIp}")
            Api = Response.json()

            Status = "Valid" if Api.get('status') == "success" else "Invalid"
            Country = Api.get('country', "None")
            CountryCode = Api.get('countryCode', "None")
            Region = Api.get('regionName', "None")
            ZipCode = Api.get('zip', "None")
            City = Api.get('city', "None")
            Latitude = Api.get('lat', "None")
            Longitude = Api.get('lon', "None")
            Timezone = Api.get('timezone', "None")
            Isp = Api.get('isp', "None")
            Org = Api.get('org', "None")
            AsHost = Api.get('as', "None")
            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searching for information... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Status       :{Style.RESET_ALL} {Status}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Country      :{Style.RESET_ALL} {Country}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Country code :{Style.RESET_ALL} {CountryCode}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Region       :{Style.RESET_ALL} {Region}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Zip          :{Style.RESET_ALL} {ZipCode}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} City         :{Style.RESET_ALL} {City}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Latitude     :{Style.RESET_ALL} {Latitude}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Longitude    :{Style.RESET_ALL} {Longitude}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Timezone     :{Style.RESET_ALL} {Timezone}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Isp          :{Style.RESET_ALL} {Isp}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Org          :{Style.RESET_ALL} {Org}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} As host      :{Style.RESET_ALL} {AsHost}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} IP unavailable{Style.RESET_ALL}")
            time.sleep(2)
        
