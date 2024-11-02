import argparse
import sys

import file_browsing


def main():
    days=["pn", "wt", "śr", "czw", "pt", "sob", "nd"]

    # create args parser
    parser = argparse.ArgumentParser(
        description="""Script for reading/writing CSV files in structure of catalogues [miesiąc]/[dzień]/[pora_dnia].
                        Script performs only one type of action per run, it's not possible to write AND read at the same time.
                        If you try to read data from directories/files that do not exist, you will be notified, default value of 0 will be used
                        to calculate sum but the directory/file will NOT be created."""
    )

    parser.add_argument(
        '-m', '--miesiace',
        nargs='+',
        help="Insert any number of polish month names.",
        required=True
    )

    parser.add_argument(
        '-d', '--dni',
        nargs='+',
        help="""Insert the same amount of days or days ranges (day1-day2) as you did for months.
                Available day names are [pn, wt, śr, czw, pt, sob, nd].""",
        required=True
    )

    parser.add_argument(
        '-p', '--pory',
        nargs='+',
        help="For each given day insert the time of the day [r/w], default will be 'r'."
    )

    parser.add_argument(
        '-t', '--tworzenie',
        action='store_true',
        help="Specifies that you want to create files at given directories."
    )

    parser.add_argument(
        '-o', '--odczytywanie',
        action='store_true',
        help="Specifies that you want to read files from given directories."
    )

    args = parser.parse_args()

    # validate script parameters and turn them into triples from which directories will be created
    if (len(args.miesiace) != len(args.dni)):
        print("Amount of given months is not equal to amount of given days and days ranges.")
        sys.exit(1)

    if args.pory is None:
        args.pory = []

    triples_to_paths = []
    for index in range(len(args.miesiace)):
        days_in_range = []
        zakres = args.dni[index].split("-")

        try:
            ind_p = days.index(zakres[0])
            ind_k = days.index(zakres[max(0, len(zakres) - 1)])
        except ValueError:
            print("Unavailable name day was used, check 'help' for available day names.")
            sys.exit(1)

        if ind_p > ind_k:
            print("One of the given day ranges is incorrect.")
            sys.exit(1)
        
        while (ind_p <= ind_k):
            days_in_range.append(days[ind_p])
            ind_p += 1
        
        for day in days_in_range:
            if index < len(args.pory): #jezeli zostala podana pora dnia
                triples_to_paths.append((args.miesiace[index], day, args.pory[index]))
            else:
                triples_to_paths.append((args.miesiace[index], day, "r"))

    # perfom choosen action on given directories
    if (args.tworzenie and args.odczytywanie):
        print("Can't write AND read from files, choose exactly one action.")
        sys.exit(1)
    elif args.tworzenie:
        file_browsing.create_files(triples_to_paths)
    elif args.odczytywanie:
        file_browsing.check_and_sum(triples_to_paths)
    else:
        print("Action on directories was not specified, choose exaclty one flag from -t and -o.")
        sys.exit(1)


if __name__ == "__main__":
    main()