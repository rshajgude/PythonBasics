
# lambda is a 1 line function and you can create it while using OR
# create a lambda function give a name to it and use that name
# Note it lambda is more similar to macros in C language

square_it=lambda a : a*a

print(square_it(5))



# here buitiful line function name takes parameter and repeat passed character
buitiful_line=lambda c : print(60*c)

buitiful_line('^')

# here buitiful line function name takes parameter and repeat passed character
buitiful_line_2=lambda c , n=100 : print(n*c)
# default repeatation is set to 60 , if number is provided then its used else its always 60 by default

buitiful_line_2('-', 10)
buitiful_line_2(('-'))