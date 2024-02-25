import re

def snake_to_camel(snake_str):
     components = snake_str.split('_')
     return components[0] + ''.join(x.title() for x in components[1:])

snake_case_string = "hello_world_python"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)


