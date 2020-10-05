# Manjaro Package List Backup and Restore

This repo is for my package list backup so that i can re-install all my package without remembering all of them.

### To backup all of your currently installed package
#### Backup package in repository
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
for x in $(cat pkglist-aur.txt); do pamac build $x; done
```

The information was gathered from [here](https://classicforum.manjaro.org/index.php?topic=16484.0)

For how to install virt-manager, you can check the [wiki](https://github.com/bruhtus/manjaro_backup/wiki)
