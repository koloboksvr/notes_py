number_of_worlds = 0
with open(r'SampleFile.txt' ,'r') as file :
    data = file.read()
    lines = data.split()
    for word in lines:
        if not word.isnumeric():
            number_of_worlds += 1
print(number_of_worlds)