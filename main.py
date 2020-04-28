#!/usr/bin/python3
"python3 path"

import time
import sys


def main(minutes_of_concentration: int = 25, minutes_of_short_break: int = 5,
         number_of_concentration_before_long_break: int = 4,
         minutes_of_long_break: int = 30, total_number_of_cycles: int = 2):
    '''
    The main function of the app
    '''
    for i in range(total_number_of_cycles):
        for j in range(number_of_concentration_before_long_break):
            print_minutes(minutes_of_concentration, 'CONCENTRATION TIME')

            if j == number_of_concentration_before_long_break - 1:
                break

            print_minutes(minutes_of_short_break, 'SHORT BREAK')

        if i == total_number_of_cycles - 1:
            total_minutes_of_concentration = minutes_of_concentration * \
            (total_number_of_cycles * number_of_concentration_before_long_break)

            total_minutes = total_minutes_of_concentration + (
                minutes_of_long_break * (total_number_of_cycles - 1) +
                minutes_of_short_break * ((number_of_concentration_before_long_break - 1) *
                                          total_number_of_cycles))

            final_output = 'The whole cycle is over.\n' \
                           'You\'ve had {} minutes of concentration\n' \
                           'The whole cycle took {} minutes to finish'.format(
                               total_minutes_of_concentration, total_minutes)

            sys.stdout.write('\r' + final_output)

        else:
            print_minutes(minutes_of_long_break, 'LONG BREAK')


def print_manual():
    """
    If the user puts an incorrect argument or if he calls the \"help\" command
    this function will be called
    """
    return


def print_minutes(minutes: int, type_of_minute: str):
    """
    Print the minutes and seconds and the moment
    """
    for i in range(minutes, 0, -1):
        sys.stdout.write('\r' + str(i) + ':00')
        string_minutes = str(i - 1)
        for j in range(59, -1, -1):
            string_seconds = str(j)

            if len(string_seconds) == 1:
                sys.stdout.write('\r' + type_of_minute + '\n' + string_minutes +
                                 ':' + '0' +string_seconds)

            else:
                sys.stdout.write('\r' + type_of_minute + '\n' + string_minutes +
                                 ':' + string_seconds)

            time.sleep(1)


if __name__ == "__main__":
    MINUTES_OF_CONCENTRARION = int(sys.argv[1])
    MINUTES_OF_SHORT_BREAK = int(sys.argv[2])
    NUMBER_OF_CONCENTRATIONS_BEFORE_LONG_BREAK = int(sys.argv[3])
    MINUTES_OF_LONG_BREAK = int(sys.argv[4])
    TOTAL_NUMBER_OF_CYCLES = int(sys.argv[5])

    main(MINUTES_OF_CONCENTRARION, MINUTES_OF_SHORT_BREAK,
         NUMBER_OF_CONCENTRATIONS_BEFORE_LONG_BREAK, MINUTES_OF_LONG_BREAK,
         TOTAL_NUMBER_OF_CYCLES)
