import psutil, win32api

#get info
def get_partition_info():
    drives = psutil.disk_partitions()
    drive_info = {}
    for drive in drives:
        try:
            label = win32api.GetVolumeInformation(drive.device)[0]
        except:
            label = "No Label"

        try:
            usage = psutil.disk_usage(drive.mountpoint)
            total_gb = usage.total / (1024 ** 3)
        except:
            total_gb = "Unknown"

        fstype = drive.fstype

        drive_info[drive.device] = {
            "label": label,
            "total_gb": total_gb,
            "fstype": fstype
        }

    print_item(drive_info)
    return drive_info
    

# print info 
def print_item(drive_info):
    count = 0
    for drive, info in drive_info.items():
        count += 1

        if f"{info['total_gb']}" == "Unknown":
            print(f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']} GB")
        else:
            print(f"[{count}] => {drive:<4} | {info['label']:<10} | {info['fstype']} | {info['total_gb']:.2f} GB")
