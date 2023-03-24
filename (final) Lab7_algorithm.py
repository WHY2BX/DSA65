from time import time
import random

def summation_ver1(n): #Big-O --> n
    result = 0
    for i in range(1, n+1):
        result += i
    print (result)

def summation_ver2(n): #Big-O --> 1
    result = (n*(n+1))/2
    print (result)

def isintersect_n2(n):
    list_a = []
    list_b = []
    list_c = []
    intersector = []
    
    for i in range (n):
        list_a.append(random.randint(0,100))
        list_b.append(random.randint(0,100))
        list_c.append(random.randint(0,100))
    print(list_a, list_b, list_c)
    
    # for i in range (n):
    intersector = [i for i in list_a if i in list_b and i in list_c]
    print(intersector)
    print(bool(intersector))
        
def isintersect_n3(n):
    list_a = []
    list_b = []
    list_c = []
    intersector = []
    intersector_2 = []
    
    for i in range (n):
        list_a.append(random.randint(0,10))
        list_b.append(random.randint(0,10))
        list_c.append(random.randint(0,10))
    # print(list_a, list_b, list_c)

        intersector = [i for i in list_a if i in list_b]
        intersector_2 = [i for i in intersector if i in list_c]
    # print(intersector, intersector_2)
    print(bool(intersector is intersector_2))

    
    
#timing
def analyze_algo_ver1(n=1):
    stime = time() # record the starting time
    summation_ver1(n)
    etime = time() # record the ending time
    elapsed = etime-stime # compute the elapsed time
    print("execution time: ", elapsed)

def analyze_algo_ver2(n=1):
    stime = time() # record the starting time
    summation_ver2(n)
    etime = time() # record the ending time
    elapsed = etime-stime # compute the elapsed time
    print("execution time: ", elapsed)
    
def analyze_algo_intersec(n=1):
    stime = time() # record the starting time
    isintersect_n2(n)
    etime = time() # record the ending time
    elapsed = etime-stime # compute the elapsed time
    print("execution time: ", elapsed)
    
# analyze_algo_ver1(100)
# analyze_algo_ver1(1000)
analyze_algo_intersec(3)
# analyze_algo_intersec(1000)
# analyze_algo_intersec(10000)
# isintersect_n2(3)
# isintersect_n3(3)