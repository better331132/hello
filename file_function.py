def write_file():
    with open("a.xls","w", encoding='utf8') as file :
        file.write("이름, 성별, 나이\n")
        file.write("김일수, 남, 14\n")
        file.write("김이수, 남, 24")
# write_file()

with open("filename", "r", encoding='utf8') as file:
    for line in file:
        print(line)

