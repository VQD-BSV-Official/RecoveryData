disk = r'\\.\E:'  # disk
out_file = "Disk.img"  # out

# read & write
with open(disk, 'rb') as disk:
    with open(out_file, 'wb') as w:
        while True:
            byte = disk.read(4096)
            if not byte:
                break  # Exit loop
            # Write byte
            w.write(byte)