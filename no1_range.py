'''Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
'''
#range(stop) or range(start, stop[, step]): tạo 1 chuỗi các số tăng dần theo giá trị bắt đầu và kết thúc, step: khoảng cách giữa các số trong chuỗi
#str.join(sequence): nối các phần tử của sequence thành 1 dãy , ngăn cách bởi str

def findMultiplesOfNumber7(mylist):
    for i in range(2000,3201):
        if(i % 7 == 0 )and (i % 5 != 0):
            mylist.append(str(i))
    print(','.join(mylist))

list1 = []
findMultiplesOfNumber7(list1)
