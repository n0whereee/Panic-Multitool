from config.settings import *

def ExtractMetadata():
        os.system("cls")
        Slow(AnalyzeBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Metadata extractor{Style.RESET_ALL}")
        print("")
        Raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Image -> {Style.RESET_ALL}")

        Image = CleanPath(Raw)

        if not os.path.isfile(Image):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image not found :{Style.RESET_ALL} {Image}")
            time.sleep(2)
            return

        try:
            Img = PIL.Image.open(Image)

            RawExif = Img._getexif()

            if not RawExif:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No metadata found{Style.RESET_ALL}")
                time.sleep(2)
                return

            Exif = {}

            for k, v in Img._getexif().items():
                tag = PIL.ExifTags.TAGS.get(k)
                if tag:
                    Exif[tag] = v

            Make = Exif.get('Make', "None")
            Model = Exif.get('Model', "None")
            Software = Exif.get('Software', "None")
            Date = Exif.get('DateTime', "None")
            OriginalDate = Exif.get('DateTimeOriginal', "None")
            GpsInfo = Exif.get("GPSInfo")

            if not GpsInfo:            
                lat = None
                long = None
            else:
                try:
                    RawLat = GpsInfo[2]
                    RawLon = GpsInfo[4]

                    lat = RawLat[0]
                    long = RawLon[0]
                except Exception:
                    lat = None
                    long = None

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searchig for information... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Make           :{Style.RESET_ALL} {Make}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Model          :{Style.RESET_ALL} {Model}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Software       :{Style.RESET_ALL} {Software}")
            print("")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Recording time :{Style.RESET_ALL} {OriginalDate}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Last modified  :{Style.RESET_ALL} {Date}")
            print("")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Latitude       :{Style.RESET_ALL} {lat}")
            time.sleep(0.05) 
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Longitude      :{Style.RESET_ALL} {long}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Metadata could not be extracted{Style.RESET_ALL}")
            time.sleep(2)
        