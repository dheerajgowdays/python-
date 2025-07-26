import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output.csv")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    try:
        with open(input_filename, "r", newline='') as infile:
            reader = csv.DictReader(infile)
            rows = []
            for row in reader:
                first, last = row["name"].split(',', 1)
                house = row["house"]
                rows.append({"first": first, "last": last, "house": house})

        with open(output_filename, "w", newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    except FileNotFoundError:
        print(f"Could not read {input_filename}")
        sys.exit(1)

main()
