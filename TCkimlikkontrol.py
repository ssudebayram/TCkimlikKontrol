tckn = ""
while True:
    tckn = input("kimlik no giriniz")
    if not tckn.isdigit():
        print("kimlik no rakamlardan oluşmalıdır")
    elif len(str(int(tckn))) != 11:
        print("kimlik no 11 haneden oluşmalıdır")
    else:
        tckn_int = int(tckn)
        ilk9 = tckn_int // 100
        son2 = tckn_int % 100
        tekler, ciftler = 0, 0
        i = 1
        while i <= 9:
            b = ilk9 % 10
            if i % 2:
                tekler += b
            else:
                ciftler += b
            ilk9 //= 10
            i += 1
        b10 = (tekler * 7 - ciftler) % 10
        b11 = (tekler + ciftler + b10) % 10
        if son2 == b10 * 10 + b11:
            print("kimlik doğru")
            break
        else:
            print("lütfen doğru bir kimlik giriniz")

print(tckn)