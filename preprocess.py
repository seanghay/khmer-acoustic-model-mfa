import os
import csv

with open("km_kh_male/line_index.tsv") as fp:
  reader = csv.reader(fp, delimiter="\t")
  for item in reader:
    txtfile = os.path.join("km_kh_male", "wavs", item[0] + ".txt")
    with open(txtfile, "w") as outfile:
      outfile.write(item[2])
