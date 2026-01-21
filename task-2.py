## problem statement-2
try:
    with open('output.txt', 'w+') as file:
        t=input("Enter text to write to the file: ")
        file.write(t)
        print("data successfully written to output.txt")
        t1=input("Enter additional text to append to the file: ")
        file.write('\n'+t1)
        print("data successfully appended")
        print("final content of output.txt: ")
        file.seek(0)
        print(file.read())
except Exception as e:
    print(f"An error occurred: {e}")
