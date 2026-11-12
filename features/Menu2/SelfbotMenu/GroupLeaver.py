from config.settings import *

async def LeaveAllGroups(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Group selfbot{Style.RESET_ALL}")
    time.sleep(0.05)

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseUrl}/users/@me/channels", headers=HEADERS
        )

        if res.status_code in SuccesStatus:
            Channels = res.json()

            Groups = [c for c in Channels if c.get("type") == 3]

            if not Groups:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No groups found{Style.RESET_ALL}")
                time.sleep(2)
                return

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Leaving all groups... {Style.RESET_ALL}")
            time.sleep(1.5)
            try:
                print("")
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

                for channel in Channels:
                    if channel.get("type") != 3:
                        continue

                    Recipients = channel.get("recipients") or []

                    if Recipients:
                        Names = [u.get("username", "Unknown") for u in Recipients]
                        GroupName = ", ".join(Names)
                    else:
                        GroupName = "Unknown Group"

                    DmId = channel["id"]
                    try:
                        DeleteRes = await client.delete(
                                f"{BaseUrl}/channels/{DmId}",
                                headers=HEADERS)
                        
                        if DeleteRes.status_code in SuccesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Left group            : {Style.RESET_ALL}{GroupName} - {DmId}")
                        elif DeleteRes.status_code == 429:
                            Retry = DeleteRes.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave group : {Style.RESET_ALL}{GroupName} - {DmId}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave group : {Style.RESET_ALL}{GroupName} - {DmId}")
    
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Groups unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to leave all groups{Style.RESET_ALL}")
            time.sleep(2)
            return
        
        print("")
        print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Selfbot menu{Style.RESET_ALL}")
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