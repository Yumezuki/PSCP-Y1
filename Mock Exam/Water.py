"""Water"""


def water(month):
    """Function"""
    price_a = float(input())
    limit_b = float(input())
    price_more_c = float(input())
    nt_limit_d = float(input())
    som = 0
    for _ in range(month):
        total = 0
        use_water = float(input())
        total += (use_water * price_a)
        print(total)
        if use_water > limit_b:
            total += (abs(use_water - limit_b) * price_more_c)
            print(total)
        if total <= nt_limit_d:
            total = 0
            print(total)
        som += total
    print("%.2f" %som)


water(int(input()))
