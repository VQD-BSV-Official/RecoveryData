import os, subprocess

block_size = 512

data_disk = open("\\\\.\\E:", "rb")

byte = data_disk.read(block_size)

offset = 0
conut = 0

drec = False

while byte:
	find_header = byte.find(b'\xFF\xD8\xFF\xDB\x00\x84')
	if find_header >= 0:
		drec = True

		print('==== Found JPG at location: ' + str(hex(find_header+(block_size*offset))) + ' ====')

		#Lưu header
		Save = open(f"IMG_{conut}.JPG", "wb")
		Save.write(byte[find_header:])

		while drec:
			byte = data_disk.read(block_size)
			find_end 	= byte.find(b'\xFF\xD9')

			if find_end >= 0:
				#Lưu end
				Save.write(byte[:find_end + 2])

				data_disk.seek((offset+1)*block_size)
				drec = False
				conut += 1
			else: 
				Save.write(byte)

#=============================================================================
		if os.path.exists(f"IMG_{conut - 1}.JPG"):
			with open(f"IMG_{conut - 1}.JPG", "rb") as r:
				data = r.read()
				pass
			if b'\xFF\xC0\x00\x11\x08\x00\x78\x00\xA0' in data:
				pr0c = ["del_file.bat", f"IMG_{conut - 1}.JPG"]

				startupinfo = subprocess.STARTUPINFO()
				startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
				subprocess.Popen(pr0c, startupinfo=startupinfo)   
#=============================================================================

	byte = data_disk.read(block_size)
	offset += 1
data_disk.close()

