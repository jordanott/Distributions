import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--category', default='artificial_intelligence')
args = parser.parse_args()

with open('Results/%s.json' % args.category, 'r') as f:
    data = '[' + f.read()[:-1] + ']'
    print(len(eval(data)))
