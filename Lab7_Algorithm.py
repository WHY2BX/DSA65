def summation_ver1(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print (result)

def summation_ver2(n):
    result = (n*(n+1))/2
    print (result)

summation_ver1(100)
summation_ver2(100)
