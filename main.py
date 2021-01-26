#!/usr/bin/env python3

def check_numbers(dict):
    for k, v in dict.items():
        try:
            dict.update({k: float(v)})
        except:
            print(
                f'''\n ***Parameter \'{k}\' has invalid value \'{v}\'. It must be a valid number. Please input again***\n''')
            return 0
    return 1


def calculate_metric_to_imperial(w, p, r):
    iw = w/10/2.54
    id = (iw*p/100*2) + r
    ir = r

    return round(id, 2), round(iw, 2), round(ir, 1)


def calculate_imperial_to_metric(d, w, r):
    mw = w * 2.54 * 10
    p = (d - r) / 2 * 2.54 * 1000 / mw
    mr = r

    return round(mw), round(p), round(mr, 1)


def input_metric_to_imperial():
    correct = False
    while not(correct):
        print('''Please type in values w,p,r

        Example:
        For tyre 265/85 R15

        w=265
        p=85
        r=15
            ''')

        my_dict = {}
        my_dict.update({"w": input("w: ")})
        my_dict.update({"p": input("p: ")})
        my_dict.update({"r": input("r: ")})

        correct = check_numbers(my_dict)
    return(my_dict)


def input_imperial_to_metric():
    correct = False
    while not(correct):
        print('''Please type in values d,w,r

        Example:
        For tyre 31 x 10.5 R15

        d=31
        w=10.5
        r=15
            ''')

        my_dict = {}
        my_dict.update({"d": input("d: ")})
        my_dict.update({"w": input("w: ")})
        my_dict.update({"r": input("r: ")})

        correct = check_numbers(my_dict)

    return(my_dict)


def main():
    print('''
    Please select:
    (1) Convert metric to imperial
    (2) Convert imperial to metric
    ''')

    choice = None
    while choice is None:
        my_choice = input()
        if my_choice in {"1", "2"}:
            choice = int(my_choice)
        else:
            print('Please type in 1 or 2')


    if choice == 1:
        d, w, r = calculate_metric_to_imperial(**input_metric_to_imperial())
        print(f'\nImperial dimensions are {d} x {w} R{r}')

    else:
        w, p, r = calculate_imperial_to_metric(**input_imperial_to_metric())
        print(f'\nMetric dimensions are {w} x {p} R{r}')

    input()


if __name__ == '__main__':
    main()
