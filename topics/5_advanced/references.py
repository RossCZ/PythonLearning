def list_reference_example():
    def reassign(lst):
        print("reasign")
        lst = [0, 1]

    def append(lst):
        print("append")
        lst.append(1)

    lst = [0]
    print(lst)
    reassign(lst)
    print(lst)
    append(lst)
    print(lst)


def object_state_example():
    class Hrnek():
        def __init__(self, vyska, prumer):
            self.vyska = vyska
            self.prumer = prumer
            self.barva = ""

        def __str__(self):
            return f"v={self.vyska}, d={self.prumer}, color={self.barva}"

    def obarvi_hrnek(hrnek, barva):
        hrnek.barva = barva
        print(hrnek)

    def zvetsi_hrnek(hrnek):
        hrnek.vyska *= 2
        hrnek.prumer *= 3
        print(hrnek)

    def vypocti_objem(h, d):
        h = 10
        objem = h * 3.14 * d / 4
        return objem

    h1 = Hrnek(1, 1)
    h2 = Hrnek(2, 2)

    o1 = vypocti_objem(h1.vyska, h1.prumer)
    print(f"objem = {o1}")

    obarvi_hrnek(h1, "zluta")
    obarvi_hrnek(h2, "zelena")

    zvetsi_hrnek(h1)
    zvetsi_hrnek(h2)


# driver code
list_reference_example()
object_state_example()
