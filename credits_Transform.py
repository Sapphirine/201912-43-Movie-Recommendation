"""
Author: Guojing Wu
Date: 2019/11/19
Description:
    This file is used for transform credits.csv into .json
"""

import csv, json, ast
input_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/credits.csv"
output_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/credits.json"


def main(input_file, json_file):
    fp = open(json_file, 'w')

    with open(input_file) as csv_file:
        for credit in csv.DictReader(csv_file):
            tmp = dict()
            tmp['id'] = int(credit['id'])

            if len(credit["cast"]) > 0:
                tmp["cast"] = ast.literal_eval(credit["cast"])

            if len(credit["crew"]) > 0:
                tmp["crew"] = ast.literal_eval(credit["crew"])

            json.dump(tmp, fp, ensure_ascii=False)
            fp.write('\n')


if __name__ == '__main__':
   main(input_path, output_path)