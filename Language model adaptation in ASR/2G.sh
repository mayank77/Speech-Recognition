#!/bin/zsh
echo "START"
minppl=999
minval=$i
for i in $(seq 0.00 $1 1.00 )
do
ngram -lm 2gramGIG_lm.lm.gz -mix-lm 2gram_wsj70.lm.gz -lambda $i -write-lm adapted_LM.lm
ngram -lm adapted_LM.lm -ppl wsj_eval_dev.trn >one.txt
echo "====================="
echo "FOR " $i 
echo $(sed -n '2p' one.txt)
curr=$(awk 'END {print $NF}' one.txt)
rm one.txt
res=$(awk -vx=$curr -vy=$minppl 'BEGIN{ print x>=y?1:0}')
if [ "$res" -eq 0 ]
then minval=$i
minppl=$curr
fi
rm adapted_LM.lm
done
echo "OPTIMAL LAMBDA IS : " $minval



