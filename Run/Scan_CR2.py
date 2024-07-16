def Scan_CR2_Image(image):
    # Read byte image
    with open(image, "rb") as file:
        data = file.read()

    # 3 marker (s = start, m = mid, e = end)
    s_marker = b"\x49\x49\x2A\x00\x10\x00\x00\x00\x43\x52\x02\x00"
    m_marker = b"\xFF\xD8\xFF\xC4"
    e_marker = b"\xFF\xD9"

    # 3 offset (s = start, m = mid, e = end)
    # count & find s_marker 
    count = 0
    s_offset = data.find(s_marker)

    while s_offset != -1:
        # Find m_marker 
        m_offset = data.find(m_marker, s_offset)
      
        if m_offset != -1:
            # Find e_marker
            e_offset = data.find(e_marker, m_offset)

            if e_offset != -1:
                count += 1

                # Save
                with open(f"IMG_{count}.CR2", "wb") as w:
                    w.write(data[s_offset:e_offset + len(e_marker)]) # len = 2 byte FF D9
                
                print(f"|_IMG_{count}.CR2")
                s_offset = data.find(s_marker, e_offset)
            else:
                break
        else:
            break