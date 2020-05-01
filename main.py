#!/usr/bin/python3
"python3 path"

import time
import sys
import os


def main(concentration: int = 25, short_break: int = 5,
         concentrations_before_long_break: int = 4,
         long_break: int = 30, total_cycles: int = 2):
    '''
    The main function of the app
    '''

    os.system('cls' if os.name == 'nt' else 'clear')  # clear the terminal

    for i in range(total_cycles):
        for j in range(concentrations_before_long_break):
            print_minutes(concentration, 'CONCENTRATION TIME')

            if j == concentrations_before_long_break - 1:
                break

            print_minutes(short_break, 'SHORT BREAK')

        if i == total_cycles - 1:
            total_concentration = concentration * \
                (total_cycles * concentrations_before_long_break)

            total_minutes = total_concentration + (
                long_break * (total_cycles - 1) +
                short_break * ((concentrations_before_long_break - 1) * total_cycles))

            final_output = 'The whole cycle is over.\n' \
                           'You\'ve had {} minutes of concentration\n' \
                           'The whole cycle took {} minutes to finish'.format(
                               total_concentration, total_minutes)

            clear_lines(2)
            sys.stdout.write(final_output)

        else:
            print_minutes(long_break, 'LONG BREAK')


def print_manual():
    """
    If the user puts an incorrect argument or if he calls the \"help\" command
    this function will be called
    """
    print('blablabla')


def print_minutes(minutes: int, type_of_minute: str):
    """
    Print the minutes and seconds and the moment
    """

    for i in range(minutes, 0, -1):
        clear_lines(1)
        string_minutes = str(i - 1)
        sys.stdout.write(type_of_minute + '\n' + str(minutes) + ':00')

        for j in range(59, -1, -1):
            clear_lines(1)
            string_seconds = str(j)

            if len(string_seconds) == 1:
                sys.stdout.write(type_of_minute + '\n' + string_minutes + ':' + '0' +
                                 string_seconds)

            else:
                sys.stdout.write(type_of_minute + '\n' + string_minutes + ':' + string_seconds)

            sys.stdout.flush()
            time.sleep(1)


def clear_lines(lines: int):
    """
    This function clear the lines of the terminal
    """
    sys.stdout.write('\033[F\033[K' * lines) #'lines' is the number of lines that will be overwriten
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            main()

        else:
            MINUTES_OF_CONCENTRARION = int(sys.argv[1])
            MINUTES_OF_SHORT_BREAK = int(sys.argv[2])
            NUMBER_OF_CONCENTRATIONS_BEFORE_LONG_BREAK = int(sys.argv[3])
            MINUTES_OF_LONG_BREAK = int(sys.argv[4])
            TOTAL_NUMBER_OF_CYCLES = int(sys.argv[5])

            main(MINUTES_OF_CONCENTRARION, MINUTES_OF_SHORT_BREAK,
                 NUMBER_OF_CONCENTRATIONS_BEFORE_LONG_BREAK, MINUTES_OF_LONG_BREAK,
                 TOTAL_NUMBER_OF_CYCLES)

    except (ValueError, IndexError):
        print_manual()
