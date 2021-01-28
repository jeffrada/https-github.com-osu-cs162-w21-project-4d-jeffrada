# Author: Adam Jeffries
# Date: 1/27/2021
# Description: A bubble sort that counts the number of comparisons and the number of exchanges
# made while sorting a list and returns a tuple of the values.

def bubble_count(a_list):
    """
    Sorts a_list in ascending order
    """
    comparison_count = 0
    exchange_count = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparison_count += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchange_count += 1
    return comparison_count and exchange_count


def insertion_count(a_list):
    """
    Sorts a_list in ascending order
    """
    comparison_count = 0
    exchange_count = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        comparison_count += 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            exchange_count += 1
        a_list[pos + 1] = value
