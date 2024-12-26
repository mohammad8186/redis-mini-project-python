from Cli.actions.utils.argParser import ArgParser
from Cli.actions.Actions import Action, Actions
class CLI():
    def __init__(self):
        self._argParser = ArgParser()
        self._args = self._argParser.get_args()
        self._parser = self._argParser.parser
        self._action = Action()
        
    
    def execute(self):
        
        if self._args.command == str(Actions.CREATE):
            self._action.create(self._args.passwordName, " ".join(self._args.description), self._args.key, self._args.expiration)
        
        elif self._args.command == str(Actions.LIST):
            self._action.list()
        
        elif self._args.command == str(Actions.READ):
            self._action.read(" ".join(self._args.passwordName))
        
        elif self._args.command == str(Actions.UPDATE):
            self._action.update(" ".join(self._args.passwordName), self._args.key)
        
        elif self._args.command == str(Actions.DELETE):
            self._action.delete(" ".join(self._args.passwordName))
        
        elif self._args.command == str(Actions.REMAIN):
            self._action.get_remaining_time(" ".join(self._args.passwordName))
        
        else:
            self._parser.print_help()
