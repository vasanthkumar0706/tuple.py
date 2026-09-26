data = ((10,20,30), (5,12,15,20,36), (2,4,6))

largest = data[]

for d in data:
    if len(d) > len(largest):
        largest = d 

        print("tuple with more numbers:", largest)
        print("number of numbers:", len(largest))