## Python3 codes for RBM-based analysis of T-cell repertoires ##

Python3 codes to implement Restricted Boltzmann Machine (RBM)-based analyses described in Bravi et al. 2021 to identify condition and epitope-specific T-cell receptors and characterize their sequence motifs from TRB repertoire sequencing data.

The publication of research using this software, modified or not, must include appropriate citations to: Bravi et al., PLoS Comput. Biol. (2021)  

For the implementation of the software SONIA - to infer selection pressures on features of amino acid CDR3 sequences - please visit https://github.com/statbiophys/SONIA

## Codes provided ##

- Folder 'Align_utils': The alignment routines require matlab and matlab engine API for Python https://fr.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

- Folder 'Notebooks': list of notebooks, each implementing a part of the analyses in Bravi et al. 2021: estimation of response scores and their correlation to clonal fold change between pre- and post-antigen stimulation; comparison of different repertoires from Balachandran et al. Nature 2017 in terms of scores of specificity; estimation of diversity index and correlation to model's performance at discriminating specific from generic receptors; dimensionality reduction of responding clones and visualization of sequence motifs underlying response (also for receptors specific to viral epitopes from Dash et al. Nature 2017 and Glanville et al. Nature 2017).

The notebooks reproduce some figures from Bravi et al. 2021, directly using the datasets, the trained RBM models provided in the folders Data and Models and the excel tables with numerical values of all results discussed. These tables are an extended version of the ones available as the paper's Supporting Information. In particular see:
Results_RBM_Visualization: for Figs. 1,2,5,6
Results_RBM_specificity_score: for Figs. 4,8
Results_RBM_response_score: for Figs. 3,8
Results_RBM_dissimilarity_vs_AUC: for Fig. 7

- Folder 'Example': Notebook explaining step-by-step the construction of count-weighted datasets; sequence alignment; RBM and RBM-LR (Left-right version) training; estimation of response and specificity scores.
