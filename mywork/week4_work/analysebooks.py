from bookDAO import readbooks

books = readbooks()

total = 0
count = 0
for book in books:
    total += book['price']
    count += 1

print("Average price of ", count , " books is ", total/count)