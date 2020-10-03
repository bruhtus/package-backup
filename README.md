# i3 Window Manager Configuration

i3 is a tling window manager (usually called i3wm). The default configuration may vary depending on your distro, in my case the default configuration file is on $HOME/.i3/config (you can search using `locate .i3/config` but don't forget to do `sudo updatedb` first).
You can find the info about i3 on [their website](https://i3wm.org) or [their documentation](http://i3wm.org/docs/).

The component used in this config is:
- [pywal](https://github.com/dylanaraps/pywal)
- [polybar](https://github.com/polybar/polybar)
- [py3status](https://github.com/ultrabug/py3status)
- [rofi](https://github.com/davatorium/rofi)
- [conky](https://github.com/brndnmtthws/conky)
- [flameshot](https://github.com/flameshot-org/flameshot)

If you're using the default config from /usr/ folder then you need to change ownership of that file using the command below:
```bash
sudo chown owner.group folder/file
```
you can check owner and group by using `ls -lart` in the folder (the owner is on column 3 and the group on column 4).
(For more information about change ownership you can see [this article](https://www.howtoforge.com/linux-chown-command/).

You could change new terminal color scheme by adding pywal color scheme to you shell config (.bashrc or .zshrc or something else) by adding this command:
```bash
(cat ~/.cache/wal/sequences &)
cat ~/.cache/wal/sequences
source ~/.cache/wal/colors-tty.sh
```

#### Mounting External Drives For Ranger
Use `lsblk` to find external drives and then do `udisksctl mount -b /dev/sdxY` to mount the external drives or do `udisksctl unmount -b /dev/sdxY` to unmount the external drives.

For example: `udisksctl mount -b /dev/sdb1` or `udiskctl unmount -b /dev/sdb1`

File [startxrandr.sh](startxrandr.sh) is for setting up dual monitor with xrandr.
