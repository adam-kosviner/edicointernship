#!/usr/bin/python
def findsim(fastqlocation, newfilename):
    numbdict = {}
    j = ''
    k = 0
    with open(newfilename, 'w') as stream_out:
        with open(fastqlocation, "r") as stream:
            for i, line in enumerate(stream):
                atloc = line[0:6]
                if atloc=='@test.':
                    numb = line[6:15]
                    stream_out.write(atloc + numb + j+ '\n')
                    #print numb + j
                    if numb == "000000192":
                        k = k+1
                        j = "_" + str(k)
                else:
                    stream_out.write(line)









if __name__ == "__main__":
    fastqloc='/home/adam/PycharmProjects/fastqproject/mason_hg19_chrM_151bp_30x_known_variants_2.fastq'
    findsim(fastqloc, '/home/adam/PycharmProjects/fastqproject/mason_hg19_chrM_151bp_30x_known_variants_2_new.fastq')