import sys, re, collections

WORD_RE = re.compile('\w+')
index = collections.defaultdict(list)

with open(sys.argv[1],encoding='utf8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location=(line_no, column_no)
            index[word].append(location)