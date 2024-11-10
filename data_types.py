#Create variables of each primitive data type
integervar = 10
floatvar = 30.5
stringvar = "Hello"
booleanvar = 'true'
# Arithmetic operations on int and float
int_sum = integervar + 5     
float_sum = floatvar + 3.5      
int_product = integervar * 2 
float_product = floatvar * 1.5  

# String concatenation
string_concat = stringvar + " World"

# Logical operations
logical_and = booleanvar and False
logical_or = booleanvar or False
logical_not = not booleanvar

#  Create a dictionary to store variables by type
variables_by_type = {
    "int": [integervar, int_sum, int_product],
    "float": [floatvar, float_sum, float_product],
    "str": [stringvar, string_concat],
    "bool": [booleanvar, logical_and, logical_or, logical_not]
}

# Display the dictionary
print("Variables by Type:")
for var_type, values in variables_by_type.items():
    print(f"{var_type}: {values}")
