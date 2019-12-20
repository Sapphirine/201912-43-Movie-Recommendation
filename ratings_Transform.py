"""
Author: Guojing Wu
Date: 2019/11/19
Description:
    This file is used for transform ratings.csv into .json
"""

import csv, json, ast
from datetime import datetime
input_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/ratings.csv"
output_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/ratings.json"


def main(input_file, json_file):
    fp = open(json_file, 'w')

    with open(input_file) as csv_file:
        for rate in csv.DictReader(csv_file):
            tmp = dict()
            tmp['userId'] = int(rate['userId'])
            tmp["movieId"] = int(rate["movieId"])
            tmp["rating"] = float(rate["rating"])
            tmp["timestamp"] = int(rate["timestamp"])

            json.dump(tmp, fp, ensure_ascii=False)
            fp.write('\n')

    fp.close()


if __name__ == '__main__':
   main(input_path, output_path)