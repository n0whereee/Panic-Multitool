from config.settings import *

def CorruptImage():
        os.system("cls")
        Slow(FileBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Image corrupter{Style.RESET_ALL}")
        print("")
        Raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Image -> {Style.RESET_ALL}")

        FilePath = CleanPath(Raw)

        if not os.path.isfile(FilePath):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image not found :{Style.RESET_ALL} {FilePath}")
            time.sleep(2)
            return

        def IsImage(path):
            with open(path, "rb") as f:
                header = f.read(20)

            signatures = [
                b"\x89PNG\r\n\x1a\n",
                b"\xff\xd8\xff",
                b"GIF87a",
                b"GIF89a",
                b"RIFF"
            ]

            return any(header.startswith(sig) for sig in signatures)

        if not IsImage(FilePath):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid file type{Style.RESET_ALL}")
            time.sleep(2)
            return

        try:
            with open(FilePath, "rb") as f:
                data = bytearray(f.read())

            FileSize = len(data)

            if FileSize < 2560 or FileSize > 41943040:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image too large or too small{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            MinPos = 1500
            MaxPos = FileSize - 1000
            
            if FileSize < 5120:
                GlitchCount = 10
            elif FileSize < 10240:
                GlitchCount = 20
            elif FileSize < 20480:
                GlitchCount = 30
            elif FileSize < 51200:
                GlitchCount = 40
            elif FileSize < 102400:
                GlitchCount = 50
            elif FileSize < 512000:
                GlitchCount = 60
            elif FileSize < 1048576:
                GlitchCount = 70
            elif FileSize < 2097152:
                GlitchCount = 80
            elif FileSize < 5242880:
                GlitchCount = 90
            elif FileSize < 10485760:
                GlitchCount = 100
            elif FileSize < 20971520:
                GlitchCount = 110
            elif FileSize < 31457280:
                GlitchCount = 120
            else:
                GlitchCount = 500

            Rnd = random.Random()
            for _ in range(GlitchCount):
                    pos = Rnd.randint(MinPos, MaxPos)
                    data[pos] = Rnd.randint(0, 255)

            with open(FilePath, "wb") as f:
                    f.write(data)

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Corrupting image... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Image corrupted :{Style.RESET_ALL} {FilePath}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image could not be corrupted{Style.RESET_ALL}")
            time.sleep(2)
        