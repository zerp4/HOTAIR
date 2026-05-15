# HOTAIR

Structure is a window into the mechanism and function of an RNA. Therefore, we applied SHAPE-MaP chemical probing to determine the secondary structure of the lncRNA HOTAIR *in cellulo* and *in vitro*. We determined the global architecture of HOTAIR in cells, as well as local structural differences relative to *in vitro*. The structural work was complemented by developing a bioinformatics pipeline to identify HOTAIR loci within primate genomes and then building multiple sequence alignments to evaluate conservation. Our alignments also reveal covariation within a specific structural domain of HOTAIR, providing evidence in favor of functional structural elements in HOTAIR. These results can serve as a roadmap for future mechanistic studies of structure-function relationships in HOTAIR.

This code is provided as-is for reproducibility purposes and may be reused freely under the MIT License. No guarantees are made regarding functionality in other environments or use cases.

## Contents

### Data_input

All data files required to reproduce the analyses in the Jupyter notebooks.

### Reference_sequences

Sequences used for alignment of SHAPE-MaP and MRT-ModSeq sequencing reads.

### Superfold_structures

Final structures of HOTAIR from Superfold for the following samples:
- *in cellulo* SHAPE-MaP rep 1
- *in cellulo* SHAPE-MaP rep 2
- *in cellulo* SHAPE-MaP average
- *in vitro* SHAPE-MaP rep 1
- *in vitro* SHAPE-MaP rep 2
- *in vitro* SHAPE-MaP average
  
### Trees

Phylogenetic tree generated from the full-length MSA of HOTAIR that was clustered by 95% (Maximum Likelihood, General Time Reversible) 

# Structure Pipeline

Analysis of SHAPE-MaP chemical probing data of HOTAIR *in cellulo* and *in vitro*. Includes quality control metrics and identification of structurally significant regions using chemical reactivity and Shannon entropy metrics. To follow along with the analysis, the following files are required:

- HOTAIR_Structure_Probing_Analysis.ipynb
- Data_input/Structure_Analysis/Supplemental_Data_2_HOTAIR_SHAPE-MaP.xlsx
- Data_input/Structure_Analysis/Supplemental_Data_3_HOTAIR_deltaSHAPE.xlsx

# Bioinformatics Pipeline

The bioinformatics pipeline from [https://github.com/pylelab/NcRNA_Evolution_in_Primates] was applied to HOTAIR to generate the alignments in **Step 1. Genome Searches**. All subsequent steps are based on those alignments. All files required for the analysis in HOTAIR_Conservation_and_Covariation_Analysis.ipynb are included in the subfolders of Data_input/Bioinformatics_Pipeline.

## Step 1. Genome Searches

### 1.1 Full-length Search

MSA generated from searching 190 primate genomes with full-length hHOTAIR.

### 1.2 Exon-aware Searches

MSAs generated from searching 190 primate genomes with subsequences of hHOTAIR:
- Exons 2-4
- Exons 4-6
- Exon 7

## Step 2. Scaffold Validation

### 2.1_Scaffold_Checks

Check that the best hits from the three exon-aware searches are on the same scaffold. Remove any that are not.

```
./check_exon_scaffolds.sh
```

### 2.2_MSAs_of_Exons_on_Same_Scaffold

MSAs generated from exon-aware searches after scaffold validation

### 2.3_Conservation_Results

Per column and per-nucleotide information content and non-gapped frequency for the MSAs in **Step 2.2**.

## Step 3. Concatenate MSA

MSA generated after combining exons 2-7 to concatenate the full transcript.

## Step 4. Divergence Group MSAs

The following alignments are included. Primate alignments were extracted from the final alignment in **Step 3**.
- human_mouse
- primates_9MYA
- primates_19MYA
- primates_29MYA
- primates_43MYA
- primates_69MYA
- primates_74MYA

## Step 5. Clustering

The alignment in **Step 3** was further processed by clustering based on various sequence similarity thresholds (95, 98, and 99%). A subalignment of Domain 3 was also extracted from the full-length, 95% clustered MSA.

## Step 6. Covariation Analysis

### 6.1_Prepare_MSAs_with_SS

Preparation of MSAs as suitable input to R-scape.

SS denotes MSAs with the replicate-averaged *in cellulo* secondary structure of HOTAIR

### 6.2_R-scape_Output

Raw output of R-scape run with different alignments and parameters.

### 6.3_R-scape_Results

Processed R-scape results with covarying base pairs.

## References

- Primate genomes:\
  Kuderna LFK, Gao H, Janiak MC, et al. A global catalog of whole-genome diversity from 233 primate species. Science. 2023;380(6648):906-913. doi:10.1126/science.abn7829

 - Pipeline development:\
   Beeram et al., GitHub: [https://github.com/pylelab/NcRNA_Evolution_in_Primates]

 - Structure tools:\
   ShapeMapper2 (Busan and Weeks 2018)\
   SuperFold (Reuter and Mathews 2010)\
   deltaSHAPE (Smola et al. 2015)\

 - Bioinformatics tools:\
   Exonerate (version 2.4.0) with the est2genome model (Slater and Birney 2005)\
   MAFFT (version 7.526, --auto flag) (Katoh and Standley 2013)\
   Esl-alistat and Esl-reformat in HMMER (version 3.4)\
   Clustal Omega (Madeira et al. 2024)\
   UGENE (version 52.0) (Okonechnikov et al.  2012)\
   CD-HIT-EST (version 4.8.1) (Li and Godzik 2006; Fu et al. 2012)\
   R-scape (version 0.2.1) (Rivas and Eddy)

- AI was used to assist with coding and debugging.
