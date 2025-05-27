# LABB 2
# Sebastijan Babic
# 2024 - 31 - 01

q = [-2,1,0,0,1]
p = [2,0,1]
p0 = [2,0,1,0]
q0 = [0,0,0]
#### uppgift 1 ###############################################

def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string


poly_to_string(q)








#### uppgift 2 ##############################################
## a) #######################################################
def drop_zeros(p_list):
    '''
    Returns a list without a zero in the end, function goes through a list and stops
    when a zero isn't in the way or if the list is empty'
    '''
    while p_list and p_list[-1] == 0:
        p_list.pop() # Removes the zero once a zero is found
    return p_list 

drop_zeros(p)


## b) ######################################################
def eq_poly(p_list, q_list):
    '''
    Sets two polynomial-lists at equality and returns bool True or False depending on if
    the polynomials are equal.
    '''
    p_list = drop_zeros(p_list) # Gets rid of a zero using the function drop_zeros
    q_list = drop_zeros(q_list)
    if p_list == q_list:
        return True
    else: 
        return False 
    
eq_poly(p,q)






####  uppgift 3 ##############################################
def eval_poly(coefficients, x):
    """
    Evaluates a polynomial at a given point x using Horner's algorithm.
    """
    result = coefficients[-1]  # Start with the last coefficient (highest degree term)

    # Iterate from the second-to-last coefficient backwards to the first
    for coefficient in reversed(coefficients[:-1]):
        result = result * x + coefficient

    return result


eval_poly(q, -2)

# ChatGPT used here for the 'reversed' function in order to simplify the function eval_poly 






#### uppgift 4 ###############################################
## a) ########################################################
def neg_poly(p_list):
    neg_p_list = [] # Creates list to save the negated p_list
    
    for coeff in p_list: # Iterates through every coefficient in p_list
        neg_p_list.append(-1 * coeff) # Negates by multiplying every coeff by -1
        
    return neg_p_list

neg_poly(p)


## b) ########################################################
def add_poly(p_list, q_list):
    add_poly_list = []  # Creates list to save the added lists
    max_length = max(len(p_list), len(q_list))
    
    for i in range(max_length):
        if i < len(p_list) and i < len(q_list):
            # p_list & q_list index i
            add_poly_list.append(p_list[i] + q_list[i])
        elif i < len(p_list):
            # p_list index i
            add_poly_list.append(p_list[i])
        elif i < len(q_list):
            # q_list index i
            add_poly_list.append(q_list[i])

    return add_poly_list

# Test the function
print(add_poly([2, 0, 1, 1], [1, 1, 1]))


## c) ########################################################
def sub_poly(p_list, q_list):
    sub_poly_list = []  # Creates list to save the added lists
    max_length = max(len(p_list), len(q_list))
    
    for i in range(max_length):
        if i < len(p_list) and i < len(q_list):
            # p_list & q_list index i
            sub_poly_list.append(p_list[i] - q_list[i])
        elif i < len(p_list):
            # p_list index i
            sub_poly_list.append(p_list[i])
        elif i < len(q_list):
            # q_list index i
            sub_poly_list.append(q_list[i])

    return sub_poly_list

print(add_poly([2, 0, 1], [1, 1, 1, 1, 1]))


#### uppgifft 5 ##############################################
# Following should be included in the function poly_to_string:
# * Empty list = 0
# * Terms with coeff 1 to be written without the 1
# * Terms with coeff -1 to be written as -x
# * Terms with coeff 0 not to be written
# * An empty list to be writen as 0
def poly_to_string(p_list):
    if not p_list:  # Check for empty list
        return '0'
    
    terms = []
    degree = len(p_list) - 1  # Start from the highest degree

    for coeff in reversed(p_list):  # Read from highest degree to lowest
        if coeff == 0:
            degree -= 1
            continue  # Skip terms with a coefficient of 0

        if degree == 0:
            terms.append(str(coeff))
        elif coeff == 1:
            if degree == 1:
                terms.append('x')
            else:
                terms.append('x^' + str(degree))
        elif coeff == -1:
            if degree == 1:
                terms.append('-x')
            else:
                terms.append('-x^' + str(degree))
        else:
            if degree == 1:
                terms.append(str(coeff) + 'x')
            else:
                terms.append(str(coeff) + 'x^' + str(degree))

        degree -= 1

    if not terms:  # Check if terms is empty after going through all coefficients
        return '0'
    # Did not succeed in making a readable version for whatever reason so ChatGPT added the final_string = ...
    final_string = ' + '.join(terms[::-1])  # Reverse to start from the lowest degree
    return final_string

poly_to_string(p)
print(poly_to_string([1,1,1]))