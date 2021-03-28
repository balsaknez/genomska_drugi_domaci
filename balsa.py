import pysam

unmapped_reads = 0
total_reads = 0
reads_mapp_0 = 0
avg_mapp_all = 0
avg_mapp_without_0 = 0

sum_quality = 0;

for read in pysam.AlignmentFile("/sbgenomics/project-files/merged-tumor.bam"):
    
    if read.is_unmapped:
        unmapped_reads += 1
        
    if read.mapping_quality == 0:
        reads_mapp_0 += 1
        
    sum_quality += read.mapping_quality
    
    total_reads += 1

avg_mapp_all = sum_quality / reads;
avg_mapp_without_0 = sum_quality / (reads - reads_mapp_0)

print("How many unmapped reads are in the file?: " + str(unmapped_reads))
print("Total number of reads: " + str(total_reads))
print("Number of reads with mapping quality 0: " + str(reads_mapp_0))
print("Average mapping quality for all the reads: " + str(avg_mapp_all))
print("Average mapping quality if reads with 0 mapp quality are filtered out: " + str(avg_mapp_without_0))