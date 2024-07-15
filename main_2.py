# header RecoveryData
def header():
   os.system("cls")

   with open("header.txt", "r") as r:
      print(r.read())

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
# Create Form & Get info
def form():
   header(); info_part = get_info()
   print("\n#Scan_Image")

   return info_part
#=============================================
def forks(partition):
   key = input("\n==> ")

   if key == "x":
      return
   elif key == "Scan":
      scan(partition)
   elif key == "Get_Image":
      get_image(partition)

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
def scan(partition):
   # input extension
   print("Extension: CR2/CR3"); extension = input("\n==> "); header()
   print("=> ",path, " => ",extension)
   
   if extension == "CR2":
      Scan_CR2(path)

   elif extension == "CR3":
      Scan_CR3(path)

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
      print("=> ",path, " => ",extension)
      
      if extension == "CR2":
         Scan_CR2_Image(path)

      elif extension == "CR3":
         Scan_CR3_Image(path)

#=============================================
from Run.get_partition import get_partition_info
from Run.Scan_CR2 import Scan_CR2_Image
from Run.Scan_CR3 import Scan_CR3_Image
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
      print(get_part[4:]); print("""\n#Scan #Get_Image"""); forks(get_part[7])
