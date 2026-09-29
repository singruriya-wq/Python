list = [10, 20, 30, 40, 50] 
print("Original list:", list)

n = int(input("Enter element to remove: "))

if n in list:
    list.remove(n)
    print("Updated list:", list)
else:
    print("Element not found")
