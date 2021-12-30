#WAP to print all positive numbers in range
start=int(input("Enter the start of range : "))
end=int(input("Enter the end og range : "))
# itering each number in list
for num in range(start,end+1):
    #checki.ng condition
    if num >= 0:
        print(num,end = " ")
