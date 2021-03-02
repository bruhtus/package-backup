# Arch-based Linux Package List Backup and Restore

This repo is for my package list backup so that i can re-install all my package without remembering all of them. You can also use the command below to backup and re-install your package on new installation.

### To backup all of your currently installed package
#### Backup package in official repository
```bash
pacman -Qqen > pkglist-repo.txt
```

#### Backup package in arch user repository (AUR)
```bash
pacman -Qqem > pkglist-aur.txt
```

### To restore / re-install all of your package
#### For repository package
```bash
sudo pacman -S --needed - < pkglist-repo.txt
```

#### For AUR package
```bash
for x in $(< pkglist-aur.txt); do yay -S $x; done
```

The information was gathered from [here](https://classicforum.manjaro.org/index.php?topic=16484.0).

Another useful information to restore system, [here you go](https://forum.manjaro.org/t/how-to-save-your-manjaro-installation-when-it-breaks/3902).

To access TTY you can use `Ctrl+Alt+F2` to access TTY2 (or another function key to access another TTY).

For how to install virt-manager, you can check the [wiki](https://github.com/bruhtus/manjaro_backup/wiki).

For setting up the bluetooth devices: <br>
Install pulseaudio bluetooth using command below:
```bash
sudo pacman -S pulseaudio-bluetooth
```
and then run the following command:
```bash
pactl load-module module-bluetooth-discover
```
That's all.
