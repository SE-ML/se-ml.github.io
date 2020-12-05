import json
import markdown
import mdx_latex
import regex as re
from pathlib import Path

def split_content(c):
  c_ = c.split(': ')
  return c_[1] if len(c_) > 1 else ''



def read_files():
  practice_folder = Path('./_best_practices/').rglob('*.md')
  files = [x for x in practice_folder]
  return [open(x, 'r').readlines() for x in files]


def parse_to_dic(content):
  dic_, parse_c = {}, False
  ct = ''
  for c in content:
    if 'name:' in c:
      dic_['name'] = split_content(c)
    elif 'index:' in c:
      dic_['index'] = split_content(c)
    elif 'references:' in c:
      dic_['references'] = split_content(c)
    elif 'intent:' in c:
      dic_['intent'] = split_content(c)
    elif 'motivation:' in c:
      dic_['motivation'] = split_content(c)
    elif 'applicability:' in c:
      dic_['applicability'] = split_content(c)
    elif 'related:' in c:
      dic_['related'] = split_content(c)
    elif '---' in c and dic_ != {}:
      parse_c = True
    elif parse_c == True:
      ct += c
  dic_['content'] = ct

  return dic_


def dic_to_tex(dic):
  # md = markdown.Markdown(None, extensions=['latex'])
  md = markdown.Markdown()
  latex_mdx = mdx_latex.LaTeXExtension()
  latex_mdx.extendMarkdown(md, markdown.__dict__)

  # template = """
  # \\textbf{{Title}}: {0} \n
  # \\textbf{{Intent}}: {1} \n
  # \\textbf{{Motivation}}: {2} \n
  # \\textbf{{Applicability}}: {3} \n
  # \\textbf{{Description}}: {4} \n
  # \\bigskip
  # """

  template="""
  \\begin{{frame}}[plain]{{ {0} }}

  \\textbf{{Intent}}: {1} \n
  \\textbf{{Motivation}}: {2} \n
  \\textbf{{Applicability}}: {3} \n
  \\textbf{{Description}}: {4} \n

  \\end{{frame}}

  """
  # cont_ = dic['content'].replace('#', '')
  pattern =r'<(a|/a).*?>'
  cont_ = re.sub(pattern , "", dic['content'])
  cont_ = md.convert(cont_)
  cont_ = cont_.replace('<root>', '')
  cont_ = cont_.replace('</root>', '')

  return template.format(dic['name'], dic['intent'], dic['motivation'],
  dic['applicability'], cont_).replace('#', '')




headers = """
\\documentclass{article}
\\usepackage[utf8]{inputenc}

\\title{practices}
\\author{aserban }


\\begin{document}

\\maketitle
"""

footer = """
\\end{document}
"""


headers = ""
footer = ""

def main():
  files = read_files()
  files_dic = [parse_to_dic(x) for x in files]

  file = open("scripts/main.tex", "w")
  file.write(headers)
  for i in files_dic:
    # try:
    print(i)
    pr_ = dic_to_tex(i)
    file.write(pr_)
    # except Exception as e:
    #   print(e)
    #   pass

  file.write(footer)
  file.close()



if __name__ == '__main__':
  main()