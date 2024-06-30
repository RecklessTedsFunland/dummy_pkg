# Notes

## USB Drive

- USB drive is 32GB formatted FAT32
    - FAT32 allows drive to be used in both Linux and macOS
- Everything is executable ... because it is FAT32?
- Shouldn't it automount to `/media` when the drive is inserted?

```bash
$ sudo mkdir -p /mnt/usbdrive

$ id
uid=1000(kevin) gid=1003(kevin) groups=1003(kevin),4(adm),20(dialout),24(cdrom),27(sudo),29(audio),44(video),46(plugdev),60(games),100(users),107(netdev),992(render),995(input),1000(gpio),1001(spi),1002(i2c)

$ sudo mount /dev/sda1 /mnt/usbdrive -o uid=1000
$ sudo umount /mnt/usbdrive
```

- [Ubuntu help on USB drives](https://help.ubuntu.com/community/Mount/USB) says automount should work
- [askubuntu question about failure to automount](https://askubuntu.com/questions/1452580/how-to-automount-a-usb-key-when-plugged-in-on-ubuntu-22-04) suggests doing: `dosfslabel /dev/sda1 DISKNAME`

## Foxglove Bridge

```bash
ros2 launch foxglove_bridge foxglove_bridge_launch.xml
```