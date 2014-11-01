

# USAGE
#
#
#
#
#
#
#

import csv;

CLOSE_INDEX = 4;

def rate_to_trend(file_path):
  with open(file_path, 'rb') as opened_file:
    reader = csv.reader(opened_file, delimiter=' ', quotechar='|')
    iterator = reader.__iter__()

    # Handle header (for now simply ignore)
    header = iterator.next()
    prev_close_val = -1; 
    
    for idx, (date, data) in enumerate(reader):
      split_data  = data.split(',')
      close_value = split_data[CLOSE_INDEX]
      if prev_close_val != -1:
        if prev_close_val < close_value:
          trend = 1
        elif prev_close_val > close_value:
          trend = -1
        else:
          trend = 0

        print("{}, {}".format(date, trend))

      prev_close_val = close_value

# For testing
rate_to_trend('sample-data/USD_JPY_sample.csv')
