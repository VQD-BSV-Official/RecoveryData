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

#=============================================
from Run.get_partition import get_partition_info
import platform, os, time

# Loop
while True:
   form()
   a = input()
   # choose()