file = open('sequence.fasta', 'r')
lines = file.readlines()
file.close()

sequence_lines = lines[1:]
sequence = ''.join(sequence_lines)
sequence = sequence.replace('\n', '')

print('Sequence loaded successfully.')
print('First 100 bases:', sequence[:100])

count_A = sequence.count('A')
count_T = sequence.count('T')
count_G = sequence.count('G')
count_C = sequence.count('C')

print('No of A:', count_A)
print('No of T:', count_T)
print('No of G:', count_G)
print('No of C:', count_C)

sum_of_GC = count_G + count_C
Total_length = len(sequence)
gc_content = sum_of_GC  / Total_length
gc_content = gc_content * 100
rounded_gc_content = round(gc_content, 2)
gc_text = str(rounded_gc_content)

print('Sum of GC:', sum_of_GC)
print('Total length:', Total_length)
print('GC Content:', gc_text, '%')

window_size = 50
gc_values = []
for i in range(len(sequence) - window_size +1):
    window = sequence[i : i + window_size]

    G_count = window.count('G')
    C_count = window.count('C')
    GC = G_count + C_count
    GC_content_window = GC / window_size
    GC_content_window = GC_content_window * 100
    rounded_GC_content_window = round(GC_content_window, 2)
    gc_values.append(rounded_GC_content_window)

print(gc_values[:10])

# graphical representation:

import matplotlib.pyplot as plt
positions = list(range(len(gc_values)))

plt.figure(figsize=(10, 4))
plt.plot(positions, gc_values)

plt.title('Sliding window GC content across BRCA1 Sequence (WS = 50)')
plt.xlabel('Position in Sequence')
plt.ylabel('GC Content (%)')

plt.savefig('gc_content_plot.png', dpi=300, bbox_inches='tight')

#plt.show()


analysis_sequence = sequence[:200]
position = int(input('Enter mutation position (1 to 200):'))
index = position - 1
new_base = input('Enter new base (A/T/G/C):')
new_base = new_base.upper()
if position < 1 or position > len(analysis_sequence):
    print('Invalid position')
elif new_base not in 'ATGC':
    print('Invalid new base')
else: 
    index = position - 1       
    original_base = analysis_sequence[index]
    sequence_list = list(analysis_sequence)
    sequence_list[index] = new_base

    mutated_sequence = ''.join(sequence_list)
    original_gc = (analysis_sequence.count('G') + analysis_sequence.count('C')) / len(analysis_sequence) * 100
    mutated_gc = (mutated_sequence.count('G') + mutated_sequence.count('C')) / len(mutated_sequence) * 100
    original_gc = round(original_gc, 2)
    mutated_gc = round(mutated_gc, 2)
    gc_difference = round(mutated_gc - original_gc, 2)
    if original_base in 'GC' and new_base in 'AT':
        mutation_type = 'GC to AT change'
    elif original_base in 'AT' and new_base in 'GC':
        mutation_type = 'AT to GC change'
    else:
        mutation_type = 'Same category base change'

    flank_size = 10

    start = max(0, index - flank_size)
    end = min(len(analysis_sequence), index + flank_size + 1)
    original_region = analysis_sequence[start:end]
    mutated_region = mutated_sequence[start:end]

    marker_position = index - start
    marker = ' ' * marker_position + '^'


    print('Original base at position', position, ':', original_base)
    print('Mutated base at position', position, ':', new_base)

    print('Mutation Region:')
    print('Original region:', original_region)
    print('Mutated region :', mutated_region)
    print('                 ' + marker)

    print('Mutation Impact Summary:')
    print('Original 200-base GC Content:', original_gc, '%')
    print('Muatated 200-base GC Content:', mutated_gc, '%')
    print('GC Content Difference:', gc_difference, '%')
    print('Mutation Type:', mutation_type)


    