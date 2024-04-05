# ECOR 1042 Lab 6 - Template for curve_fit function



# Remember to include docstring and type annotations for your functions



# Update "" with your name (e.g., Cristina Ruiz Martin)

__author__ = "Emily Causi"



# Update "" with your student number (e.g., 100100100)

__student_number__ = "101236902"



# Update "" with your team (e.g. T-102, use the notation provided in the example)

__team__ = "T-55"


#==========================================#

# Place your curve_fit function after this line

def curve_fit(characters: list[dict], attribute: str, degree: int) -> str:
    """ Return the string equation of the line of best fit for the calculated average of the "Health" attribute.
    
    characters is a dictionary list, attribute = "", degree >= 0
    
    >>> curve_fit([{"Stamina":3, "Luck": 0.62, "Health": 12, "Intelligence": 8}, {"Stamina": 2, "Intelligence": 2, "Health": 21, "Luck": 0.60}, {"Luck": 0.38, "Stamina": 3, "Health": 7, "Intelligence": 9}, {"Stamina": 3, "Luck": 0.10, "Health": 12, "Intelligence": 0}], "Stamina", 3)
    'y = -10.67x + 42.33'
    
    >>> curve_fit([{"Stamina":3, "Luck": 0.62, "Health": 12, "Intelligence": 7}, {"Stamina": 2, "Intelligence": 7, "Health": 21, "Luck": 0.60}, {"Luck": 0.38, "Stamina": 3, "Health": 7, "Intelligence": 9}, {"Stamina": 3, "Luck": 0.10, "Health": 12, "Intelligence": 7}], "Intelligence", 7)
    'y = -4.00x + 43.00'
    
    >>> curve_fit([{"Stamina":3, "Luck": 0.62, "Health": 12, "Intelligence": 8}, {"Stamina": 2, "Intelligence": 2, "Health": 21, "Luck": 0.60}, {"Luck": 0.38, "Stamina": 2, "Health": 7, "Intelligence": 9}, {"Stamina": 3, "Luck": 0.10, "Health": 12, "Intelligence": 0}], "Stamina", 2)
    'y = -2.00x + 18.00'
    
    """
    import numpy as np
    
    attribute_list = []
    health_list = []

    for character in characters:
        if character[attribute] not in attribute_list:
            attribute_list.append(character[attribute])
            health_list.append([character["Health"]])
        
        else:
            index = attribute_list.index(character[attribute])
            health_list[index].append(character["Health"])
    
    for i in range(len(health_list)):
        health_list[i] = np.mean(health_list[i])

    if len(attribute_list) <= degree:
        deg = len(attribute_list) - 1
    
    else:
        deg = degree
    
    attribute_list = np.array(attribute_list, dtype=float)
    health_list = np.array(health_list, dtype=float)

    coefficients = np.polyfit(attribute_list, health_list, deg)

    expression = "y = "
    
    for h in range(len(coefficients)):
        power = len(coefficients) - h - 1
        coefficient_string = f"{coefficients[h]:.2f}"
        
        if power > 1:
            expression += f"{coefficient_string}x^{power} + "
        
        elif power == 1:
            expression += f"{coefficient_string}x + "
       
        else:
            expression += coefficient_string

    expression = expression.rstrip(" + ")

    return expression


# Do NOT include a main script in your submission
