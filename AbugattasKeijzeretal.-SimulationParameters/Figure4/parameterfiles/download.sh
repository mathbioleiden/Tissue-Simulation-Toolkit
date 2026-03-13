file=ECM0010000.jpg

rsync -zahP \
    --include 'data_*/' \
    --include 'data_*/instances/' \
    --include 'data_*/instances/state_dumper/' \
    --include 'data_*/instances/state_dumper/workdir' \
    --include ${file} \
    --include 'state_0010000.pickle' \
    --include 'state_0005000.pickle' \
    --include 'state_0000000.pickle' \
    --include 'configuration.ymmsl' \
    --exclude '*' \
    camb:/home/koen/data/20251222/ \
    .

rsync -zahP camb:~/data/20251222/"*feather" .
# mkdir finals
# 
# find . -name 'data_*' | while read folder; do
#     name=${folder#./data_*}    
#     cp ${folder}/instances/state_dumper/workdir/${file} finals/${name}.jpg
# done
# 
