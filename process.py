import sys
import json

def main(args):

    # Parse out the command-line arguments #
    props_path = args[1]

    # Read in the properties file #
    with open(props_path) as x:
        props = json.load(x)
    print(props)

    # Read data from SQL table #

    # Process data to get necessary information #

    # Graph the data(matplotlib) #
    
    # Exit job when finished without error #
    sys.exit(0)
    # put everything in a try-catch
    

if __name__ == '__main__':
    main(sys.argv)
