import os
import sys
import time
import argparse
sys.path.append('scholarly')
from scholarly import scholarly

os.makedirs('Results/', exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument('--category', default='artificial_intelligence')
args =  parser.parse_args()

query = scholarly.search_keyword(args.category)

start_time = time.time()

for i, author in enumerate(query):
    author.yearly_citations = scholarly.search_id(author.id)

    elapsed_seconds = time.time() - start_time

    str_time = '{:02d}:{:02d}:{:02d}'.format(
        int(elapsed_seconds//3600),
        int((elapsed_seconds%3600)/60),
        int(elapsed_seconds%60)
    )

    try: citedby = author.citedby
    except: citedby = 0

    sys.stdout.write("\rCategory: {category}, Authors: {authors}, Cited by: {cited}, Time: {time}".format(
        category=args.category,
        authors=i,
        cited=citedby,
        time=str_time
    ))
    sys.stdout.flush()

    with open('Results/%s.json' % args.category, 'a') as f:
        f.write(str(author) + ',\n')
