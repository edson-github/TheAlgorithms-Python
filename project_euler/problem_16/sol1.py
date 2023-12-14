power = int(input("Enter the power of 2: "))
num = 2**power

string_num = str(num)

list_num = list(string_num)

print("2 ^",power,"=",num)

sum_of_num = sum(int(i) for i in list_num)
print("Sum of the digits are:",sum_of_num)
