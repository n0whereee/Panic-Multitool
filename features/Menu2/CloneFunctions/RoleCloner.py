from config.settings import *

async def CloneRoles(TargetId, CloneId, headers):
    roles = requests.get(f"{BaseUrl}/guilds/{TargetId}/roles", headers=headers)
    DelRoles = requests.get(f"{BaseUrl}/guilds/{CloneId}/roles", headers=headers)

    DelRolesData = DelRoles.json()

    if roles.status_code in SuccesStatus:
        for DelRole in DelRolesData:
            DelRoleName = DelRole["name"]
            DelRoleID = DelRole["id"]

            if DelRole["name"] == "@everyone":
                continue
            
            rDel = requests.delete(
                f"{BaseUrl}/guilds/{CloneId}/roles/{DelRoleID}",
                headers=headers
            )

            if rDel.status_code in SuccesStatus:
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Deleted role              : {Style.RESET_ALL}{DelRoleName} - {DelRoleID}")
            elif rDel.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)      
            else:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to delete role     : {Style.RESET_ALL}{DelRoleName} - {DelRoleID}")
                
            time.sleep(0.2)

        RolesData = roles.json()
        RoleMap = {}
        RoleMap[TargetId] = CloneId

        for role in RolesData:
            RoleName = role["name"]
            RoleID = role["id"]

            Payload = {
                "name": role["name"],
                "permissions": role["permissions"],
                "color": role["color"]
            }

            if role["name"] == "@everyone":
                continue

            r = requests.post(
                f"{BaseUrl}/guilds/{CloneId}/roles",
                headers=headers,
                json=Payload
            )

            if r.status_code in SuccesStatus:
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned role               : {Style.RESET_ALL}{RoleName} - {RoleID}")
                try:
                    RoleMap[role["id"]] = r.json()["id"]
                except Exception:
                    pass

            elif r.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry) 
            else:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone role      : {Style.RESET_ALL}{RoleName} - {RoleID}")

            time.sleep(0.2)
            
    else:
        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Roles unavailable{Style.RESET_ALL}")

    return RoleMap