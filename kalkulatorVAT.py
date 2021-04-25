# Kalkulator wykonany na potrzeby pracy grupwej na zajęcia z "Narzędzia do automatyzacji budowy oprogramowania"
# Mariusz Szmyt
import math
import linecache

print('________________Oto kalkulator podatku VAT!_________________')
print('1 - Dodawanie kwot')
print('2 - Odejmowanie kwot')
print('3 - Obliczanie podatku od podanych kwot')
print('4 - Obliczanie kwoty netto')
print('____________________________________________________________')


def kalkulator():

    print('------------------------------------------------------------')
    wybor = (input('Wybierz działanie '))

    def wybor1():

        try:

            int(wybor)

        except ValueError:
            print("Niedozwolony wybór")
            kalkulator()

    wybor1()


    def Calc():

        liczb1 = input("Podaj 1 liczbę ")

        def liczba1():   # sprawdzamy czy dane wejściowe nie są napisem

            try:

                float(liczb1)

            except ValueError:
                print("Niedozwolony znak - sprawdź dane wejściowe")
                print(liczb1)
                kalkulator()

        liczba1()

        liczb2 = input("Podaj 2 liczbę ")

        def liczba2():

            try:
                float(liczb2)

            except ValueError:
                print("Niedozwolony znak - sprawdź dane wejściowe")
                print(liczb2)
                kalkulator()



        liczba2()

        if wybor == '1':


            print('------------------------------------------------------------')

            v1 = float(liczb1)
            v2 = float(liczb2)

            print("Wynik to:", v1+v2, "netto, wynik brutto (23%) to:", round((v1+v2)*1.23,2))
            print("Podatek wynosi:", round(((v1+v2)*1.23)-(v1+v2),2))



        elif wybor == '2':


            print('------------------------------------------------------------')

            v1 = float(liczb1)
            v2 = float(liczb2)
            print("Wynik to:", v1-v2, "netto, wynik brutto (23%) to:", round((v1-v2)*1.23,2))
            print("Podatek wynosi:", round(((v1 - v2) * 1.23) - (v1 - v2),2))

        elif wybor == '3':

            v1 = float(liczb1)
            v2 = float(liczb2)
            print("Podatek 23% od pierwszej kwoty wynosi: ", round(v1*0.23,2))
            print("Podatek 23% od drugiej kwoty wynosi: ", round(v2* 0.23,2))

        elif wybor == '4':

            v1 = float(liczb1)
            v2 = float(liczb2)
            print("Pierwsza kwotta netto wynosi: ", round(v1/123*100,2))
            print("Druga kwota netto wynosi ", round(v2/123*100,2))


        else:
             print("Nie ma takiego działania")




        kalkulator()

    Calc()

kalkulator()


