
def findAvg():
    with open("/home/adam/varsim/mrjd_test.bed", "r") as stream:
        for i, line in enumerate(stream):
            range1 = getBedRng1(line)
            range2 = getBedRng2(line)
            print range2,range1


def getBedRng1(line):
    range1 =line.split()[1]
    range1=int(range1)
    return range1


def getBedRng2(line):
    range2 = line.split()[2]
    range2 = int(range2)
    return range2


if __name__ == "__main__":
   # parser = argparse.ArguementParser()

    #parser.add_arguement(''
    findAvg()