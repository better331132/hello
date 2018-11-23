# def write_file():
#     with open("파일만들기.csv","w", encoding='utf8') as file :
#         file.write("이름, 성별, 나이\n김기,남,1\n님니,여,2\n딤디,남,3\n림리,여,4\n림리,여,5")
# write_file()

# with open("filename", "r", encoding='utf8') as file:
#     for line in file:
#         print(line)

def read_file():
    with open("파일만들기.csv","r", encoding = 'utf8') as file:
        for line in file:
            print(line)

read_file()
