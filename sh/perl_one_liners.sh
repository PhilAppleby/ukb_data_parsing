# A perl pie script - edit in-place with backup
perl -p -i.bak -e 's/\/home\/pda11181\/devel\/ukb_data_parsing/\$\{PROJROOT\}/g' *.sh
# A perl -pe script - edit with column split and data removal
time zcat cd_build37_40266_20161107.txt | perl -pe 's/^MarkerName/Chr\tPos/g;s/(\d+):(\d+)_\w+_\w+/$1\t$2/g' > chg_file2.txt

time zcat cd_build37_40266_20161107.txt.gz | perl -pe 's/^(MarkerName)/Chr\tPos\t$1/g;s/(\d+)(:)(\d+)(_\w+_\w+)/$1\t$3\t$1$2$3$4/g' > chg_file3.txt


