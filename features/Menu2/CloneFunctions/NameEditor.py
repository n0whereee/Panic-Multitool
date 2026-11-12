from config.settings import *

def EditName(TargetId, CloneId, headers):
        TargetRes  = requests.get(f"{BaseUrl}/guilds/{TargetId}", headers=headers)
        TargetName = TargetRes.json().get("name", "Unknown Server")

        payload = {
            "name": TargetName
        }
        
        res = requests.patch(
            f"{BaseUrl}/guilds/{CloneId}", 
            headers=headers, 
            json=payload
        )
        
        if res.status_code in SuccesStatus:
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned server name        : {Style.RESET_ALL}{TargetName}")
        else:
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone name      : {Style.RESET_ALL}{TargetName}")