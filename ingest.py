import pandas as pd
import sys
import json
import sqlite3

def main(args):

    try:
        # Parse out the command-line arguments #
        props_path = args[1]
        data_path = args[2]

        # Read in the properties file #
        with open(props_path) as x:
            props = json.load(x)

        # Read in the data #
        data = pd.read_csv(data_path)

        # Clean the data and get the necessary columns only #
        cleaned_data0 = data[props['data_columns']]
        cleaned_data1 = cleaned_data0[cleaned_data0.Down.eq(3)]

        # Push data to SQL table(sqllite3) #
        print('Ingesting cleaned data to SQL table.')
        connection = sqlite3.connect(props['database_name'])
        cleaned_data1.to_sql(props['table_name'], connection, index=True)
    except:
        print('There was an issue ingesting the data into the SQL table.')
    else:
        # Exit job when finished without error #
        print('Finished ingeting the data, exiting now.')
        sys.exit(0)    

if __name__ == '__main__':
    main(sys.argv)
