import subprocess
import sys




def create_vcf_with_specified_variant_rate(desired_interval, input_vcf, intersection_name, output_vcf, bed_file):
    previous_chromosome = None
    this_variant_position = None

    # open either vcf or vcf.gz
    if '.gz' in input_vcf:
        import gzip
        open_gz_safe = gzip.open
    else:
        open_gz_safe = open

    subprocess.check_output("bedtools intersect -a "+ bed_file + " -b "+ input_vcf + " > " + intersection_name, shell=True)


    with open(output_vcf, 'w') as stream_out:
        with open_gz_safe(input_vcf) as stream_in:
            for i, line in enumerate(stream_in):

                if line[0] == '#':
                    stream_out.write(line)
                    #print(line)
                    continue

                # import pdb; pdb.set_trace()
                this_chromosome = line.split()[0]
                this_variant_position = int(line.split()[1])

                if this_chromosome != previous_chromosome:
                    previous_chromosome = this_chromosome
                    ref_position = this_variant_position
                    stream_out.write(line)
                    belowline = line
                    below = this_variant_position
                    target = ref_position + desired_interval
                    continue

                if this_variant_position > target:
                    above = this_variant_position
                    if (above - target) < (target - below):
                        stream_out.write(line)
                       # print("interval a: ", above - ref_position)
                        #print(line)
                        ref_position = above
                    else:
                        if below > ref_position:
                            stream_out.write(belowline)
                           # print("interval b: ", below - ref_position)
                           # print(line)
                            ref_position = below
                    target = ref_position + desired_interval
                else:
                    below = this_variant_position
                    belowline = line


if __name__ == '__main__':
    vcf_in = '/home/adam/varsim/small.vcf'#vcfSplit/subset_dbsnp_2.txt'
    vcf_out = '/home/adam/PycharmProjects/vcfSimplify/test.vcf'
    bed_in = '/home/adam/varsim/mrjd_test.bed'
    int_name= "int_test.txt"
    #create_vcf_with_specified_variant_rate(1000, vcf_in, int_name, vcf_out, bed_in)
    #cutIt(imput interval spacing, output vcf name)
    create_vcf_with_specified_variant_rate(1000,/mnt/vault/theoh/mrjd/dbsnp-142.vcf,test1000.txt,dbsnp-142-test.vcf,/mnt/vault/theoh/mrjd/mrjd_test.bed