def tambah () :
    print('\t1. PENJUMLAHAN')
    a = int(input('\tMASUKAN NILAI x = '))
    b = int(input('\tMASUKAN NILAI y = '))
    c = a+b
    print ('\tx + y = ',c)
    tanya()
def kurang () :
    print ('\t2. PENGURANGAN')
    a = int(input('\tMASUKAN NILAI x = '))
    b = int(input('\tMASUKAN NILAI y = '))
    c = a-b
    print ('\tx - y = ',c)
    tanya()
def kali () :
    print ('\t3. PERKALIAN')
    a = int(input('\tMASUKAN NILAI x = '))
    b = int(input('\tMASUKAN NILAI y = '))
    c = a*b
    print ('\tx * y = ',c)
    tanya()
def bagi () :
    print ('\t4. PEMBAGIAN')
    a = int(input('\tMASUKAN NILAI x = '))
    b = int(input('\tMASUKAN NILAI y = '))
    c = a/b
    print ('\tx / y = ',c)
    tanya()
def tanya() :
    tanya = input('Kembali Ke Menu Utama Kalkulator Iman Setiawan(Y/T)')
    if tanya=='Y' or tanya=='y':
        menu()
    elif tanya=='T' or tanya=='t':
        exit()
    else:
        print('\t\nMAAF INPUT YANG ANDA MASUKAN TIDAK DI KENAL')
        exit()
    
def menu () :
    print ('\t_______________________________________________')
    print ('\n\t        PROGRAM KALKULATOR IMAN SETIAWAN')
    print ('\t_______________________________________________')
    print ('\t1.PENJUMLAHAN')
    print ('\t2.PENGURANGAN')
    print ('\t3.PERKALIAN')
    print ('\t4.PEMBAGIAN')
    print ('\t______________________________________________')
    print ('\tSilahkan Pilih 1-4')
    print (' ')
    pil = input('\tMasukan Pilihan:')
    if pil=='1':
       tambah()
    elif pil=='2':
        kurang()
    elif pil=='3':
        kali()
    elif pil=='4':
        bagi()
    else:
        print('\n\tMaaf, input yang anda masukan salah,')
        print('\tCoba anda ulangi lagi yaa........\n')
menu()
tanya()
