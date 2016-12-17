import random
import re
import os
from shutil import copyfile

rep = 0
def deleteLine(tx,nm):
    global rep
    r = -1
    f = open('wsj_eval_train.trn')
    with open(nm, "a") as myfile:
        myfile.write(tx)
        myfile.write("\n")
    output = []
    for line in f:
        if tx != line.strip():
            output.append(line)
        else:
            r = r + 1
    f.close()
    f = open('wsj_eval_train.trn', 'w')
    f.writelines(output)
    f.close()
    rep = rep + r*len(re.findall(r'\w+', tx))
    if r > 0:
        print "The Redundant Sentence Was : ",tx
        print "It occured : ", r+1 , " times\n\n"


def random_line(nm):
    lines = open('wsj_eval_train.trn').read().splitlines()
    myline =random.choice(lines)
    deleteLine(myline,nm)

   
lines = open('wsj_eval.trn').read().splitlines()
f = open('wsj_eval.trn')
output = []
for b in f:
    a = re.sub(r' \([^)]*\)', '',b )
    output.append(a)
f.close()
f = open('wsj_eval.trn', 'w')
f.writelines(output)
f.close()

if os.path.exists('wsj_eval_dev.trn'):
    os.remove('wsj_eval_dev.trn')
    
if os.path.exists('wsj_eval_test.trn'):
    os.remove('wsj_eval_test.trn')
    
if os.path.exists('wsj_eval_train.trn'):
    os.remove('wsj_eval_train.trn')
    
copyfile('wsj_eval.trn', 'wsj_eval_train.trn')

for i in range(0,int(0.3*len(lines))):
    random_line('wsj_eval_dev.trn')
    
for i in range(0,int(0.02*len(lines))):
    random_line('wsj_eval_test.trn')
    
with open('wsj_eval.trn') as f:
    sentence = f.read()
words = re.findall(r'\w+', sentence)
print "Words in Original Set :" , len(words)
    
with open('wsj_eval_train.trn') as f:
    sentence = f.read()
words1 = re.findall(r'\w+', sentence)
print "Words in Training Set :" , len(words1)


with open('wsj_eval_dev.trn') as f:
    sentence1 = f.read()
words2 = re.findall(r'\w+', sentence1)
print "Words in Development Set :" , len(words2)

with open('wsj_eval_test.trn') as f:
    sentence2 = f.read()
words3 = re.findall(r'\w+', sentence2)
print "Words in Test Set :" , len(words3)
print "Number of Extra Words Removed Due to Repeated Sentences " , rep

print "Total Words = ", len(words1) + len(words2) + len(words3) + rep