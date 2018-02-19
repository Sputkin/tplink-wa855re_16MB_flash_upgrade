# tplink-wa855re_16MB_flash_upgrade


 ##### spi0.0: w25q128 (16384 Kbytes)
 ##### spi0.0:128k(u-boot)ro,1600k(kernel),14336k(rootfs),256k(config),64k(art),15936k@0x20000(firmware)

    root@LEDE:~# cat /proc/mtd
     dev:    size   erasesize  name
     mtd0: 00020000 00010000 "u-boot"
     mtd1: 00190000 00010000 "kernel"
     mtd2: 00e00000 00010000 "rootfs"
     mtd3: 00c30000 00010000 "rootfs_data"
     mtd4: 00040000 00010000 "config"
     mtd5: 00010000 00010000 "art"
     mtd6: 00f90000 00010000 "firmware"


     Filesystem                Size      Used Available Use% Mounted on
     /dev/root                 2.0M      2.0M         0 100% /rom
     tmpfs                    13.7M     56.0K     13.7M   0% /tmp
     tmpfs                    13.7M     48.0K     13.7M   0% /tmp/root
     tmpfs                   512.0K         0    512.0K   0% /dev
     /dev/mtdblock3           12.2M    480.0K     11.7M   4% /overlay
     overlayfs:/overlay       12.2M    480.0K     11.7M   4% /

