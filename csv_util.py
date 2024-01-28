import csv
import os

FILE_KEYS = ['device', 'timestamp', 'type', 'x', 'y', 'z']

def save_to_csv(file_name, data):
    try:
        # Check if file exists and is not empty
        if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
            # Open the file in append mode
            mode = 'a'
        else:
            # Open the file in write mode
            mode = 'w'

        with open(file_name, mode) as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # If file is opened in write mode, write the header
            if mode == 'w':
                csv_writer.writerow(FILE_KEYS)
            
            # Write the data
            for row in data:
                # check data format
                if not isinstance(row, dict):
                    continue
                # check if all keys are present
                if not all(key in row for key in FILE_KEYS):
                    continue
                
                row_values = list(row.values())
                csv_writer.writerow(row_values)

    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# data in format
# @device: device id
# @timestamp: time of data
# @type: type of sensor
# @x: value of x-axis
# @y: value of y-axis
# @z: value from z-axis