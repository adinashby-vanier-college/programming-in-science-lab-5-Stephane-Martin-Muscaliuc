# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""    
    
    for i in range(n):
        if i == (n - 1) or i == 0:
            result += "*" * n + "\n"
        else:
            result += "*" + " " * (n - 2) + "*" + "\n"

    return result.strip()
    

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(n):
        for j in range(1, i + 2):
            result += str(j)
        result += "\n"

    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result =  ""

    sum = 0
    for i in range(n + 1):
        sum += i
    return sum




# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result =  ""

    for i in range(n):
        row = ""
        for j in range(2 * n - 1):
            if j < n - i - 1 or j > n + i - 1:
                row += " "
            else:
                row += "*"
        result += row.rstrip()
        if i < n - 1:
            result += "\n"
    return result.rstrip()


    
