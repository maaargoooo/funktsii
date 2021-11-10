from module import*
while True:
    print("Funktsioonid".center(50"+"))
    v=input("arithmetic- A,\nis_year_leap-Y")
    if v.upper()=="A":
        a = float(input("Arv 1:"))
        b = float(input("Arv2:"))
        c = input("Tehe:")
        rezult=arithmetic(a,b,c)
        print(rezult)
    elif v.upper()== "Y":
        rezult=is_year_leap(int(input("Sisesta aasta:")))
        print(rezult)