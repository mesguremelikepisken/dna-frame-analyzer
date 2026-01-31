# dna-frame-analyzer
Educational DNA reading frame and ORF analysis tool

**DNA Frame Analyzer**

An educational bioinformatics tool written in Python for basic DNA sequence preprocessing and reading frame analysis.
This project focuses on understanding reading frames, start/stop codons, and ORF logic at the DNA level by explicitly showing how these decisions are made.
(This project is intentionally simplified and focuses on conceptual clarity rather than feature completeness.)

**Purpose**

- Practice bioinformatics pipeline thinking
- Translate basic molecular biology rules into Python code
- Understand how reading frame and ORF decisions are made internally
This is a learning-oriented project, not a production-grade analyzer.

**What does this tool do?**

Given a DNA sequence, this tool:
1.  Removes gaps and non-nucleotide characters
2. Generates the three forward reading frames (+0, +1, +2)
3. Scans frames for standard stop codons (TAA, TAG, TGA)
4. Checks for the presence of a start codon (ATG)
5. Reports the most biologically plausible reading frame
   
**Biological assumptions**

This tool is based on standard molecular biology assumptions:
- DNA sequences are read in the 5′ → 3′ direction
- Only complete codons (triplets) are considered biologically meaningful
- Incomplete trailing bases (1–2 nucleotides) are ignored, not treated as stop codons
- A candidate protein-coding ORF must:
  - contain at least one start codon (ATG)
  - not contain a premature stop codon (TAA, TAG, TGA)
Sequences that do not meet these criteria are not considered erroneous;
they are simply treated as non–protein-coding regions.

**How to run**

`python dna_frame_analyzer.py`
You will be prompted to enter a DNA sequence manually.
Example input
`ATG-CGTAA--GCT`
Example output
`Best frame is Frame 2 with sequence: TGCGTAAGCT`
