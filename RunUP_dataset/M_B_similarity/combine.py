import os
import glob
import pandas as pd

extension = 'csv'

os.chdir('../W_B_similarity/')
cnt=0
for i in glob.glob('*_similarity.{}'.format(extension)):
    cnt+=1
    if cnt%400 == 0:
        print(cnt)
    df = pd.read_csv(i)[:31]
    df.to_csv(i)
#combine all files in the list
# try:
#     combined_csv = pd.concat([pd.read_csv(f, encoding='cp949', names=['link','prod_id','original_num','name','price','gender','type','images']) for f in all_filenames ])
# except:
# combined_csv = pd.concat([pd.read_csv(f, encoding='utf-8', names=['link','prod_id','original_num','name','price','gender','type','images'], header=1) for f in all_filenames ])

# file = pd.read_csv()

# #export to csv
# combined_csv.to_csv(f"smartstore_detail_combined.csv", index=False)
