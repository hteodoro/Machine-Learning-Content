
####  LIST COMPREHENSIONS ####
sample = [2, 5, 8]
# This is how you construct a list comprehension
example_list = [item ** 2 for item in sample]
# Change to True to print
if False:
    print(example_list)

# without a list comprehension you'd need to do this
example_list = []
for item in sample:
    example_list.append(item ** 2)

#### LAMBDA FUNCTIONS ####
# Lambdas exist to provide a quick way to build up a function tha will not be used a lot
# They are really useful when working with Maps and Filters
lambda x : x ** 2

# This has the same functionality as the lambda above
def make_square(x):
    return x ** 2


#### MAP FUNCTIONS ####
# Map functions are used to re-define values from a specific element that can be looped
# We use lambda functions to make the process easier and not define a function
example_list = list(map(lambda x : x ** 2, sample))
# Change to True to print
if True:
    print(example_list)

# Otherwise we would need to do this:
example_list = []
for item in sample:
    example_list.append(make_square(item))
