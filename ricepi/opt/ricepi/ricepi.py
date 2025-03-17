# RicePy - The best Raspberry Pi utility
# Copyright (C) 2025  RaspberryRetards

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pystyle
import random
import time
import os
import subprocess
import platform

if os.name == "nt":
    raise RuntimeError("Not running on a Raspberry Pi or running Windows unofficially!")
elif platform.system() == "Linux":
    cpucat = subprocess.run("cat /proc/cpuinfo", shell=True, capture_output=True, text=True)
    if "Raspberry Pi" in cpucat.stdout:
        pass
    else:
        raise RuntimeError("Not running on a Raspberry Pi!")    

def termclear():
    os.system("clear")

ricepy_pystyle_colors = [
    pystyle.Colors.red_to_yellow,
    pystyle.Colors.blue_to_green,
    pystyle.Colors.blue_to_white,
    pystyle.Colors.blue_to_red,
    pystyle.Colors.blue_to_black,
    pystyle.Colors.white_to_black
]

color = random.choice(ricepy_pystyle_colors)

pystyle.Write.Print("""RicePi Copyright (C) 2025 RaspberryRetards
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.""", color, interval=0)
print()

def write_ascii():
    pystyle.Write.Print(f"""
██████╗ ██╗ ██████╗███████╗██████╗ ██╗
██╔══██╗██║██╔════╝██╔════╝██╔══██╗██║
██████╔╝██║██║     █████╗  ██████╔╝██║
██╔══██╗██║██║     ██╔══╝  ██╔═══╝ ██║
██║  ██║██║╚██████╗███████╗██║     ██║
╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝╚═╝     ╚═╝
""", color, interval=0)

write_ascii()

print()
pystyle.Write.Print(f"The best Raspberry Pi utility - #WeLoveGNU!", color, interval=0)
print()
print()
time.sleep(3)
while True:
    termclear()
    write_ascii()
    choice = pystyle.Write.Input("""
[1] Power options
[2] SSH options
[3] Internet options
[4] General options

Which option would you like to select? """, color, interval=0)
    if choice == "1":
        termclear()
        write_ascii()
        rchoice = pystyle.Write.Input("""
[1] Reboot
[2] Power off
[3] Halt
[4] Immediate reboot (DANGEROUS!)

Which reboot option would you like to select? """, color, interval=0)
        if rchoice == "1":
            os.system("sudo reboot")
        elif rchoice == "2":
            os.system("sudo poweroff")
        elif rchoice == "3":
            os.system("sudo halt")
        elif rchoice == "4":
            os.system("echo b | sudo tee /proc/sysrq-trigger")
    elif choice == "2":
        termclear()
        write_ascii()
        schoice = pystyle.Write.Input("""
[1] Enable SSH
[2] Disable SSH
[3] Test SSH (ssh localhost)

Which SSH option would you like to select? """, color, interval=0)
        if schoice == "1":
            os.system("sudo systemctl enable sshd")
            os.system("sudo systemctl start sshd")
        elif schoice == "2":
            os.system("sudo systemctl disable sshd")
            os.system("sudo systemctl stop sshd")
        elif schoice == "3":
            os.system("ssh localhost")
    elif choice == "3":
        termclear()
        write_ascii()
        ichoice = pystyle.Write.Input("""
[1] Show IP addresses
[2] Test internet connectivity
[3] Get router IP address

Which internet option would you like to select? """, color, interval=0)
        if ichoice == "1":
            print()
            os.system("ip a | grep inet")
            publicip = subprocess.run("curl ifconfig.me -4", text=True, shell=True, capture_output=True)
            print(f"    Oh, and your public IP: {publicip.stdout}")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif ichoice == "2":
            print()
            os.system("ping 8.8.8.8 -c 3")
            print()
            pystyle.Write.Print("Here is your result ^", color, interval=0)
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif ichoice == "3":
            print()
            os.system("ip route | grep default")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
    elif choice == "4":
        termclear()
        write_ascii()
        gchoice = pystyle.Write.Input("""
[1] Check current OS        [6] Check Active Processes
[2] Check Disk Usage        [7] View System Logs
[3] Check Memory Usage      [8] Display System Info
[4] Check CPU Info          [9] Update your system
[5] Check System Uptime     [10] Raspberry Pi Hardware Info
                            [11] Check Raspberry Pi Model and revision

Which option would you like to select? """, color, interval=0)
        if gchoice == "1":
            os_info = {}
            with open("/etc/os-release") as f:
                for line in f:
                    key, _, value = line.partition("=")
                    os_info[key] = value.strip().strip('"')
            print()
            print("/etc/os-release says your OS is:", os_info["PRETTY_NAME"])
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "2":
            termclear()
            write_ascii()
            print()
            os.system("df -h")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "3":
            termclear()
            write_ascii()
            print()
            os.system("free -h")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "4":
            termclear()
            write_ascii()
            print()
            os.system("lscpu")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "5":
            termclear()
            write_ascii()
            print()
            os.system("uptime -p")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "6":
            termclear()
            write_ascii()
            print()
            os.system("top -n 1")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "7":
            termclear()
            write_ascii()
            print()
            os.system("journalctl -xe")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "8":
            termclear()
            write_ascii()
            print()
            os.system("uname -a")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "9":
            termclear()
            write_ascii()
            print()
            os.system("sudo apt-get upgrade")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "10":
            termclear()
            write_ascii()
            print()
            os.system("vcgencmd measure_temp")
            os.system("vcgencmd measure_volts")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)
        elif gchoice == "11":
            termclear()
            write_ascii()
            print()
            os.system("cat /proc/cpuinfo | grep 'Model'")
            os.system("cat /proc/cpuinfo | grep 'Revision'")
            print()
            pystyle.Write.Input("Press Enter to go back...", color, interval=0)