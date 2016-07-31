import argparse

class CreateArguments:

"""
dict = {'argument_name':'name of the argument',
        'required':true/false,
        'help_string':'helpstring',
        'data_type': 'data type',
        'verbose': true/false,
        'default':'default value of the argument if nothing is provided',
        'custom_name': 'custome name provided to an argument',
        'action':'store/store_const/store_true/store_false/append/append_const/count',
        'constant_value':'any constant value if any of the const actions is specified'
        }
"""
def __init__(self, arguments_list, description):
    self.arguments_list = arguments_list
    self.description = description

def create_cli_arguments(self):
    parser = argparse.ArgumentParser(description=self.description)
    for options in self.arguments_List:
        argument_name = options.['argument_name']
        help_string = options.['help_string']
        data_type = options['data_type']
        default = options.get('dafault')
        custom_name = options.get('custom_name')
        action = options.get('action')
        constant_value = options.get('constant_value')
    
        



