# age = input('please enter your age: ')

# if int(age) >= 18:
#     print('adult')
# elif int(age) >= 6:
#     print('teenager')
# else:
#     print('kid')


def compare(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA == varB:
            print('equal')
        else:
            print('smaller')


a = 'hello'
b = 3
c = 5

# compare(a, b)
# compare(b, c)


def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    """
    if n > 21:
        return abs(n-21) * 2
    else:
        return abs(n-21)


# print(diff21(19))
# print(diff21(21))
# print(diff21(25))


def cigar_party(cigars, is_weekend):
    """
    When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
    """
    return 40 <= cigars <= 60 or is_weekend and cigars >= 40

    # if is_weekend and cigars >= 40:
    #     return True
    # else:
    #     return 40 <= cigars <= 60
    #     if 40 <= cigars <= 60:
    #         return True
    #     else:
    #         return False


# print(cigar_party(30, False))  # False
# print(cigar_party(50, False))  # True
# print(cigar_party(70, True))  # True


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


# countdown(5)

def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    return fabonacci(n-2) + fabonacci(n-1)


# print(fabonacci(6))
# print(fabonacci(2))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n


print(factorial(3))
