# BWAW
* Genomics course project, 3rd grade, Medical Informatics program at the Faculty of Computers and Information Science, Mansoura University.
* BWAW is a web application for short reads aligner to a reference genome, stands for Burrows-Wheeler Aligner Web app.
* Short read alignment is the process of figuring out where in the genome a short sequence is from.
* Due to the difficulty of using command-line (with non-professional users) as in most alignment programs, we developed the website with GUI.

### Input & Output:
* Input: 
** a Fasta file that contains the reference genome
** a Fastq file that contains short reads
** the minimum allowed matching ratio between a read and the reference
* Output:
** quick overview to show if there is exact matching
** alignment results for each read in a separeted table that contains the aligned position of that read across the reference, matching score and the reference suffix starting from the aligned position(aligned suffix).

### Algorithms used:
* Burrows-Wheeler Transformation

### References:
