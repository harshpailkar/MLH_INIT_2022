a = []
num = int(input("Enter the total number of elements : "))
for i in range(num):
    value = int(input("Enter the %d element of the list : " %i))
    a.append(value)

i = 0
while(i < num -1):
    j = 0
    while(j < num - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
        j = j + 1
    i = i + 1

print("The Sorted List in Ascending Order is : ", a)
