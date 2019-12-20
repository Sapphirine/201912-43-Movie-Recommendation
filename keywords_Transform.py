"""
Author: Guojing Wu
Date: 2019/11/19
Description:
    This file is used for transform keywords.csv into .json
"""

import csv, json, ast
input_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/keywords.csv"
output_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/keywords.json"


def main(input_file, json_file):
    fp = open(json_file, 'w')

    with open(input_file) as csv_file:
        for keyword in csv.DictReader(csv_file):
            tmp = dict()
            tmp['id'] = int(keyword['id'])

            tbl = ast.literal_eval(keyword['keywords'])
            # print(tbl)
            tmp['keywords'] = tbl

            json.dump(tmp, fp, ensure_ascii=False)
            fp.write('\n')

    fp.close()


if __name__ == '__main__':
   main(input_path, output_path)