import argparse
import sys

def main(days=["pn", "wt", "śr", "czw", "pt", "sob", "nd"]):

    parser = argparse.ArgumentParser(
        description="Script for reading and writing CSV files in structure of catalogues [miesiąc]/[dzień]/[pora_dnia]."
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
        help="For each given day insert the time of the day [r(rano)/w(wieczór)], default will be 'r'."
    )

    args = parser.parse_args()

    if (len(args.miesiace) != len(args.dni)):
        print("Amount of months is not equal to amount of days/days ranges.")
        sys.exit(1)

    if args.pory is None:
        args.pory = []

    #preprocessing on script parameters to create file paths
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

    

if __name__ == "__main__":
    main()