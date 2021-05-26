#import numpy as np
from fuzzywuzzy import fuzz
import time
from operator import itemgetter

""" PARSING DATA """


"""
    Description: reading fastq file and extract reads sequences.
    Input: fastq file.
    Output: 1 array of reads.
"""
def readFastq_seq(filename):
    reads= []

    with open(filename) as file_obj:
        while True:
            file_obj.readline()
            seq= file_obj.readline().strip()
            file_obj.readline()
            file_obj.readline()

            if not seq:
                break

            reads.append(seq)

    total_reads= len(reads)

    if total_reads>1500:
        reads= reads[:1500]
        
    return reads


"""
    Description: reading fasta file and extract genome reference.
    Input: fasta file.
    Output: string of reference, string of reference name, integer of reference length.
"""
def readFasta_seq(filename):
    ref= ''

    with open(filename) as file_obj:
        SN= file_obj.readline().strip()
        
        while True:
            seq= file_obj.readline().strip()
            if not seq:
                break
            ref+= seq
    
        if ref[-1]!='$': ref+='$'    
    SN= SN[1:]
    LN= len(ref)

    return ref, SN, LN





""" INDEXING """


""" 
    Description: Retun list of rotations of input string t.
    Input: reference string.
    Output: list of rotations of string.
    """
def rotations(t):
    tt= t * 2
    return [tt[i:i+len(t)] for i in range(0, len(t))]


""" 
    Description: Construct Burrows-wheeler Matrix .
    Input: reference string.
    Output: lexicographically sorted list of t's rotations
"""
def bwm(t):
    return sorted(rotations(t))


""" 
    Description: Extract Burrows-wheeler transformation from Burrows-wheeler Matrix.
    Input: reference string.
    Output: BWT(t) by way of the BWM
 """
def bwtViaBwm(t):
    """ Given t, returns BWT(t) by way of the BWM """
    BWT= ''.join(map(lambda x:x[-1], bwm(t)))
    return BWT


""" 
    Description: Construct Suffix Array for a given string.
    Input: reference string.
    Output: suffix array SA(t), which is an array of sorted tuples of suffixes and offsets.
 """  
def suffixArray(t):
    setup= sorted([(t[i:], i) for i in range(0, len(t))])
    return  setup       


""" 
    Description: Construct count array and occurances table of a BWT of a string.
    Input: BWT.
    Output: C, Occ.
""" 
def preprocessing(BWT):

    """ C table """
    C= {}
    alphabet= sorted(set(BWT))

    alphabetRev= alphabet
    alphabetRev.reverse()

    for i in alphabet:
        C[i]= 0
    for char in BWT:
        C[char] += 1

    size= len(BWT)
    for char in alphabetRev:
        C[char]= size - C[char]
        size= C[char]

    """ Occ table"""
    Occ= {}

    for char in alphabet:
        Occ[char]= [0]*len(BWT)

    for step in range(len(BWT)):
        char= BWT[step]
        Occ[char][step]= 1

    for char in alphabet:
        for step in range(1, len(BWT), 1):
            Occ[char][step] += Occ[char][step-1]

    return C, Occ    
    




""" ALIGNMENT """


""" NOT USED 
    Description: Computing edit distance(levenshtein distance) between 2 string.
    Input: string a, string b.
    Output: minimum distance between them.
""" 
"""
def levDist(a, b):

    size_a= len(a)
    size_b= len(b)+1
    matrix= np.zeros((size_b, size_a))

    for i in range(size_a):
        matrix[0, i]= i

    for i in range(size_b):
        matrix[i, 0]= i

    for row in range(1, len(b)+1):
        for col in range(1, len(a)):
            if a[col-1]==b[row-1]:
                matrix[row][col]= matrix[row-1][col-1]
            else:
                matrix[row][col]= min(matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1]) + 1

    return (matrix[size_b-1, size_a-1])
"""

    
""" 
    Description: Exact match.
    Input: reference, read.
    Output: exact matching positions.
""" 
def boyermoorehorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1


