
#DAY 1

def day1_1(l1, l2):
    
    sumDis = 0
    i = 0
    iniLen = len(l1)

    while(i <= (iniLen - 1)):
        
        min1 = min(l1)
        min2 = min(l2)

        dis = abs(min1 - min2)

        sumDis = sumDis + dis
        
        l1.remove(min1)
        l2.remove(min2)
        
        i = i + 1

    return sumDis

def day1_2(l1, l2):
    
    res = 0

    i = 0
    iniLen = len(l1)

    while(i <= (iniLen - 1)):
        
        cont = 0

        value = l1[0]
        
        for e in l2:

            if(e == value):
                cont = cont + 1

        res = res + (value * cont)
        
        l1.remove(value)
        
        i = i + 1

    return res


def main():

    l1 = []
    l2 = []
    
    #input por consola

    '''
    print("Input:")

    while True:
        line = input()
            
        if line.strip() == "":  # If the next line is empty
            break
            
        col1, col2 = map(int, line.split())  # Split and parse to int
            
        l1.append(col1)
        l2.append(col2)
    
    '''

    #file
    
    with open("input.txt", "r") as file:

        for line in file:
        
            col1, col2 = map(int, line.split())  # Dividir y convertir a enteros
        
            l1.append(col1)
            l2.append(col2)

    #res = day1_1(l1, l2)

    res = day1_2(l1, l2)

    print("output: ",res)

main()