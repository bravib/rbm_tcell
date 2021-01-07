## Python3 codes for RBM-based analysis of T-cell repertoires ##

Python3 codes to implement Restricted Boltzmann Machine (RBM)-based analyses described in Bravi et al. 2021 to identify antigen-specific T-cell receptors and characterize their sequence motifs.

The publication of research using this software, modified or not, must include appropriate citations to: Bravi et al. [reference to define] 


## Codes provided ##

- Folder Align_utils -> The alignment routines require matlab and matlab engine API for Python https://fr.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

- Folder Notebooks -> list of notebooks, each implementing a part of the analyses in Bravi et al. 2021: estimation of response scores and their correlation to clonal fold change between pre- and post-antigen stimulation; comparison of different repertoires from Balachandran et al. Nature 2017 in terms of scores of specificity; estimation of diversity index and correlation to model's performance at discriminating specific from generic receptors; dimensionality reduction of responding clones and visualization of sequence motifs underlying response (also for receptors specific to viral epitopes from Dash et al. Nature 2017 and Glanville et al. Nature 2017).

The notebooks reproduce some figures from Bravi et al. 2021, directly using the datasets and the trained models provided in the folders Data and Models 

- Folder Example: Notebook explaining step-by-step the construction of count-weighted datasets; sequence alignment; RBM and RBM-LR (Left-right version) training; estimation of response and specificity scores.
