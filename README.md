# BWAW
* Genomics course project, 3rd grade, Medical Informatics program at the Faculty of Computers and Information Science, Mansoura University.
* BWAW is a web application for short reads aligner to a reference genome, stands for Burrows-Wheeler Aligner Web app.
* Short read alignment is the process of figuring out where in the genome a short sequence is from.
* Due to the difficulty of using command-line (for non-professional users) as in most alignment programs, we developed the website with GUI.

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
* Boyer-Moore-Horspool

### References:
* https://github.com/SaraEl-Metwally/Informatics-on-High-throughput-Sequencing-Data-Course-Summer-2020-/
* https://github.com/lh3/bwa
* https://www.cs.jhu.edu/~langmea/resources/lecture_notes/bwt_and_fm_index.pdf
* https://www.researchgate.net/publication/271600379_Fast_inexact_mapping_using_advanced_tree_exploration_on_backward_search_methods
* https://www.sciencedirect.com/science/article/pii/S1570866713000397
* https://gist.github.com/Puriney/6324227
* https://youtu.be/Dd_NgYVOdLk
* https://iajit.org/PDF/November%202019,%20No.%206/15585.pdf

### Video demo drive link:
* https://drive.google.com/file/d/1jqwcC0SOCjnzNTihr66iesycv5Fm7byq/view

### Team members:
* Asmaa Mostafa Elsayed
* Aya Salah Mohamed
* Hanaa Hamdy Ahmed
* Kholoud Mohamed Mohamed
* Reham Mohamed Elbaz
