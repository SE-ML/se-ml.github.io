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

    with open('./references.bib', 'w') as f:
        for _, r in df.iterrows():
            f.write("@misc{" + r['Ref'] + ',')
            f.write("\n")
            f.write("title = {{ {} }} ".format(r['Title']))
            f.write(",")
            f.write("\n")
            f.write("author = {} ")
            f.write(",")
            f.write("\n")
            f.write("howpublished =  {}".format(
                "\"" + str(r['URL'])+"\""))
            f.write(",")
            f.write("\n")
            f.write("year = {}")
            f.write(",")
            f.write("\n")
            f.write("note = \"[Online; accessed 15-December-2019]\"")
            f.write("\n")
            f.write("}")
            f.write("\n")
            f.write("\n")

            # @misc{bworld,
            #   author = {Ingo Lütkebohle},
            #   title = {{BWorld Robot Control Software}},
            #   howpublished = "\url{http://aiweb.techfak.uni-bielefeld.de/content/bworld-robot-control-software/}",
            #   year = {2008},
            #   note = "[Online; accessed 19-July-2008]"
            # }


if __name__ == '__main__':
    main()
