## from Stefan Janssen (https://groups.google.com/d/msg/qiime-forum/9hVlnyBpNQU/pRsONxJ3CgAJ)
import numpy as np
import pandas as pd
import biom

filename_input = 'seqs.biom'
filename_output_include = 'include.txt'
filename_output_exclude = 'exclude.txt'

# read the biom table and convert it into a pandas dataframe
def biom2pandas(file_biom):
    table = biom.load_table(file_biom)
    return pd.DataFrame(table.matrix_data.T.todense().astype(int), index=table.ids(axis='sample'), columns=table.ids(axis='observation')).T
otus = biom2pandas(filename_input)  # read input file

# filter those OTUs that have at least 10 counts in one of the samples
# otus is the count table, otus >= 10 will tell for each cell (true or false) if the value is at least 10
# .apply(any, axis=1) logically combines all values for each OTU with a logical OR, i.e. if there is one or more True value everything will be True, otherwise False.
include = otus[(otus >= 10).apply(any, axis=1)]

# a logical set operation. The exclude IDs are those that are in the orginal biom table, but not in the include set of OTU IDs.
exclude = set(otus.index) - set(include.index)

# write all OTU IDs that should be kept into a file (one ID per line)
f = open(filename_output_include, 'w')
f.write("\n".join(include.index))
f.close()

# write all OTU IDs that should be filtered out into a file (one ID per line)
f = open(filename_output_exclude, 'w')
f.write("\n".join(exclude))
f.close()
