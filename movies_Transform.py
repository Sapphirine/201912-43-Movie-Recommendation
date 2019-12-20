"""
Author: Guojing Wu
Date: 2019/11/19
Description:
    This file is used for transform movies_metadata.csv into .json
"""

import csv, json, ast
from datetime import datetime
input_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/movies_metadata.csv"
output_path = "/Users/wuguojing/Desktop/Myfile/EECS6893/Final/movies.json"


def main(input_file, json_file):
    fp = open(json_file, 'w')

    with open(input_file) as csv_file:
        for movie in csv.DictReader(csv_file):
            tmp = dict()

            tmp["id"] = int(movie["id"])

            tmp["imdb_id"] = movie["imdb_id"]

            tmp["adult"] = (movie["adult"] == "true")

            if len(movie["belongs_to_collection"]) > 0:
                tmp["belongs_to_collection"] = ast.literal_eval(movie["belongs_to_collection"])

            if len(movie["budget"]) > 0:
                tmp["budget"] = int(movie["budget"])

            if len(movie["genres"]) > 0:
                tmp["genres"] = ast.literal_eval(movie["genres"])

            tmp["homepage"] = movie["homepage"]

            tmp["original_language"] = movie["original_language"]

            tmp["original_title"] = movie["original_title"]

            tmp["overview"] = movie["overview"]

            if len(movie["popularity"]) > 0:
                tmp["popularity"] = float(movie["popularity"])

            tmp["poster_path"] = movie["poster_path"]

            if len(movie["production_companies"]) > 0:
                tmp["production_companies"] = ast.literal_eval(movie["production_companies"])

            if len(movie["production_countries"]) > 0:
                tmp["production_countries"] = ast.literal_eval(movie["production_countries"])

            if len(movie["release_date"]) > 0:
                try:
                    tmp["release_date"] = datetime.strptime(movie["release_date"], '%m/%d/%y').strftime('%Y-%m-%d')
                except ValueError:
                    tmp["release_date"] = datetime.strptime(movie["release_date"], '%m/%d/%Y').strftime('%Y-%m-%d')

            if len(movie["revenue"]) > 0:
                tmp["revenue"] = int(movie["revenue"])

            if len(movie["runtime"]) > 0:
                tmp["runtime"] = int(movie["runtime"])

            if len(movie["spoken_languages"]) > 0:
                tmp["spoken_languages"] = ast.literal_eval(movie["spoken_languages"])

            tmp["status"] = movie["status"]

            tmp["tagline"] = movie["tagline"]

            tmp["title"] = movie["title"]

            tmp["video"] = (movie["video"] == 'true')

            if len(movie["vote_average"]) > 0:
                tmp["vote_average"] = float(movie["vote_average"])

            if len(movie["vote_average"]) > 0:
                tmp["vote_average"] = int(movie["vote_count"])

            json.dump(tmp, fp, ensure_ascii=False)
            fp.write('\n')

    fp.close()


if __name__ == '__main__':
   main(input_path, output_path)