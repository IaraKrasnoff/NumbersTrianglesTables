"""
TableUtilities - Python equivalent of Java TableUtilities class
Contains functions for generating formatted multiplication tables using loops
"""


def get_multiplication_table(table_size):
    """
    Return formatted multiplication table of specified size
    Args:
        table_size: Dimensions of the square multiplication table
    Returns:
        String representation of formatted multiplication table
    """
    result = ""
    for i in range(1, table_size + 1):
        add_string = ""
        for j in range (1, table_size + 1):
            add_string += f'{str(i*j):>3}'+ " |"  
        result += add_string +"\n"
    return result


def get_small_multiplication_table():
    """
    Return formatted 4x4 multiplication table
    Returns:
        String representation of 4x4 multiplication table
    """
    result = ""
    return get_multiplication_table(5)


def get_large_multiplication_table():
    """
    Return formatted 10x10 multiplication table
    Returns:
        String representation of 10x10 multiplication table
    """
    result = ""
    return get_multiplication_table(10)    

print(get_small_multiplication_table())
print(get_large_multiplication_table())