def Scan_CR3_Partition(partition, addbyte):
	block_size = 512
	data_disk = open(f"\\\\.\\{partition}:", "rb")
	byte = data_disk.read(block_size) # read 512 byte first
	offset = count = 0
	drec = False

	while byte:
		# Find header
		find_header = byte.find(b'\x00\x00\x00\x18\x66\x74\x79\x70\x63\x72\x78\x20\x00\x00\x00\x01')

		if find_header >= 0:
			drec = True
			print(f"|_IMG_{count}.CR3")

			#Save header
			Save = open(f"IMG_{count}.CR3", "wb")
			Save.write(byte[find_header:])

			while drec:
				byte = data_disk.read(block_size)
				# Find end 
				find_end 	= byte.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")

				if find_end >= 0:
					byte = data_disk.read(addbyte)
					#Save end & file
					Save.write(byte[:find_end + addbyte - 512])

					data_disk.seek((offset+1)*block_size)
					drec = False
					count += 1
				else: 
					Save.write(byte)
					
		byte = data_disk.read(block_size)
		offset += 1
	data_disk.close()

def Scan_CR3_Image(image, addbyte):
	# Read byte image
    with open(image, 'rb') as f:
        data = f.read()

    # 3 marker & size (s = start, m = mid, e = end)
    s_marker = b"\x00\x00\x00\x18\x66\x74\x79\x70\x63\x72\x78\x20\x00\x00\x00\x01"
    m_marker = b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF"
    e_size = addbyte

    # 3 offset (s = start, m = mid, e = end)
    # count & find s_marker 
    count = 0
    s_offset = data.find(s_marker)
    
    while s_offset != -1:
    	# Find m_marker 
        m_offset = data.find(m_marker, s_offset)
        
        if m_offset != -1:
        	# + e_size
            e_offset = m_offset + e_size
            count += 1

            #Save
            with open(f'IMG_{count}.CR3', 'wb') as out_file:
                out_file.write(data[s_offset:e_offset])

            print(f"|_IMG_{count}.CR3")
            s_offset = data.find(s_marker, e_offset)
        else:
            break