""" 
    Description: calculate fm-index for each backward search iteration to get possible intervals to align a pattern to string using BWT and SA.
    Input: iteration num, previous top, previous bottom, current char, pattern, Suffix array of the string, dict of distances to fill, BWT, C array, Occ table.
    Output: current top, current bottom.
""" 
def FM_index_iteration(i, k, l, b, p, SA, dists, BWT, C, Occ):
    
    k_dash= k
    l_dash= l
    next= 0
    
    if b == '$':
        next= C['A']
    elif b == 'A':
        next= C['C']
    elif b == 'C':
        next= C['G']
    elif b == 'G':
        next= C['T']
    elif b == 'T':
        next= C['T']

    if i== len(p)-1:
        k_dash= C[b]
        if b=='T': l_dash= len(BWT)-1
        else: l_dash= next-1
    else:
        k_dash= C[b] + Occ[b][k_dash-1]
        l_dash= C[b] + Occ[b][l_dash]-1

    mini= min(k_dash, l_dash)
    mini= max(mini, 1)
    maxi= max(k_dash, l_dash)
    maxi= max(maxi, 1)
    
    suffix_visited= []

    for suffix in range(mini, maxi+1):
        
        if suffix not in suffix_visited:
            dists[suffix]= fuzz.ratio(SA[suffix][0][:-1], p)
            #dists[suffix]= levDist(SA[suffix][0], p)
        
        suffix_visited.append(suffix)

    return k_dash, l_dash


""" 
    Description: perform backward search query on a pattern p using BWT.
    Input: pattern, BWT, Suffix array of the string.
    Output: r dict of mapped intervals, dists dict of levDist of suffixes and pattern.
""" 
def backward_search(p, BWT, SA):
    dists= {}
    k= 0
    l= len(BWT)-1
    r= {}
    i= len(p)-1
    while(i>=0 ):
        k,l= FM_index_iteration(i, k, l, p[i], p, SA, dists, BWT, C, Occ)
        r[i]= [k, l]
        i-=1
        
    return r, dists


""" 
    Description: Inexact search results.
    Input: dists dict, num of errors(mismatches, insertion, deletion) allowed, Suffix array of the string.
    Output: found_in dict of aligned position against the reference with n errers, s.t. n<=k.
""" 
def inexact_search(dists, minimum_match_ratio, SA):
    print('Inexact search results==> {starting_position_in_txt: (match_ratio, aligned_portion)}')
    found_in= {}
    for suffix in dists:
        if dists[suffix]>=minimum_match_ratio:
            found_in[SA[suffix][1]]= (dists[suffix], SA[suffix][0][:-1])

    found_in= {k: v for k,v in sorted(found_in.items(), key=itemgetter(1))}
    return found_in


""" 
    Description: contains basic header of alignment.
    Input: reference name from fasta file, reference length.
    Output: None.
""" 
def header(SN, LN):
    print('@SQ  SN:{0}  LN:{1}'.format(SN, LN))
    print('@PG  ID:BWAW_team    VN:1.0')




""" MAIN """
if __name__ == '__main__':

    start_time = time.time()
    t, SN, LN= readFasta_seq('phi-X174.fasta')
    reads= readFastq_seq('phi2.fastq')
    
    rotations(t)
    bwm(t)
    BWT= bwtViaBwm(t)
    SA= suffixArray(t)
    C, Occ= preprocessing(BWT)

    header(SN, LN)
    
    for read in reads:
        s = boyermoorehorspool(read, t)
        if s > -1:
            print ('Pattern \"' + read + '\" found at position',s)

    for read in reads:
        print('Read: ', read)
        r, dists= backward_search(read ,BWT, SA)
        print(inexact_search(dists, 60, SA))
        print()

    print("--- %s seconds ---" % (time.time() - start_time))


