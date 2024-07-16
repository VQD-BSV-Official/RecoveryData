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
					byte = data_disk.read(add_byte)
					#Lưu end
					Save.write(byte[:find_end + add_byte - 512])

					data_disk.seek((offset+1)*block_size)
					drec = False
					conut += 1
				else: 
					Save.write(byte)

		byte = data_disk.read(block_size)
		offset += 1
	data_disk.close()

def Scan_CR3_Image(image_path, output_dir):
    with open(image_path, 'rb') as f:
        data = f.read()

    start_marker = b"\x00\x00\x00\x18\x66\x74\x79\x70\x63\x72\x78\x20\x00\x00\x00\x01"
    mid_marker = b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF"
    end_marker_size = 7762

    file_count = 0
    start_offset = data.find(start_marker)
    
    while start_offset != -1:
        middle_offset = data.find(mid_marker, start_offset)
        
        if middle_offset != -1:
            end_offset = middle_offset + end_marker_size
            file_count += 1

            cr3_filename = os.path.join(output_dir, f'IMG_{file_count}.CR3')
            with open(cr3_filename, 'wb') as out_file:
                out_file.write(data[start_offset:end_offset])

            print(f'Extracted {cr3_filename} from {start_offset} to {end_offset}')
            start_offset = data.find(start_marker, end_offset)
        else:
            break

# Đường dẫn đến tệp phân vùng
image_path = 'Partition_D.img'
output_dir = os.getcwd()
os.makedirs(output_dir, exist_ok=True)

Scan_CR3_Image(image_path, output_dir)
