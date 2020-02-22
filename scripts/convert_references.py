###
# Converts csv with references to markdown
##
import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='references.csv', type=str)
    return parser.parse_args()


def main():
    # config
    args = parse_args()
    df = pd.read_csv(args.file)
    df = df.dropna(subset=['Ref'])
    for _, r in df.iterrows():
        filename = '../_references/' + str(r['Ref']).lower() + '.md'
        with open(filename, 'w') as f:
            f.write("---")
            f.write("\n")
            f.write("title: \'{}\' ".format(r['Title']))
            f.write("\n")
            f.write("acronym: {}".format(r['Ref']))
            f.write("\n")
            f.write("type: {}".format(r['Type']))
            f.write("\n")
            f.write("webpage: \'{}\' ".format((r['URL'])))
            f.write("\n")
            f.write("---")


if __name__ == '__main__':
    main()
