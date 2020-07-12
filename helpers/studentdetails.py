import csv

csv_data = [['ID', 'Name ', 'email', 'fee', 'deposit'],
           ['1', 'Sam', 'sam@gmail.com', '20000', '10000'],
           ['2', 'John', 'nhojgmail.com', '20000', '10000'],
           ['3', 'Samu', 'san@gmail.com', '20000', '10000']]

with open('student_details.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)
