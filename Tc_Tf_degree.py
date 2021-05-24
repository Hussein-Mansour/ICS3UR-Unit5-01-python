#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sun/May23/2021
# This program is a fahrenheit program


def fahrenheit():
    # this function lets you enter in a temperature in degrees celsius
    # prints out what that temperature is in degrees Fahrenheit

    # input
    Tc = input("Enter the temperature in degrees celsius(℃):")

    # process & output
    try:
        Tc_int = int(Tc)

        Tf = (9/5)*Tc_int+32
        print("\nThe temperature in degrees Fahrenheit is : {0}℉".format(Tf))

    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
