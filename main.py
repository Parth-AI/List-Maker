tasks = ['']
task1 = ""
print("\nwrite 'no' if you are done creating your list.")

while(tasks[-1] != "no"):
     task1 = input("Enter Item ")
     tasks.append(task1)

print("\nYour List Is:")

for i in tasks:
     if(i != "no"):
          print("\t"+i)