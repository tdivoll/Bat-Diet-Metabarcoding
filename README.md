# Bat-Diet-Metabarcoding

Supporting Information for manuscript # MEN12770 in ___Molecular Ecology Resources___

Disparities in second‐generation DNA metabarcoding results exposed with accessible and repeatable workflows

    Timothy J. Divoll, Veronica A. Brown, Jeff Kinne, Gary F. McCracken, Joy M. O'Keefe 

First published: 17 February 2018
https://doi.org/10.1111/1755-0998.12770

Version 5 is the latest version of the tutorial. The file is too big to display, but can be accessed by cloning and forking or downloading. 

## Test Data Sets
While the RNotebook tutorial is in the master branch, example data sets are in separate branches to avoid mixing up the necessary files for either Ion Torrent PGM or Illumina MiSeq data analysis.

## Summary

In theis study, we demonstrate the differences when sequencing the same bat fecal DNA extracts (insects, COI gene) with Ion Torrent PGM and Illumina MiSeq. The pipeline takes DNA metabarcoding data and offers an alternative approach to the standard OTU clustering at 97%. We cluster at 98.5% with the SWARM algorithm to retain rare prey in the data set rather than risk lumping sister taxa into the same operational taxonomic units (OTUs) at the start of the data processing pipeline. In this way, multiple OTUs may be assigned the same taxonomy; however, it still reduces the data set and provides the option to collapse taxa at the end of the pipeline rather than losing rare prey unknowingly.

## Unix

We use bash commands to manipulate FASTA files: renaming, organizing, concatenating, and calling tools from FASTX and QIIME.

## Python

We use Python scripts from QIIME to process and filter sequencing files down to a BIOM table.

## R

We use R commands to assign taxonomy to denovo OTUs in the final filtered data set via the 'bold' package, which pull from the [Barcode of Life Database](http://v3.boldsystems.org/)
