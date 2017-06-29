

def cutIt(interval,filename):
    writer=open(filename+'.vcf',"w+")
    firstline = 0
    below = 0
    belowLine=''
    chrom1=0;
    #firstline lets the first line of the vcf print unconditionally
    #below is set to zero to allow the first run; below is normaly changed at the bottom of the method
    with open("/home/adam/varsim/vcfSplit/subset_dbsnp_2.txt", "r") as stream:
        for i, line in enumerate(stream):
            if line[0] == '#':
                writer.write (line)
                continue
            # ^ skips comments
            #if firstline == 0:
             #   firstline = 1
             #   writer.write (line)
              #  reference = int(line.split()[1])
             #   chrom1 = int(line.split()[0][3:])
            # ^ prints first line and esablishes reference value as previously printed value as well as first chromesome tested

            chrom2 = int(line.split()[0][3:])
            if chrom1 != chrom2:
                reference = int(line.split()[1])
                writer.write(line)
                chrom1 = chrom2
                dontCompare=1
            # ^ if the chromesome changes the first line of the new chrom prints
            print reference
            print reference + interval
            print int(line.split()[1])
            print
            if (int(reference+interval) < int(line.split()[1])) & dontCompare==0:
                above = line.split()[1]
                above=int(above)
                #above is the higher of the two values that the reference+interval is between

                if (above-reference) < (reference-below):
                    writer.write(line)
                    reference = above-(above%interval)
                else:
                    writer.write(belowLine)
                    reference = below - (below % interval)
            below = line.split()[1]
            below= int(below)
            belowLine=line
            dontCompare=1
            # bottom is the lower of the two values that the reference+interval is between

def cutIt2(interval, filename):
    writer = open(filename + '.vcf', "w+")
    chrom1 = 0
    below=0
    interval= int(interval)
    with open("/home/adam/varsim/vcfSplit/subset_dbsnp_2.txt", "r") as stream:
        for i, line in enumerate(stream):

            if line[0] == '#':
                writer.write (line)
                continue

            chrom2 = int(line.split()[0][3:])
            if chrom2 != chrom1:
                chrom1 = chrom2
                writer.write(line)
                reference = int(line.split()[1])
                belowline = line
                below = int(line.split()[1])
                continue

            target =reference+interval
            current = int(line.split()[1])

            if target < current:
                above = current

                if above - target < target - below:
                    print 1
                    writer.write(line)
                    reference = above #- (int(line.split()[1]) % interval)
                else:
                    writer.write(belowline)
                    reference = below #- (below % interval)
            else:
                belowline = line
                below = current

cutIt2(1000,'test')

    #cutIt(imput interval spacing, output vcf name)