
#DAY 1

def day2_1(cc):
    
    safeReports = len(cc)

    for i in range(0,len(cc)):
        
        c = cc[i]

        unsafe = False

        incr = True # true (default): increase, false: descrease

        for j in range(0,len(c) - 1):
            print(c[j])

            if c.index(c[j]) == 0:
                
                if abs(c[j] - c[j + 1]) >= 4:
                    unsafe = True
                    break

                elif(c[j] > c[j + 1]):
                    incr = False
            
            elif c.index(c[j]) == len(c) - 1:
                if (abs(c[j] - c[j - 1]) >= 4) or ((incr and (c[j] < c[j - 1])) or ((not incr) and (c[j] > c[j - 1]))):
                    unsafe = True
                    break
            
            else:

                if (abs(c[j] - c[j + 1]) >= 4) or ((incr and (c[j] < c[j + 1])) or ((not incr) and (c[j] > c[j + 1]))):
                    unsafe = True
                    break

            if unsafe:
                print(i, "is unsafe")
                safeReports = safeReports - 1
                break

    return safeReports

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

    cc = {{7,6,4,2,1}, {1,2,7,8,9}, {9,7,6,2,1}, {1,3,2,4,5}, {8,6,4,4,1}, {1,3,6,7,9}}
    

    print(day2_1(cc))

    #console input

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

    #file input
    
    '''
    with open("Day1_input.txt", "r") as file:

        for line in file:
        
            col1, col2 = map(int, line.split())  # Dividir y convertir a enteros
        
            l1.append(col1)
            l2.append(col2)

    print("Exercise 1")

    l1_1 = l1.copy()
    l2_1 = l2.copy()

    res1 = day1_1(l1_1, l2_1)
    
    print("output: ",res1)

    print("Exercise 2")

    res2 = day1_2(l1, l2)

    print("output: ",res2)


    '''

main()