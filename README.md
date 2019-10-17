# Bat-Diet-Metabarcoding
Supporting Information for manuscript # MEN12770 in Molecular Ecology Resources. Article DOI: 10.1111/1755-0998.12770

Version 5 is the latest version. Tutorial is in the master branch, example data sets are in separate branches to avoid mixing up the necessary files for either Ion Torrent PGM or Illumina MiSeq data analysis.

This pipeline takes metabarcoding data and offers an alternative approach to the standard clustering at 97%. We cluster at 98.5% with the SWARM algorithm to retain rare prey in the data set rather than risk lumping sister taxa into the same operational taxonomic units (OTUs) at the start of the data processing pipeline. In this way, multiple OTUs may be assigned the same taxonomy; however, it still reduces the data set and provides the option to collapse taxa at the end of the pipeline rather than losing rare prey unknowingly.
