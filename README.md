# HOTAIR

Structure is a window into the mechanism and function of an RNA. Therefore, we applied SHAPE-MaP chemical probing to determine the secondary structure of the lncRNA HOTAIR *in cellulo* and *in vitro*. We determined the global architecture of HOTAIR in cells, as well as local structural differences relative to *in vitro*. The structural work was complemented by developing a bioinformatics pipeline to identify HOTAIR loci within primate genomes and then building multiple sequence alignments to evaluate conservation. Our alignments reveal covariation within a specific structural domain of HOTAIR, providing evidence in favor of functional structural elements in HOTAIR. These results can serve as a roadmap for future mechanistic studies of structure-function relationships in HOTAIR.

This code is provided as-is for reproducibility purposes and may be reused freely under the MIT License. No guarantees are made regarding functionality in other environments or use cases.

## Structure

Analysis of SHAPE-MaP chemical probing data of HOTAIR *in cellulo* and *in vitro*. Includes quality control metrics and identification of structurally significant regions using chemical reactivity and Shannon entropy metrics. To follow along with the analysis, the following files are required:

- HOTAIR_Structure_Probing_Analysis.ipynb
- etc...

## Bioinformatics

The bioinformatics pipeline from Beeram et al [link] was applied to HOTAIR to generate the alignments in **1. Exon-aware and Full-length Searches**. All subsequent steps are based on those alignments. To follow along with the analysis, the following files are required:

- HOTAIR_Conservation_and_Covariation_Analysis.ipynb
- etc...

### 1. Exon-aware and Full-length Searches

### 2. Scaffold Validation

### 3. Merge MSA

### 4. Divergence Group MSAs

### 5. Clustering

### 6. Covariation Analysis

## References

AI was used to assist with coding and debugging.
