# LABB 5
# Sebastijan Babic
# 2024 - 02 - 15

## UPPGIFT 1 ##
class DnaSeq():
    def __init__(self, accession, seq):
        self.accession = accession
        self.seq = seq
        if not accession or not seq:
            raise ValueError('Accession och DNA-sekvensen får inte vara tomma')
        
    def __len__(self):
        if self.seq is None:  # Handle case if length is None to return 0, overkill though due to raise ValueError above
            return 0
        return len(self.seq)
        
    def __str__(self):
        if self.accession == '': # ^^^
            return 0
        return f"<DnaSeq accession='{self.accession}'>"


    




## UPPGIFT 2 ##
def read_dna(filename):
    dna_sequences = [] # Make empty list to save DnaSeq object
    current_accession = None # Variable to hold current id
    
    
    with open(filename, 'r') as file:
        
        for line in file:
            line = line.strip() # Get rid of empty space
            
            if not line: # Ignore empty row
                continue
        
            if line.startswith('>'): # Identify id-row
                current_accession = line[1:] # Save id (exclude >)
            
            else: # Line is sequence, append as DnaSeq object
                dna_sequence = line # 
                dna_sequences.append(DnaSeq(current_accession,dna_sequence))
        
    return dna_sequences







## UPPGIFT 3 ##
def check_exact_overlap(a, b, min_overlap=10):
    '''
    Takes two DnaSeq objects and a minimum length. 
    
    Returns length of the longest overlap between sequence a and b. Assuming overlap minimum as long as 
    min_overlap=10
    
    :param a: DnaSeq-objekt, sequence a
    :param b: DnaSeq-objekt, sequence b
    :param min_overlap: Minimum length for overlap (default value 10)
    :return: Length of the longest overlap, if no overlap return 0
    '''
    # Make sure sequences long enough to overlap
    max_possible_overlap = min(len(a.seq), len(b.seq))
    # Stop with -1 so to stop iteration before min_length
    # Step -1 - count backwards
    for overlap_length in range(max_possible_overlap, min_overlap - 1, -1): 
        if a.seq[-overlap_length:] == b.seq[:overlap_length]:
            return overlap_length  # Return length of overlap if any overlap exists
    return 0  # Return 0 if no overlap exists


seq1 = 'GAGATCAT'
seq2 = 'ATCATTT'

dna1 = DnaSeq('seq1_id', seq1)
dna2 = DnaSeq('seq2_id', seq2)

overlap_length = check_exact_overlap(dna1, dna2, min_overlap=10)

# print(f"Längden på överlappet är: {overlap_length}")






## UPPGIFT 4 ##
def overlaps(lst, overlap_function):
    overlaps_dict = {}  # Dictionary to store overlaps

    # Iterate over all unique pairs of DnaSeq objects in the list
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue  # Skip comparing a sequence with itself

            a, b = lst[i], lst[j]
            overlap_length = overlap_function(a, b)  # Check for overlap

            # Record the overlap if its length is greater than 0
            if overlap_length > 0:
                if a.accession not in overlaps_dict:
                    overlaps_dict[a.accession] = {}
                overlaps_dict[a.accession][b.accession] = overlap_length

    return overlaps_dict







## TESTER ## 
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    print(s1)
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == "<DnaSeq accession='s1'>", 'The __str__ method is not following the specification.'
    assert str(s2) == "<DnaSeq accession='s2'>", 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'

    dna2 = read_dna('ex2.fa')
    assert len(dna2) == 6, 'The file "ex2.fa" has exactly 6 sequences, but your code does not return that.'

    covid = read_dna('sars_cov_2.fa')
    assert len(covid[0].seq) == 29903, 'The length of the genome in "sars_cov_2.fa" is 29903, but your code does not return that.'

    print('read_dna passed')


def test_overlap():
   s0 = DnaSeq('s0', 'AAACCC')
   s1 = DnaSeq('s1', 'CCCGGG')
   s2 = DnaSeq('s2', 'TTATCC')
   s3 = DnaSeq('s3', 'CCAGGG')
   s4 = DnaSeq('s4', 'GGGGGGGGAAAGGGGG')
   s5 = DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTAT')

   data1 = [s0, s1, s2, s3]
   assert check_exact_overlap(s0, s1, 2) == 3
   assert check_exact_overlap(s0, s1) == 0
   assert check_exact_overlap(s0, s3, 2) == 2
   assert check_exact_overlap(s1, s2, 2) == 0
   assert check_exact_overlap(s2, s1, 2) == 2
   assert check_exact_overlap(s2, s3, 2) == 2
   assert check_exact_overlap(s4, s5, 1) == 0, 'Do not allow "internal" substrings to overlap. s4 and s5 does not have an overlap.'
   assert check_exact_overlap(s4, s5, 2) == 0
   assert check_exact_overlap(s4, s5, 3) == 0
   assert check_exact_overlap(s5, s2, 1) == 4

   res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
   assert len(res0) == 2, 'You get the wrong number of overlaps'
   assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

   dna_data = read_dna('ex1.fa')
   res1 = overlaps(dna_data, check_exact_overlap)
   assert len(res1) == 5
   for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                       ('s4', 's5')]:
       assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
   print('overlap code passed')



def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')

# Uncomment this to test everything:
test_all()
