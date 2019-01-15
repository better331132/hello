filename = "a.bin"
filename_text = "a.txt"
data = 100

with open(filename, "wb") as f:
    f.write(bytearray([data]))

with open(filename_text, "w") as i:
    i.write(str(data))