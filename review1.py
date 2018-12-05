# with open("students.csv", "r", encoding = "utf8") as file:
#     for line in file:
#         return line
# print(a)
import csv
reader = csv.reader("students.csv", dialect = 'excel')
for row in reader:
    writer = csv.writer("students.csv", dialect = 'excel')
    writer.writerow(['aaa', 'bbb'])
print(writer)