class Action(object):

    name = "Name of the action"
    desc = "Description of the action"

    def __init__(self, cmd_line_args):
        pass
    
    def run(self):
        raise NotImplementedError("Abstract method")
