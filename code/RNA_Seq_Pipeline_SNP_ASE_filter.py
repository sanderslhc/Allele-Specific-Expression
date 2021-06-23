#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path

def filter(input_file, output_file):
    with open(input_file, "r") as fp, open(output_file, "w") as wp:
        header = fp.readline().strip().split()
        wp.write("\t".join(header[0:8]) + "\n")
        for line in fp:
            line_split = line.strip().split()
            refCount = int(line_split[5])
            altCount = int(line_split[6])
            totalCount = int(line_split[7])
            if totalCount >= 20 and refCount >=3 and altCount >=3 and refCount/totalCount >= 0.01 and altCount/totalCount >= 0.01:
            # if totalCount >= 30 and refCount >=5 and altCount >=5 and refCount/totalCount >= 0.01 and altCount/totalCount >= 0.01:
                out_line = line_split[0:8]
                wp.write("\t".join(out_line) + "\n")
def main():
    file_list = "/media/disk2/sijf/Cattle_RNASeq/Scripts/Cattle_RNASeq.SRS.all.list"
    dir_in = "/media/disk2/sijf/Cattle_RNASeq/Output/SNP"
    dir_out = "/media/disk2/sijf/Cattle_RNASeq/Output/ASE"
    # os.mkdir(dir_out)
    Path(dir_out).mkdir(parents=True, exist_ok=True)
    with open(file_list, "r") as fp:
        for line in fp:
            srs_id = line.strip()
            input_file = f'{dir_in}/{srs_id}/{srs_id}.ASE.table.txt'
            output_file = f'{dir_out}/{srs_id}.ASE.table.filter.txt'
            # output_file = f'{dir_out}/{srs_id}.ASE.table.filter.strict.txt'
            if os.path.exists(input_file):
                filter(input_file, output_file)
            else:
                print(f'{srs_id}.ASE.table.txt do not exist.')
if __name__ == "__main__":
    main()
