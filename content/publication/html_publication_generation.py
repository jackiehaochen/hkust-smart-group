import csv

with open('test.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  total_paper = 0
  for row in reader:
    total_paper += 1
    print('''<small><a href="'''+row['URL']+'''">'''+ row['Title'] + "</a></small><i><small><small><br>"+row['Authors']+'.'+row['Source']+'</br></small></small></i>\n')

