import csv    
f = open('output.csv', 'w', encoding='euc-kr', newline='')
wr = csv.writer(f)
wr.writerow([1, "김정수", False])
wr.writerow([2, "박상미", True])
f.close()