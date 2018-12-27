import re

line = "Beautiful is better than ugly."

matches = re.findall("Beautiful", line)
# print(matches)

matches2 = re.findall("beautiful", line, re.IGNORECASE)
# print(matches2)

zen2 = """Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - - let's do more of those!"""

m = re.findall("^if", zen2, re.MULTILINE)
m2 = re.findall("now\.", zen2, re.MULTILINE)
m3 = re.findall("im.", zen2, re.MULTILINE)
m4 = re.findall("im.*", zen2, re.MULTILINE)
m5 = re.findall("idea.$", zen2, re.MULTILINE)

print(m,m2,m3,m4,m5)

string = "Two aa too"

m = re.findall("t[wo]o", string)
print(m)
m = re.findall("idea[l'']", zen2, re.IGNORECASE)
print(m)


m = re.findall("t[^w]o", string, re.IGNORECASE)
print(m)


string = "123?45yy7890 hi 999 hello"

m1 = re.findall("\d", string)
m2 = re.findall("[0-9]{1,3}", string)
m3 = re.findall("[1-5]{1,2}", string)

print("m1=", m1)
print("m2=", m2)
print("m3=", m3)

string = "aaaaaaa<hr>This<h1>awsed<h1>ar<h3>aerh<h4>dfbg<h1>"

abcd = re.compile("<(.*)>")         #cf. re.compile("<.*>")

mm = re.findall(abcd, string)
print(mm)

for m in re.finditer(abcd, string):
    print(m.groups(1))