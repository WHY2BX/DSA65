def insertionSort(list, last):
    compare = 0
    current = 1
    while current <= last:
        hold = list[current]
        walker = current - 1
        compare += 1
        while walker >= 0 and hold < list[walker]:
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1 
        list[walker+1] = hold #insert ข้อมูลใน sorted list
        current += 1
        if walker < 0:
            compare -= 1
        print(list)
    print("compare :", compare)

def selectionSort(list, last):
    current = 0 
    compare = 0
    while current <= last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if list[walker] < list[smallest]:
                smallest = walker 
            walker += 1
            compare += 1
        #exchange (current, smallest)
        temp = list[current]
        list[current] = list[smallest]
        list[smallest] = temp
        current += 1
        print(list)
    print("compare : ", compare)
    
def bubbleSort(list, last):
    current = 0
    sorted = False
    compare = 0
    while current <= last and sorted is False:
        walker = last
        sorted = True 
        while walker > current:
            if list[walker] < list[walker-1]:
                sorted = False
                temp = list[walker]
                list[walker] = list[walker-1]
                list[walker-1] = temp
            walker -= 1
            compare += 1
        current += 1
        print(list)
    print("compare : ", compare)


insertionSort ([ 23 , 78 , 45 , 8 , 32 , 56 ,1], 6)
selectionSort ([ 23 , 78 , 45 , 8 , 32 , 56 ,1], 6)
bubbleSort ([ 23 , 78 , 45 , 8 , 32 , 56 ,1], 6)