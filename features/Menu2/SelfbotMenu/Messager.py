from config.settings import *

async def MessageEveryone(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Message selfbot{Style.RESET_ALL}")
    print("")
    time.sleep(0.05)
    Message = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Message content -> {Style.RESET_ALL}")

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseUrl}/users/@me/channels", headers=HEADERS
        )

        if res.status_code in SuccesStatus:
            Channels = res.json()

            if not Channels:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No open dms found{Style.RESET_ALL}")
                time.sleep(2)
                return

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Messaging everyone... {Style.RESET_ALL}")
            time.sleep(1.5)

            try:
                print("")
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

                for channel in Channels:
                    Recipients = channel.get("recipients", [])

                    if Recipients:
                        DmUser = Recipients[0].get("username", "Unknown")
                    else:
                        DmUser = "Unknown"

                    DmId = channel["id"]
                    try:
                        PostRes = await client.post(
                            f"{BaseUrl}/channels/{DmId}/messages",
                            headers=HEADERS,
                            json={"content": Message}
                        )

                        if PostRes.status_code in SuccesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Messaged          : {Style.RESET_ALL}{DmUser}")
                        elif PostRes.status_code == 429:
                            Retry = PostRes.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to message : {Style.RESET_ALL}{DmUser}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to message : {Style.RESET_ALL}{DmUser}")
    
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Dms unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to message everyone{Style.RESET_ALL}")
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