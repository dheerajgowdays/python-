def compound_interest(p, r, t):
    return p * ((1 + r / 100) ** t) - p


def main():
    try:
        p = float(input("Enter Amount: "))
        r = float(input("Enter Rate (%): "))
        t = float(input("Enter Time (years): "))
    except ValueError:
        print("Error: Inputs must be numeric")
        return

    if p <= 0:
        print("Error: Amount must be greater than zero")
        return
    if r < 0:
        print("Error: Rate cannot be negative")
        return
    if t <= 0:
        print("Error: Time must be greater than zero")
        return

    ci = compound_interest(p, r, t)
    print("Compound Interest:", round(ci, 2))


if __name__ == "__main__":
    main()
