# header RecoveryData
def header():
   with open("header.txt", "r") as r:
      os.system("cls"); print(r.read())

# partition info
def get_info():
   # get disk info
   drive_info = get_partition_info()

   count = 0
   info_part = ""
   for drive, info in drive_info.items():
      count += 1
      if f"{info['total_gb']}" == "Unknown":
         info_part += f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']} GB\n"
      else:
         info_part += f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']:.2f} GB\n"

   # out ket qua
   return info_part
#=============================================
# Create Form & return info
def form():
   header(); info_part = get_info()
   print("\n#Scan_Image")

   return info_part
#=============================================
def forks(partition, name_part):
   key = input("\n==> ")

   actions = {
       "x": lambda: None,  # break
       "Scan": lambda: scan(partition, name_part),
       "Get_Image": lambda: get_image(partition)
   }

   # check & break if key là "x"
   actions.get(key, lambda: None)()


# Get Image      
def get_image(partition):
   disk = r'\\.\{}:'.format(partition) # read
   out_file = f"Partition_{partition}.img"  # out file

   # read & write
   with open(disk, 'rb') as disk:
       with open(out_file, 'wb') as w:
           while True:
               byte = disk.read(1048576) # 1 MB
               if not byte:
                   break  # Exit loop
               # Write byte
               w.write(byte)


# Scan
def scan(partition, name_part):
   header(); print(name_part)
   # input extension
   print("Extension: CR2/CR3"); extension = input("\n==> ")
   header(); print(name_part)
   print("=> Scan",extension)
   
   if extension == "CR2":
      print("Demo")
      # Scan_CR2(partition)

   elif extension == "CR3":
      file = input("Enter File Path\n\n==> ");
      # Creat new form
      header(); print(name_part)
      print(f"=> Scan {extension}\n=> {file}")

      # Lấy số byte để addbyte
      with open(file, "rb") as r:
         data_find = r.read()
      # start count bytes
      offset_byte = data_find.find(b"\x08\x00\x00\x00\x86\x00\x00\x00\xD7\x03\x02\x00\x0B\x58\xFF\xFF")
      addbyte = len(data_find[offset_byte:])

      Scan_CR3(partition, addbyte)

# Scan Image
def scan_image():
   # input path
   print("Enter File Path"); path = input("\n==> "); header()
   print("=> ",path)

   if path == "x":
      return
   else:
      # input extension
      print("Extension: CR2/CR3"); extension = input("\n==> "); header()
      print("=> ",path, " \n=> ",extension)

      if extension == "CR2":
         Scan_CR2_Image(path)

      elif extension == "CR3":
         print("Demo")
         # Scan_CR3_Image(path)

#=============================================
from Run.get_partition import get_partition_info
from Run.Scan_CR2 import Scan_CR2_Image
from Run.Scan_CR3 import Scan_CR3
import os, time

# Loop
while True:
   info_part = form()

   # Choose
   select = input("\n==> ")
   if select == "x": break

   elif select == "Scan_Image":
      header(); scan_image()

   # if is num   
   elif int(select) != 0:
      header()
      # get partition & print
      get_part = info_part.splitlines()[int(select) - 1]
      name_part = get_part[4:]
      print(get_part[4:]); print("""\n#Scan #Get_Image"""); forks(get_part[7], name_part)
