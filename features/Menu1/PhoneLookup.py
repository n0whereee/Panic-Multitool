from config.settings import *

def LookupPhone():
        os.system("cls")
        Slow(OsintBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Phone number lookup{Style.RESET_ALL}")
        print("")
        Number = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Phone number (with country code) -> {Style.RESET_ALL}")

        try:
            PhoneNumber = phonenumbers.parse(Number)

            try:
                if number_type(PhoneNumber) == 0:
                    PhoneType = "Fixed Line"
                elif number_type(PhoneNumber) == 1:
                    PhoneType = "Mobile"
                elif number_type(PhoneNumber) == 2:
                    PhoneType = "Fixed Line or Mobile"
                elif number_type(PhoneNumber) == 3:
                    PhoneType = "Toll free"
                elif number_type(PhoneNumber) == 4:
                    PhoneType = "Premium Rate"
                elif number_type(PhoneNumber) == 5:
                    PhoneType = "Shared Cost"
                elif number_type(PhoneNumber) == 6:
                    PhoneType = "Voip"
                elif number_type(PhoneNumber) == 7:
                    PhoneType = "Personal Number"
                elif number_type(PhoneNumber) == 8:
                    PhoneType = "Pager"
                elif number_type(PhoneNumber) == 9:
                    PhoneType = "Universal Access Number"
                elif number_type(PhoneNumber) == 10:
                    PhoneType = "Voicemail"
                elif number_type(PhoneNumber) == -1:
                    PhoneType = "Unknown"

                ValidNumber = is_valid_number(PhoneNumber)
                InternationalNumber = format_number(PhoneNumber, PhoneNumberFormat.INTERNATIONAL)
                NationalNumber = format_number(PhoneNumber, PhoneNumberFormat.NATIONAL)

                TimeList = timezone.time_zones_for_number(PhoneNumber)
                Timezone = TimeList[0] if TimeList else "Unknown"

                Region = region_code_for_number(PhoneNumber)
                Location = geocoder.description_for_number(PhoneNumber, 'en')
                Provider = carrier.name_for_number(PhoneNumber, 'en')

                print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searchig for information... {Style.RESET_ALL}")
                print("")
                time.sleep(1.5)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Valid                : {Style.RESET_ALL}{ValidNumber}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} International number : {Style.RESET_ALL}{InternationalNumber}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} National number      : {Style.RESET_ALL}{NationalNumber}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Type                 : {Style.RESET_ALL}{PhoneType}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Timezone             : {Style.RESET_ALL}{Timezone}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Region               : {Style.RESET_ALL}{Region}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Location             : {Style.RESET_ALL}{Location}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Provider             : {Style.RESET_ALL}{Provider}")
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

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
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to grab information{Style.RESET_ALL}")
                time.sleep(2) 

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid phone number{Style.RESET_ALL}")
            time.sleep(2)
        
