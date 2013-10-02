import sys
import datetime

def maf2vcf(F_IN, F_OUT):
  maf=open(F_IN, 'r')
  vcf=open(F_OUT, 'w')
  for line in maf:
    if line.startswith("#"):
      today = datetime.date.today()
      vcf.write('##fileformat=VCFv4.0\n')
      vcf.write("##fileDate="+today.strftime('%d%m%Y\n'))
      vcf.write('##FILTER=<ID=File1Only,Description="Variant was called with qSNP">\n##FILTER=<ID=File2Only,Description="Variant was called with GATK">\n##FILTER=<ID=BothFiles,Description="Variant was called with qSNP and GATK">\n')
      vcf.write('##INFO=<ID=GENE,Type=String,Description="Hugo gene annotation">\n##INFO=<ID=TYPE,Type=String,Description="Variant classification annotation">\n##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n')
    elif line.startswith("Hugo_Symbol"):
      print "vcf header"
      vcf.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n")
    else:
      #print len(line.split("\t"))
      Hugo_Symbol, Entrez_Gene_Id, Center, NCBI_Build, Chromosome, Start_Position, End_Position, Strand, Variant_Classification, Variant_Type, Reference_Allele, Tumor_Seq_Allele1, Tumor_Seq_Allele2, dbSNP_RS, dbSNP_Val_Status, Tumor_Sample_Barcode, Matched_Norm_Sample_Barcode, Match_Norm_Seq_Allele1, Match_Norm_Seq_Allele2, Tumor_Validation_Allele1, Tumor_Validation_Allele2, Match_Norm_Validation_Allele1, Match_Norm_Validation_Allele2, Verification_Status, Validation_Status, Mutation_Status, Sequencing_Phase, Sequence_Source, Validation_Method, Score, BAM_File, Sequencer, QCMG_Flag, ND, TD, Canonical_Transcript_Id, Canonical_AA_Change, Canonical_Base_Change, Alternate_Transcript_Id, Alternate_AA_Change, Alternate_Base_Change, Confidence, CPG, Gff3_Bait, Novel_Starts, CompareStatus = line.strip().split("\t")
      if dbSNP_RS == "novel":
	dbSNP_RS = "."
      if Tumor_Seq_Allele1 == Tumor_Seq_Allele2:
	gt="1/1"
      else:
	gt="0/1"
      if Reference_Allele == Tumor_Seq_Allele1:
	print Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele2, ".", CompareStatus, "GENE="+Hugo_Symbol+";TYPE="+Variant_Classification, "GT", gt
	
	vcf.write("%s\t%s\t%s\t%s\t%s\t.\t%s\tGENE=%s;TYPE=%s\tGT\t%s\n" % (Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele2, CompareStatus, Hugo_Symbol, Variant_Classification, gt))
      
      elif Reference_Allele == Tumor_Seq_Allele2:
	print Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele1, ".", CompareStatus, "GENE="+Hugo_Symbol+";TYPE="+Variant_Classification, "GT", gt
	vcf.write("%s\t%s\t%s\t%s\t%s\t.\t%s\tGENE=%s;TYPE=%s\tGT\t%s\n" % (Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele1, CompareStatus, Hugo_Symbol, Variant_Classification, gt))

      elif Reference_Allele != Tumor_Seq_Allele3 and Reference_Allele != Tumor_Seq_Allele2 and Tumor_Seq_Allele1 == Tumor_Seq_Allele2:
	#print Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele1, ".", CompareStatus, "GENE="+Hugo_Symbol+";TYPE="+Variant_Classification, "GT", gt
	vcf.write("%s\t%s\t%s\t%s\t%s\t.\t%s\tGENE=%s;TYPE=%s\tGT\t%s\n" % (Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele1, CompareStatus, Hugo_Symbol, Variant_Classification, gt))

      else:
	vcf.write("%s\t%s\t%s\t%s\t%s,%s\t.\t%s\tGENE=%s;TYPE=%s\tGT\t%s\n" % (Chromosome, Start_Position, dbSNP_RS, Reference_Allele, Tumor_Seq_Allele1, Tumor_Seq_Allele2, CompareStatus, Hugo_Symbol, Variant_Classification, gt))


if __name__ == "__main__":
  fname=sys.argv[1]
  F_out_name=fname.strip(".maf") + ".vcf"
  maf2vcf(fname, F_out_name)