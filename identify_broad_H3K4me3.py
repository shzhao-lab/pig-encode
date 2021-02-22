#!/usr/bin/python3
import argparse
import os,sys
parser = argparse.ArgumentParser(description="description:identify broad H3K4me3")
parser.add_argument("--marker",help="eg.Duroc-Fat-H3K4me3")
parser.add_argument("--TSSPath",help="Path of TSS_reference") #1bp region
args=parser.parse_args()
######
argv0_list = sys.argv[0].split("\\")
script_name = argv0_list[0]

#filter peaks by Pvalue and FoldChange
cmd="zcat {}.nodup.tagAlign.broadPeak.gz|awk '{{if($8>8 && $7>4){{print $1,$2,$3,$8,$7}}}}' OFS='\t' - > {}_p8_fc4.bed".format(args.marker,args.marker)
os.system(cmd)
#filter peaks by width
awk '$3-$2>5000' {}_p8_fc4.bed > {}_p8_fc4_length5k.bed".format(args.marker,args.marker)
os.system(cmd)
#filter peaks by TSS
intersectBed -a {}_p8_fc4_length5k.bed -b {} -u -wa > {}_broad_H3K4me3.bed".format(args.marker,args.TSSPath,args.marker)
os.system(cmd)
#print("python3 "+script_name ) 
with open(args.tissue + ".sh",'wt') as f1:
    print("python3 "+script_name + " --marker " + args.marker + " --TSSPath " + args.TSSPath,file=f1)
cmd="rm {}_p8_fc4.bed {}_p8_fc4_length5k.bed".format(args.marker,args.marker)
os.system(cmd)
