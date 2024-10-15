#!/usr/bin/python3

import pyfiglet
import subprocess


def check_root() -> bool:
    return subprocess.run("id -u", shell=True, capture_output=True) == 0



if __name__ == '__main__':
    if check_root() == False:
        print(pyfiglet.figlet_format("Need root!", font="ANSI Shadow"))
        exit(1)


