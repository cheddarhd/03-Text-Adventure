import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)




def main():
    game = {}
    with open('thegame.json') as json_file:
        game = json.load(json_file)

def render(game,current):
    ''' Displays the current room '''

    print('You are in the ' + game['rooms'][current]['name'])
    print(game['rooms'][current]['desc'])

def getInput():
    ''' Asks the user for input and returns a stripped, uppercase version of what they typed '''

    response = input('What would you like to do? ').strip().upper()
    return response


def update(response,game,current):
    ''' Process the input and update the state of the world '''
    for e in game['rooms'][current]['exits']:
        if response == e['verb']:
            current = e['target']
    return current

    current = 'Starting place'


    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()