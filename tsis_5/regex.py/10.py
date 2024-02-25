import re

def camel_to_snake(camel_str):
     components = re.findall("[A-Z][^A-Z]*",camel_str)
     return  '_'.join(x.lower() for x in components[0:])

camel_case_string = "HelloWorldPython"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)




