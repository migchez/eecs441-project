#! /usr/bin/env python

# USAGE
#
# For now assumes that data is formatted like the sample-data/USD_JPY_sample.csv
# To use:
# ./rate_to_trend <input_file_path> <output_file_path>
# example:
# ./rate_to_trend sample-data/USD_JPY_sample.csv processed/USD_JPY_trends.csv

import csv
import argparse

def rate_to_trend(input_file_path, output_file_path):
  # Defines index of close value of data
  CLOSE_INDEX = 4;

  with open(output_file_path, 'wb') as output_file:
    writer = csv.writer(output_file);
    with open(input_file_path, 'rb') as input_file:
      reader = csv.reader(input_file, delimiter=' ', quotechar='|')
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

          writer.writerow([date, trend])

        prev_close_val = close_value

parser = argparse.ArgumentParser(description="Converts daily close rates to trends")
parser.add_argument('input_file_path')
parser.add_argument('output_file_path')
args = parser.parse_args()
rate_to_trend(args.input_file_path, args.output_file_path)
