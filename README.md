# Manjaro Package List Backup

This repo is for my package list backup so that i can re-install all my package without remembering all of them.

#### To backup all of your currently installed package
```bash
sudo pacman -Qeq > pkglist.txt
```

#### To restore / re-install all 0f your package
```bash
sudo pacman -S --needed $(< pkglist.txt)
```
or

```bash
yourt -S --needed $(< pkglist.txt) #which would install all package including those from the AUR
```
