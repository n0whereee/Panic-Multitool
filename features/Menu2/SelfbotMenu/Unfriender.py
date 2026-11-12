from config.settings import *

async def UnfriendEveryone(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Unfriend selfbot{Style.RESET_ALL}")
    time.sleep(0.05)

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseUrl}/users/@me/relationships", headers=HEADERS
        )

        if res.status_code in SuccesStatus:
            Friends = res.json()

            if not Friends:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No friends found{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Unfriending everyone... {Style.RESET_ALL}")
            time.sleep(1.5)
        
            try:
                print("")
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

                for friend in Friends:
                    User = friend.get("user", {})
                    if User:
                        FriendUser = User.get("username", "Unknown")
                    else:
                        FriendUser = "Unknown"

                    FriendId = friend["id"]
                    try:
                        DeleteRes = await client.delete(
                                f"{BaseUrl}/users/@me/relationships/{FriendId}",
                                headers=HEADERS)
                        
                        if DeleteRes.status_code in SuccesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Unfriended         : {Style.RESET_ALL}{FriendUser}")
                        elif DeleteRes.status_code == 429:
                            Retry = DeleteRes.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to unfriend : {Style.RESET_ALL}{FriendUser}")

                        await asyncio.sleep(0.2)

                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to unfriend : {Style.RESET_ALL}{FriendUser}")

                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Friendlist unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to unfriend everyone{Style.RESET_ALL}")
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