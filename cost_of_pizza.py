# This program was created by Larry Nkengbeza
# Created November 2020
# THe program is to calculate the cost of a pizza per diameter

import hst_constant


def main():

    # This function calculates the cost of a pizza

    # Input

    diameter = int(input("Enter the diameter of the pizza you would " +
                         "Like (Inch): "))
    # Process
    sub_total = hst_constant.Labor + hst_constant.Rent + \
        (diameter * hst_constant.Cost_Per_Inch)
    total = sub_total + (sub_total * hst_constant.HST)

    # Output

    print("")
    print("The cost for a {0} pizza is: ${1:,.2f}"
        .format(diameter, total))


if __name__ == "__main__":
    main()
