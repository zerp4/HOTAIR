def add_gaps_to_structure(input_file, output_file):
    # Read the file
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    # Skip header line if it starts with '>' or '#'
    if lines and (lines[0].startswith('>') or lines[0].startswith('#')):
        lines = lines[1:]
    
    if len(lines) < 3:
        print("Error: File must have at least 3 lines (after header)")
        return
    
    original_seq = lines[0]
    structure = lines[1]
    gapped_seq = lines[2]
    
    # Check that original sequence and structure have same length
    if len(original_seq) != len(structure):
        print(f"Warning: Original sequence length ({len(original_seq)}) != structure length ({len(structure)})")
    
    # Build gapped structure
    gapped_structure = []
    seq_pos = 0  # Position in original sequence (and structure)
    
    for char in gapped_seq:
        if char == '-':
            # Gap in alignment - add dot to structure
            gapped_structure.append('.')
        else:
            # Not a gap - copy structure character
            if seq_pos < len(structure):
                gapped_structure.append(structure[seq_pos])
                seq_pos += 1
            else:
                print(f"Warning: Ran out of structure positions at alignment position {len(gapped_structure)}")
                gapped_structure.append('.')
    
    gapped_structure_str = ''.join(gapped_structure)
    
    # Verify lengths match
    print(f"Original sequence length: {len(original_seq)}")
    print(f"Original structure length: {len(structure)}")
    print(f"Gapped sequence length: {len(gapped_seq)}")
    print(f"Gapped structure length: {len(gapped_structure_str)}")
    
    if len(gapped_seq) != len(gapped_structure_str):
        print("ERROR: Gapped sequence and structure lengths don't match!")
        return
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(lines[0] + '\n')
        f.write(lines[1] + '\n')
        f.write(lines[2] + '\n')
        f.write(gapped_structure_str + '\n')
    
    print(f"\nSuccess! Written to {output_file}")
    print(f"Gapped structure: {gapped_structure_str}")

# Usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        print("\nInput file format:")
        print("Line 1: Original sequence")
        print("Line 2: Secondary structure")
        print("Line 3: Gapped sequence")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    add_gaps_to_structure(input_file, output_file)