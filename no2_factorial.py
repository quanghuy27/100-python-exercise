'''
Viết một chương trình có thể tính giai thừa của một số cho trước. 
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
'''
#khử đệ quy
def factorial(n):
    factorial = 1
    if (n == 0 or n == 1):
        return 1
    else:
        for i in range(2, n + 1 ):
            factorial = factorial * i
        return factorial

#đệ quy
def factorialRecursion(n):
    if (n == 0): return 1
    else: 
        return n * factorialRecursion(n-1)

n = int(input("Nhập số nguyên dương n = "))
print("Giai thừa của", n, "là", factorial(n))
