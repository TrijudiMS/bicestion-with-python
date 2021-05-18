nilai_c = []
temp = count = c_now = c_past = 0
c = 0
toleransi_error = 0


### function yang diketahui
def f(x):
    return (pow(x, 3) + (4 * pow(x, 2)) - 10)
    #return (pow(x, 3) + (2 * pow(x, 2)) + (3 * x)- 4)


def cek_konvergen(x_now, x_past):
    global toleransi_error

    selisih = x_now - x_past

    if c_now < c_past:
        toleransi_error += 1

    if toleransi_error == 3:
        print('toleransi_error sudah mencapai nilai ke-3, mulai pengecekan konvergen')
        print(selisih, ' < 10^-5')
        if selisih <= 0.000099:
            print('konvergen')
            exit(0)
        else:
            print('belum konvergen')
    print('toleransi_error : ', toleransi_error)


def bisection(a, b):
    global c_now, c_past, temp, count, nilai_c, c
    count += 1

    if count >= 2:
        temp = c

    c = (a + b) / 2
    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~ NILAI C~~~~~~~~~~~~~~~~~~~~~~~~~~~ : ', c)
    f_a = f(a)
    f_b = f(b)
    f_c = f(c)
    
    print('a = {}\nb = {}\nc = {}'.format(a,b,c))
    print('f({}) : {}\nf({}) : {}\nf({}) : {}\n'.format(a, f_a, b, f_b, c, f_c))

    if (f_a * f_c < 0):
        a = a
        b = c
    elif (f_b * f_c < 0):
        a = c
        b = b

    nilai_c.append(c)
    print('new interval is [{}, {}]'.format(a, b))
    print(('=') * 20)

    if count == 1:
        c_now = c
    elif count >= 2:
        c_past = temp
        c_now = c
        
        cek_konvergen(c_now, c_past)

    if count == 1000:
        quit()

    return (a, b)


## memasukkan nilai interval
a = int(input('value interval from : '))
b = int(input('value interval to: '))

i = 0
while True:
    i += 1
    print((('=') * 20), 'iterasi ke ', i, ('=') * 20)
    a, b = bisection(a, b)

print('nilai C keseluruhan')
print(nilai_c)
