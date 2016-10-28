import argparse


def sort():
    for slash in open("slash"):
        line = slash.strip().split("/")
        fo = open("Genscape.txt", "a")
        fo.write(line[2] + " ")
        fo.write(line[1] + " ")
        fo.write(line[3] + " ")
        fo.write(line[0] + "\n")
    fo.close()

    for slash in open("pipe"):
        line = slash.strip().split("|")
        fo = open("Genscape.txt", "a")
        fo.write(line[1] + " ")
        fo.write(line[0] + " ")
        fo.write(line[2] + " ")
        fo.write(line[3] + "\n")
    fo.close()

    for slash in open("csv"):
        line = slash.strip().split(",")
        fo = open("Genscape.txt", "a")
        fo.write(line[1] + " ")
        fo.write(line[2] + " ")
        fo.write(line[0] + " ")
        fo.write(line[3] + "\n")
    fo.close()

    with open("Genscape.txt", "r+") as f:
        lines = f.readlines()
        lines.sort(key=lambda x: x.split()[0] if len(x.split()) > 0 else None)
        f.seek(0)
        for line in lines:
            line = line.strip()
            print(line)
        f.writelines(lines)


def createCLI():
    parser = argparse.ArgumentParser(description='Show a list of books, alphabetical ascending by author\'s last name')

    parser.add_argument('--filter',
                        help='show subset of books, looks for the argument as a substring of any of the fields')

    parser.add_argument('--year', help='sort the books by year, ascending instead of default sort', action='store_true')

    parser.add_argument('--reverse', help='reverse sort', action='store_true')

    args = parser.parse_args()

    return args


def main():
    args = createCLI()

    if args.filter:
        with open("Genscape.txt") as f:
            for line in f:
                if args.filter in line:
                    line = line.strip()
                    print(line)

    elif args.reverse:
        with open("Genscape.txt", "r+") as f:
            lines = f.readlines()
            lines.sort(key=lambda x: x.split()[0] if len(x.split()) > 0 else None, reverse=True)
            f.seek(0)
            for line in lines:
                line = line.strip()
                print(line)

    elif args.year:
        with open("Genscape.txt", "r+") as f:
            lines = f.readlines()
            lines.sort(key=lambda x: x.split()[3])
            f.seek(0)
            for line in lines:
                line = line.strip()
                print(line)

    else:
        open("Genscape.txt", 'w').close()
        sort()


if __name__ == "__main__":
    main()
