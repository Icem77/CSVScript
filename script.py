import argparse
import sys

def main():
    dni = ["pn", "wt", "śr", "czw", "pt", "sob", "nd"]

    parser = argparse.ArgumentParser(
        description="Skrypt do czytania i pisania do plików CSV w struktorze katalogów [miesiąc]/[dzień]/[pora_dnia]"
    )

    parser.add_argument(
        '-m', '--miesiace',
        nargs='+',
        help="Podaj dowolną liczb miesięcy",
        required=True
    )

    parser.add_argument(
        '-d', '--dni',
        nargs='+',
        help="Podaj tyle samo dni lub ich zakresów (dzien1-dzien2) ile zostało podanych miesięcy",
        required=True
    )

    parser.add_argument(
        '-p', '--pory',
        nargs='+',
        help="Dla kazdego z wcześniej podanych dni podaj porę [r(rano)/w(wieczór)], domyslnie pora zostanie ustawiona na 'r'"
    )

    args = parser.parse_args()

    if (len(args.miesiace) != len(args.dni)):
        print("Liczba podanych miesięcy nie jest zgodna z liczbą podanych dni lub ich zakresów")
        sys.exit(1)

    if args.pory is None:
        args.pory = []


    krotki_na_sciezki = []
    for index in range(len(args.miesiace)):
        dni_z_zakresu = []
        zakres = args.dni[index].split("-")
        ind_p = dni.index(zakres[0])
        ind_k = dni.index(zakres[max(0, len(zakres) - 1)])
        
        while (ind_p <= ind_k):
            dni_z_zakresu.append(dni[ind_p])
            ind_p += 1
        
        for dzien in dni_z_zakresu:
            if index < len(args.pory): #jezeli zostala podana pora dnia
                krotki_na_sciezki.append((args.miesiace[index], dzien, args.pory[index]))
            else:
                krotki_na_sciezki.append((args.miesiace[index], dzien, "r"))


    for krotka in krotki_na_sciezki:
        print(krotka)



if __name__ == "__main__":
    main()