while True:
    cnt = int(input('Введите число:'))
    if (cnt < 1) | (cnt > 100):
        print('Число вне диапазона')
        exit()
        
    rem = cnt % 10
    basestr = 'студент'
    if (rem in range(5,10)) | (rem == 0) | (cnt in range(10,21)):
        basestr += 'ов'
    else: 
        if rem in range(2,5): 
            basestr += 'а'
    print( cnt,basestr)