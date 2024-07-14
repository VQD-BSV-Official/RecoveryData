''' find byte (have in cr3) count bytes ==> end
All files captured with a device have the same count of bytes
'''

import os 

def get_folder_cr3():
	for filename in os.listdir(os.getcwd()):
		if filename.endswith(".CR3"):
			# Path + file name
			file_path = os.path.join(os.getcwd(), filename)
			with open(file_path, "rb") as r:
				data_find = r.read()
			# start count bytes
			offset_byte = data_find.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")
			add_byte = len(data_find[offset_byte:])

			print(filename, " ==> ", add_byte)

def get_file_cr3():
	with open("File_.CR3", "rb") as r:
		data_find = r.read()
	# start count bytes
	offset_byte = data_find.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")
	add_byte = len(data_find[offset_byte:])

	print("==> ", add_byte)

def save_file_cr3():
	with open("File_Test.CR3", "rb") as r:
		data = r.read()

	offset = data.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")

	with open ("out.cr3", "wb") as w:
		w.write(data[:offset + add_byte])