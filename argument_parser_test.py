import utility
import sys

options = [{"argument_name": "x", "require": True, "help_string": "this is simple","default_value": "xx", "custom_name": "X",
"action": "store", "constant_value":"sss", "data_type": str}]
PROG = sys.argv[0]
DESCRIPTION = """
            this is a testing program
            -------------------------
            this is a testing program
            """
program_info = {"program_name": PROG, "description": DESCRIPTION}


obj = utility.CreateArguments(options, program_info)
ops = obj.create_cli_arguments()

print(ops)
