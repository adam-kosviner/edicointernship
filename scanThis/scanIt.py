#!/usr/bin/python
import json
import argparse
import logging

logging.basicConfig(filename='logger.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


def getBedchr(line):
    chr = line.split()[0]
    chr=chr[3:]
    chr=int(chr)
    return chr


def getBedRng1(line):
    range1 =line.split()[1]
    range1=int(range1)
    return range1


def getBedRng2(line):
    range2 = line.split()[2]
    range2 = int(range2)
    return range2


def getVcfChr(line):
    if line[0]!="#":
        chr = line.split()[0]
        chr=int(chr)
        return chr

def getVcfIndex(line):
    if line[0]!="#":
        index = line.split()[1]
        index=int(index)
        return index


def compare(bedLocation, vcfLocation):
    with open(bedLocation, "r") as stream:
        for i, line in enumerate(stream):
            chr1 = getBedchr(line)
            range1= getBedRng1(line)
            range2= getBedRng2(line)
            with open(vcfLocation, "r") as stream:
                for p, line2 in enumerate(stream):
                    chr2 = getVcfChr(line2)
                    index= getVcfIndex(line2)
                    if chr1 == chr2 and range1 < index < range2:
                        logging.debug(line2)
                    else:
                        logging.debug(line2)


def createVcf(bedLocation, vcfLocation):
    #initialiae new vcf file
    print


if __name__ == "__main__":
   # parser = argparse.ArguementParser()

    #parser.add_arguement(''
   compare("/home/adam/varsim/mrjd_test.bed","/home/adam/varsim/small.vcf")