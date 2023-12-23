#!/usr/bin/env python3

""" Reversed by Exotic-Hridoy """

try:
    from rich.console import Console
    import os, time, re, json, requests
    from rich.panel import Panel
except (Exception, KeyboardInterrupt) as e:
    from urllib.parse import quote
    __import__('os').system(f'xdg-open https://wa.me/6283861251898?text=PREMIUM%20%3A%20{quote(str(e))}')
    exit()

class Main:

    def __init__(self) -> None:
        pass

    def Command(self):
        self.Banner()
        Console(width=71, style="bold royal_blue1").print(Panel("[italic red]You can contact the admin so you can try this Premium script, because the Apikey website service is having problems. You have to ask the admin to activate this command manually."))
        Console().input("[bold white][[bold green]WhatsApp[bold white]]")
        time.sleep(5.0)
        os.system(f'xdg-open https://wa.me/6283861251898?text=Hallo%20Bang%3F%0AI%20want%20to%20try%20and%20activate%20the%20Premium%20script%21')
        exit()

    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return ("Sukses Membersihkan Terminal")

    def Banner(self):
        self.Clear()
        Console(width=71, style="bold royal_blue1").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold blue]    ||[bold white]Release :[bold green] 30-Juli-2021[bold blue]||[bold white]Author :[bold yellow] Luthfi[bold blue]||[bold white]Version :[bold green] 100.0[bold blue]||
__    __  __  ____  _   _  ____  ____ 
(  )  (  )(  )(_  _)( )_( )( ___)(_  _)
 )(__  )(__)(   )(   ) _ (  )__)  _)(_ 
(____)(______) (__) (_) (_)(__)  (____) Author : Luthfi XD
\t\t[underline blue]INSTAGRAM BRUTE FORCE PREMIUM""")) # Coded by Luthfi-XD
        return ("Sukses Menampilkan Banner")

if __name__ == '__main__':
    try:
        terminal_size = re.search('columns=(\d+),', str(os.get_terminal_size())).group(1)
        if json.loads(requests.get('https://ipinfo.io/json').text)['country'] == "ID":
            if int(terminal_size) < 71:
                Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Harap Kecilkan Tampilan Termux Dengan Cara Mencubit Layar Dalam Aplikasi Termux, Kecilkan Panel Ini Sampai Terlihat Rapi!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Kecilkan Tampilan Termux) [bold green]<[bold yellow]<[bold red]<"))
                exit()
            else:
                os.system('git pull')
                Main().Command()
        else:
            Main().Banner()
            Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]Premium tools can only be accessed in Indonesian, other than Indonesian it will not work properly!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Indonesian Only) [bold green]<[bold yellow]<[bold red]<"))
            exit()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        Console(width=71, style="bold royal_blue1").print(Panel(f"[italic red]{str(e).title()}!", title="[bold red]>[bold yellow]>[bold green]>[bold royal_blue1] (Error) [bold green]<[bold yellow]<[bold red]<"))
        exit()

"""

 > what bro? | -_- |

 > Do you really deserve the source?

"""