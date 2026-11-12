from config.settings import *

async def LeaveAllServers(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Server selfbot{Style.RESET_ALL}")
    time.sleep(0.05)

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseUrl}/users/@me/guilds", headers=HEADERS
        )

        if res.status_code in SuccesStatus:
            Guilds = res.json()

            if not Guilds:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No servers found{Style.RESET_ALL}")
                time.sleep(2)
                return

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Leaving all servers... {Style.RESET_ALL}")
            time.sleep(1.5)
            try:
                print("")
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

                for guild in Guilds:
                    GuildId = guild["id"]
                    GuildName = guild.get("name", "Unknown Server")

                    try:
                        DeleteRes = await client.delete(
                                f"{BaseUrl}/users/@me/guilds/{GuildId}",
                                headers=HEADERS)
                        
                        if DeleteRes.status_code in SuccesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Left server            : {Style.RESET_ALL}{GuildName} - {GuildId}")
                        elif DeleteRes.status_code == 429:
                            Retry = DeleteRes.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave server : {Style.RESET_ALL}{GuildName} - {GuildId}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave server : {Style.RESET_ALL}{GuildName} - {GuildId}")
    
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Servers unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to leave all servers{Style.RESET_ALL}")
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