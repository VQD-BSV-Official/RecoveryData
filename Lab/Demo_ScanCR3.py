import os, subprocess

def Scan_CR3_Partition():
	block_size = 512
	data_disk = open("\\\\.\\D:", "rb")
	byte = data_disk.read(block_size) # read 512 byte first
	offset = conut = 0
	drec = False

	while byte:
		# tìm thấy header
		find_header = byte.find(b'\x00\x00\x00\x18\x66\x74\x79\x70\x63\x72\x78\x20\x00\x00\x00\x01')
		if find_header >= 0:
			drec = True

			print('==== Found CR3 at location: ' + str(hex(find_header+(block_size*offset))) + ' ====')

			#Lưu header
			Save = open(f"IMG_{conut}.CR3", "wb")
			Save.write(byte[find_header:])

			while drec:
				byte = data_disk.read(block_size)
				find_end 	= byte.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")

				if find_end >= 0:
					byte = data_disk.read(7762)
					#Lưu end
					Save.write(byte[:find_end + 7762 - 512])

					data_disk.seek((offset+1)*block_size)
					drec = False
					conut += 1
				else: 
					Save.write(byte)

		byte = data_disk.read(block_size)
		offset += 1
	data_disk.close()