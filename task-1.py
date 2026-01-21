## problem statement-1
try:
    file = open('sample.txt','r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample1.txt' was not found.")
