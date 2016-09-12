import sys

from sibyl.actions import ACTIONS

def print_usage():
    print "Usage: sibyl <command>\n"

    print "Available commands: "
    for act, act_cls in ACTIONS.iteritems():
        print "\t" + act + "\t" + act_cls.desc

        
if len(sys.argv) < 2:
    print_usage()
    
    exit(0)
    
action = sys.argv[1]

if action not in ACTIONS:

    guessed = [act_name for act_name in ACTIONS.itervalues() if act_name.startswith(action)]

    if len(guessed) == 1:
        action = guessed[0]
    else:
        if len(guessed) == 0:
            print "Unknown action: %s" % action
            print_usage()
        else:
            print "Ambiguous action: %s" % " ".join(guessed)

        exit(-1)

ACTIONS[action](sys.argv[2:]).run()
