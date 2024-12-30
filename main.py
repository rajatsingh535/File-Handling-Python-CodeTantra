#Write a python program to print each line of file in reverse order 
filename = input("")
with open (filename, "r") as f:
  lines = f.readlines()
for line in lines:
  reversed_lines = line.strip()[::-1]
  print(reversed_lines)
