import sys


parts_name = ["u-boot","kernel","rootfs","config","art"]

def read_mtd_parts():
	parts = {}
	print("enter the dimension in kB\n")
	for name in parts_name:
		parts[name] = input("%s:"%name)
	
	return parts
	
def format_mtd_parts_safeloader(parts):
	uboot_sz = parts[parts_name[0]]*1024
	kernel_start = parts[parts_name[0]]*1024
	kernel_sz = parts[parts_name[1]]*1024
	rootfs_start =  (parts[parts_name[0]]*1024)+parts[parts_name[1]]*1024
	rootfs_sz = parts[parts_name[2]]*1024
	partition_table_start = ((parts[parts_name[0]]*1024)+parts[parts_name[1]]*1024)+parts[parts_name[2]]*1024 
	partition_table_sz = 0x02000
	default_mac_start = partition_table_start+0x10000
	default_mac_sz = 0x00020
	pin_start = default_mac_start+0x100
	pin_sz = 0x00020
	product_info_start = pin_start+0xf00
	product_info_sz = 0x01000
	soft_version_start = product_info_start+0x1000
	soft_version_sz = 0x00100
	support_list_start = soft_version_start+0x1000
	support_list_sz = 0x01000
	profile_start = support_list_start+0x1000
	profile_sz = 0x08000
	user_config_start = profile_start+0xc000
	user_config_sz = 0x10000
	default_config_start = user_config_start+0x10000
	default_config_sz = 0x10000
	radio_start = default_config_start+0x10000
	radio_sz = parts[parts_name[4]]*1024

	formatted = ('.partitions = {\n\
			{"fs-uboot", %s, %s},\n\
			{"os-image", %s, %s},\n\
			{"file-system", %s, %s},\n\
			{"partition-table", %s, %s},\n\
			{"default-mac", %s, %s},\n\
			{"pin", %s, %s},\n\
			{"product-info", %s, %s},\n\
			{"soft-version", %s, %s},\n\
			{"support-list", %s, %s},\n\
			{"profile", %s, %s},\n\
			{"user-config", %s, %s},\n\
			{"default-config", %s, %s},\n\
			{"radio", %s, %s},\n\
			{NULL, 0, 0}\n\
		},\n'%("0x00000",hex(uboot_sz),hex(kernel_start),hex(kernel_sz),hex(rootfs_start),hex(rootfs_sz),\
				hex(partition_table_start),hex(partition_table_sz),hex(default_mac_start),hex(default_mac_sz),hex(pin_start),hex(pin_sz),hex(product_info_start),hex(product_info_sz),\
				hex(soft_version_start),hex(soft_version_sz),hex(support_list_start),hex(support_list_sz),hex(profile_start),hex(profile_sz),hex(user_config_start),hex(user_config_sz),\
				hex(default_config_start),hex(default_config_sz),hex(radio_start),hex(radio_sz)))

	return formatted

def main(param,arg={}):

	if not param:
		parts = read_mtd_parts()
	else:
		parts=arg

	print("############### PROFILE #####\n")

	print ('define Device/tl-wa855re-v1-16MB_flash\n\
\
			$(Device/tplink)\n\
			TPLINK_HWREV := 0\n\
			DEVICE_TITLE := TP-LINK TL-WA855RE (v1_16MB_flash)\n\
			BOARDNAME := TL-WA855RE-v1\n\
			DEVICE_PROFILE := TLWA855RE\n\
			TPLINK_HWID := 0x08550001\n\
			TPLINK_BOARD_ID := TLWA855REV1\n\
			KERNEL := kernel-bin | patch-cmdline | lzma | tplink-v1-header\n\
			IMAGE/sysupgrade.bin := append-rootfs | tplink-safeloader sysupgrade\n\
			IMAGE/factory.bin := append-rootfs | tplink-safeloader factory\n\
			MTDPARTS := spi0.0:%dk(u-boot)ro,%dk(kernel),%dk(rootfs),%dk(config),%dk(art),%dk@0x20000(firmware)\n\
			endef\n\
			TARGET_DEVICES += tl-wa855re-v1-16MB_flash\n'%(parts[parts_name[0]],parts[parts_name[1]],parts[parts_name[2]],parts[parts_name[3]],parts[parts_name[4]],parts[parts_name[1]]+parts[parts_name[2]]))

	print("\n############### safeloader.c ##### \n%s"%format_mtd_parts_safeloader(parts))
	print('\nuse "make tools/firmware-utils/compile" for recompile with new config\n')


if __name__ == "__main__":
	sz = len(sys.argv)
	if sz == 6:
		sys.argv.remove(sys.argv[0])
		
		for x in sys.argv:
			if not x.isdigit():
				sys.exit()
		
		parts = {parts_name[0]:int(sys.argv[0]),parts_name[1]:int(sys.argv[1]),parts_name[2]:int(sys.argv[2]),parts_name[3]:int(sys.argv[3]),parts_name[4]:int(sys.argv[4])}
		main(True,parts)

	else:
		main(False)




