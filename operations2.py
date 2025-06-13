# write in file using with()function
with open('codingal2.txt', 'w') as file2:
  file2.write("Hi! I am Penguin and I am 1 year old")
file2.close()

# split fule into words
with open('codingal2.txt', 'r') as file2:
  data = file2.readlines()
  print("Words in this file are...")
  for line in data:
    word = line.split()
    print (word)
file2.close()    
