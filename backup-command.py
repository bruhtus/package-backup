import os

os.system('pacman -Qqen > pkglist-repo.txt')
os.system('pacman -Qqem > pkglist-aur.txt')
