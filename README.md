# smd-benchmark

Curated single molecule data sets from published studies are provided here for benchmarking algorithms and analysis tools used for single molecule research.  Before new data is added to this repository care has been taken to ensure that files provided comply with the [SMD format](https://smdata.github.io/). Once data has been added to this repository it should not be altered. However, please consult the data verification protocols listed below. When new datasets are added the repository will be taged and a new release issued.

<!--
Download SMD Benchmark Datasets here: [smd-benchmark](https://goo.gl/sMtmAA)
View analytics on datasets: [smd-analytics](https://goo.gl/#analytics/goo.gl/sMtmAA/all_time)
--!>

## Data Sources


PMID_21478155: [Removal of covalent heterogeneity reveals simple folding behavior for P4-P6 RNA](https://www.ncbi.nlm.nih.gov/pubmed/21478155)

PMID_27493222: [Kinetic and thermodynamic framework for P4-P6 RNA reveals tertiary motif modularity and modulation of the folding preferred pathway](https://www.ncbi.nlm.nih.gov/pubmed/27493222)

PMID_TBD: To add your data please contact: http://cmgm.stanford.edu/herschlag/


## Data Verification

It is recommended that before using this data you verify that they match the expected md5 hash value.  The expected md5 values are listed in the file 'md5_hash_values.csv'. Some ways to check if these values are correct are:

1. On linux systems use the md5sum command (e.g. md5sum smddata.json)
2. On Mac OSX use the m5d command (e.g. md5 smddata.json)
3. Use the python script smdview.py included with this repository (e.g. python smdview.py -d smddata.json)
