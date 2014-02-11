from sys import argv

script, filename = argv

with open(filename, 'r') as f:
    txt = f.read()

restaurant_scores ={}

txt = txt.split("\n")

for line in txt:
    split_txt= line.split(":")
    if len(split_txt) == 2:
        restaurant_scores[split_txt[0]]=split_txt[1]

thekeys = restaurant_scores.keys()
thekeys.sort()

for k in thekeys:
    print "Restaurant %r is rated %d" % (k, int(restaurant_scores[k]))