file = open("SampleFile.txt")
lines = 0
words = 0
symbols = 0
for line in file:
    lines +=1
    words += len(line.split())
    symbols += len(line)
print("Lines:", lines)
print("Words:", words)
print("Symbol:", symbols)