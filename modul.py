def arithmetic(a:float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var: Märamata tüüb
    """
    if c== "+":
        r=a+b 
    elif c== "-":
        r=a-b
    elif c== "*":
        r=a*b
    elif c== "/":
        if b!= :
            r=a/b
        else:
            r="Div/0"
        else:
            r="Tundmatu sym"
        return r

def is_year_leap(aasta: int):
    """ Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool:Funktsiooni vastus loogilise formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus
def square(kv:float):
    return