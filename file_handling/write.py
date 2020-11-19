msg = "hello world!"
file = open("newfile.txt","w")
amount = file.write(msg)
print(amount)
file.close()
