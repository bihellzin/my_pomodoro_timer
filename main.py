#!/usr/bin/python3
"python3 path"

import time
import sys
import os
from playsound import playsound


def main(concentration: int = 25, short_break: int = 5,
         concentrations_before_long_break: int = 4,
         long_break: int = 30, total_cycles: int = 2):
    '''
    The main function of the app
    '''

    for i in range(total_cycles):
        for j in range(concentrations_before_long_break):
            print_minutes(concentration, 'CONCENTRATION TIME')

            if j == concentrations_before_long_break - 1:
                break

            play_alarm('relax.mp3')
            print_minutes(short_break, 'SHORT BREAK')
            play_alarm('back_to_study.mp3')

        if i == total_cycles - 1:
            clear_terminal()
            sys.stdout.write(final_output(concentration, short_break,
                                          concentrations_before_long_break, long_break,
                                          total_cycles))

        else:
            play_alarm('relax.mp3')
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
        clear_terminal()
        string_minutes = str(i - 1)
        sys.stdout.write(type_of_minute + '\n' + str(minutes) + ':00')

        for j in range(59, -1, -1):
            clear_terminal()
            string_seconds = str(j)

            if len(string_seconds) == 1:
                sys.stdout.write(type_of_minute + '\n' + string_minutes + ':' + '0' +
                                 string_seconds)

            else:
                sys.stdout.write(type_of_minute + '\n' +
                                 string_minutes + ':' + string_seconds)

            sys.stdout.flush()
            time.sleep(1)


def final_output(concentration: int, short_break: int, concentrations_before_long_break: int,
                 long_break: int, total_cycles: int):
    """
    This function will print a message when the cycle finishes
    """
    total_concentration = concentration * (total_cycles * concentrations_before_long_break)

    total_minutes = total_concentration + (long_break * (total_cycles - 1) + short_break \
                    * ((concentrations_before_long_break - 1) * total_cycles))

    output = 'The whole cycle is over.\n' \
    'You\'ve had {} minutes of concentration\n' \
    'The whole cycle took {} minutes to finish'.format(total_concentration, total_minutes)

    return output


def clear_terminal():
    """
    This function clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the terminal


def play_alarm(file: str):
    """
    This function plays the mp3 file named alarm.mp3
    """
    playsound(file)


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
