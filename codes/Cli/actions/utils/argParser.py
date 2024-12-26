import argparse
from Cli.actions.Actions import Actions
class ArgParser():
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Password Manager")
        subparsers = self._parser.add_subparsers(dest="command")

        
        new_parser = subparsers.add_parser(Actions.CREATE, help="Create a new password")
        new_parser.add_argument("-n", "--passwordName", type=str, help="Name of the new password")
        new_parser.add_argument("-c", "--description", type=str, nargs='+', required=True, help="Description of the new password")
        new_parser.add_argument("-key", type=str, help="key to be encrypted")
        new_parser.add_argument("-exp","--expiration", type=str, help="expiration time for the key (seconds)")

        
        show_parser = subparsers.add_parser(Actions.LIST, help="Show all passwords")

        
        select_parser = subparsers.add_parser(Actions.READ, help="Select a password")
        select_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to select")

       
        update_parser = subparsers.add_parser(Actions.UPDATE, help="Update a password")
        update_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to update")
        update_parser.add_argument("-key", type=str, help="new key value to be encrypted")
        
        delete_parser = subparsers.add_parser(Actions.DELETE, help="Delete a password")
        delete_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to delete")

        remain_parser = subparsers.add_parser(Actions.REMAIN, help="Get the remaining time untill a password expires")
        remain_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to get the remaining time of") 
    def get_args(self):
        args =  self._parser.parse_args()
        return args
    
    @property
    def parser(self):
        return self._parser

   