# Program 1: Print Each Line of a File in Reverse Order
filename = input("")
with open(filename, "r") as f:
    lines = f.readlines()
for line in lines:
    reversed_lines = line.strip()[::-1]
    print(reversed_lines)
# Program 2: Copy Content from One File to Another File
# Method 1: Using a Loop to Read and Write Line by Line
fin = open("input4.txt", "r")
fou = open("output4.txt", "w")

for line in fin:
    fou.write(line)

fou.close()

data = open("output4.txt", "r")

for i in data:
    print(i, end="")

fin.close()
data.close()
# Method 2: Using read() to Copy the Entire File
with open("input4.txt", 'r') as fsrc:
    content = fsrc.read()

with open("output4.txt", 'w') as fdst:
    fdst.write(content)

with open("output4.txt", 'r') as fdst:
    for line in fdst:
        print(line, end="")
