import json
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
    if 'name' in c:
      dic_['name'] = split_content(c)
    elif 'index' in c:
      dic_['index'] = split_content(c)
    elif 'references' in c:
      dic_['references'] = split_content(c)
    elif 'intent' in c:
      dic_['intent'] = split_content(c)
    elif 'motivation' in c:
      dic_['motivation'] = split_content(c)
    elif 'applicability' in c:
      dic_['applicability'] = split_content(c)
    elif 'related' in c:
      dic_['related'] = split_content(c)
    elif '---' in c and dic_ != {}:
      parse_c = True
    elif parse_c == True:
      ct += c
  dic_['content'] = ct
  return dic_


def dic_to_tex(dic):
  template = """
  \\textbf{{Title}}: {0} \n
  \\textbf{{Intent}}: {1} \n
  \\textbf{{Motivation}}: {2} \n
  \\textbf{{Applicability}}: {3} \n
  \\textbf{{Description}}: {4} \n
  \\bigskip
  """
  return template.format(dic['name'], dic['intent'], dic['motivation'],
  dic['applicability'], dic['content']).replace('#', '')


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

def main():
  files = read_files()
  files_dic = [parse_to_dic(x) for x in files]

  file = open("scripts/main.tex", "w")
  file.write(headers)
  for i in files_dic:
    print(i)
    try:
      pr_ = dic_to_tex(i)
      file.write(pr_)
    except Exception as e:
      pass

  file.write(footer)
  file.close()



if __name__ == '__main__':
  main()