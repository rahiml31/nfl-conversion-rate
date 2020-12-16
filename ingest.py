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

        # Push data to SQL table #
        print('Ingesting cleaned data to SQL table.')
        connection = sqlite3.connect(props['database_name'])
        data.to_sql(props['table_name'], connection, index=True)
        print('Finished ingeting the data.')

        # Read data from SQL table #
        raw_data = pd.read_sql('select * from play_data;', connection)

        # Clean the data and get the necessary columns only #
        cleaned_data0 = raw_data[props['data_columns']]
        cleaned_data1 = cleaned_data0[cleaned_data0.Down.eq(3)]
        print(cleaned_data1.head(10))

        # Process data to get necessary information #
        short = cleaned_data1[cleaned_data1.ToGo.lt(3)]
        medium = cleaned_data1[cleaned_data1.ToGo.between(4, 7)]
        long = cleaned_data1[cleaned_data1.ToGo.gt(8)]
        

        # Graph the data(matplotlib) #

    except Exception as e:
        print('There was an issue ingesting the data into the SQL table.', e)
    else:
        sys.exit(0)    


if __name__ == '__main__':
    main(sys.argv)
