# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Accessing tuple elements using indexing
my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

# Slcing
print("Sliced:", my_tuple[1:4])

# Iterating through a tuple
for lwtter in (my_tuple):
    print("Hello", letter)