def scan_cr2_image(image):
    markers = [b"\x49\x49\x2A\x00\x10\x00\x00\x00\x43\x52\x02\x00"]
    mid_marker = b"\xFF\xD8\xFF\xC4"
    end_marker = b"\xFF\xD9"

    #Scan file
    with open(image, "rb") as file:
        data = file.read()

        count = 0
        for marker in markers:
            start_offset = data.find(marker)

            while start_offset != -1:
                middle_offset = data.find(mid_marker, start_offset)
              
                if middle_offset != -1:
                    end_offset = data.find(end_marker, middle_offset)
                    if end_offset != -1:
                        count += 1
                        # Save

                        with open(f"./IMG/IMG_{count}.CR2", "wb") as w:
                            if count == 1:
                                print(f" _IMG_{count}.CR2")
                            else:
                                print(f"|_IMG_{count}.CR2")
                            w.write(data[start_offset:end_offset + len(end_marker)])

                        start_offset = data.find(marker, end_offset)
                    else:
                        break
                else:
                    break