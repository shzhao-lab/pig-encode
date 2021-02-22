#!/usr/bin/python3
import argparse
import os,sys
parser = argparse.ArgumentParser(description="description:identify enhancer or promoter")
parser.add_argument("--tissue",help="eg.LW-2W-1-Heart")
parser.add_argument("--marker1",help="eg.LW-2W-1-H3K4me3-Heart.summit2.bed")
parser.add_argument("--marker2",help="eg.LW-2W-2-H3K27ac-Heart.summit2.bed")
parser.add_argument("--TSSPath",help="Path of flanked TSS region") #2.5 kb upstream and 1 kb downstream
args=parser.parse_args()
######
argv0_list = sys.argv[0].split("\\")
script_name = argv0_list[0]
#merge tss.bed and H3K4me3.bed
cmd="cat {} {} | bedtools sort -i - > {}-total-promoter.bed".format(args.marker1,args.TSSPath,args.tissue)
os.system(cmd)
#identify enhancer
cmd="intersectBed -a {} -b {}-total-promoter.bed -v > {}-enhancer.bed".format(args.marker2,args.tissue,args.tissue)
os.system(cmd)
#identify known-promoter
cmd="intersectBed -a {} -b {} -u -wa > {}-known-promoter.bed".format(args.marker1,args.TSSPath,args.tissue)
os.system(cmd)
#identify novel-promoter
cmd="intersectBed -a {} -b {} -v > {}-novel-promoter.bed".format(args.marker1,args.TSSPath,args.tissue)
os.system(cmd)
#print("python3 "+script_name ) 
with open(args.tissue + ".sh",'wt') as f1:
    print("python3 "+script_name + " --tissue " + args.tissue + " --marker1 " + args.marker1 + " --marker2 " + args.marker2 + " --TSSPath " + args.TSSPath,file=f1)
cmd="mkdir {}".format(args.tissue)
os.system(cmd)
cmd="mv {}-total-promoter.bed {}-enhancer.bed {}-known-promoter.bed {}-novel-promoter.bed {}.sh {}".format(args.tissue,args.tissue,args.tissue,args.tissue,args.tissue,args.tissue)
os.system(cmd)
OutFile1="{}/{}-enhancer.bed".format(args.tissue,args.tissue)
OutFile2="{}/{}-known-promoter.bed".format(args.tissue,args.tissue)
OutFile3="{}/{}-novel-promoter.bed".format(args.tissue,args.tissue)
count1=len(open(OutFile1).readlines())
count2=len(open(OutFile2).readlines())
count3=len(open(OutFile3).readlines())
with open('CRE_number.txt','a+') as f1:
    print(args.tissue+'\t'+os.getcwd()+'/'+OutFile1+'\t'+str(count1)+'\t'+os.getcwd()+'/'+OutFile2+'\t'+str(count2)+'\t'+os.getcwd()+'/'+OutFile3+'\t'+str(count3),file=f1)
