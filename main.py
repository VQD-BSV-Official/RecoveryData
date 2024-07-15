# Print header
def header():
   os.system("cls")

   with open("header.txt", "r") as r:
      print(r.read())

# Print partition info
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

# Tool
def check(partition):
   key = input("\n==> ")

   if key == "Get_Image":
      get_image(partition)

# Get Image      
def get_image(partition):
   disk = r'\\.\{}:'.format(partition) # read disk
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

# Scan Image
def scan_image():
   # input & print
   print("Enter File Path"); image = input("\n==> "); header()
   print("=> ",image)

   if image == "x":  
      return
   else:
      # input & print
      print("CR2/CR3/x"); file = input("\n==> "); header()
      print("=> ",image); print("=> ",file)

      # Extension
      if file == "CR2":
         print("\n")
         Scan_CR2_Image(image)
#=============================================
from Run.get_partition import get_partition_info
from Run.Scan_CR2 import Scan_CR2_Image
from Run.Scan_CR3 import Scan_CR3_Partition

import platform, os, time

# Loop
while True:
   # Create Form & call def get info
   header(); info_part = get_info()
   print("\n#Scan_Image")

   # Choose partition
   select_partition = input("\n==> ")
   # break 
   if select_partition == "x": break
   # Scan_Image
   if select_partition == "Scan_Image":
      header()
      scan_image()

   # if int   
   elif int(select_partition) != 0:
      header()
      # get partition & print
      get_part = info_part.splitlines()[int(select_partition) - 1]
      print(get_part[4:]); print("""\n#Scan #Get_Image"""); check(get_part[7])
      