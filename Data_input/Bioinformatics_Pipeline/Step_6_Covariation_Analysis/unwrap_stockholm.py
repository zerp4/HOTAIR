def unwrap_stockholm(input_file, output_file):
    """
    Convert multi-block Stockholm file to single-line format.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    sequences = {}
    header_lines = []
    in_alignment = False
    
    for line in lines:
        line = line.rstrip('\n')
        
        # Keep header and comments
        if line.startswith('# STOCKHOLM') or line.startswith('#') and not line.startswith('#='):
            header_lines.append(line)
            continue
        
        # End marker
        if line.strip() == '//':
            continue
        
        # Empty lines
        if not line.strip():
            continue
        
        # Skip GF, GS, GR annotations for now (could be added if needed)
        if line.startswith('#=GF') or line.startswith('#=GS') or line.startswith('#=GR'):
            continue
        
        # GC annotations (like SS_cons) - skip for now, we'll add manually
        if line.startswith('#=GC'):
            continue
        
        # Sequence lines
        if not line.startswith('#'):
            parts = line.split(None, 1)  # Split on whitespace, max 2 parts
            if len(parts) == 2:
                seq_name, seq_data = parts
                if seq_name not in sequences:
                    sequences[seq_name] = []
                sequences[seq_name].append(seq_data)
    
    # Write output
    with open(output_file, 'w') as f:
        # Write header
        for header in header_lines:
            f.write(header + '\n')
        
        if not header_lines or not any('STOCKHOLM' in h for h in header_lines):
            f.write('# STOCKHOLM 1.0\n')
        
        f.write('\n')
        
        # Write sequences on single lines
        for seq_name, seq_parts in sequences.items():
            full_seq = ''.join(seq_parts)
            f.write(f'{seq_name}    {full_seq}\n')
        
        # Placeholder for SS_cons (user will add manually)
        f.write('#=GC SS_cons    [ADD YOUR STRUCTURE HERE]\n')
        f.write('//\n')
    
    print(f"Unwrapped Stockholm file written to {output_file}")
    print(f"Found {len(sequences)} sequences")
    if sequences:
        first_seq = list(sequences.values())[0]
        seq_length = len(''.join(first_seq))
        print(f"Alignment length: {seq_length}")
        print(f"\nNow replace '[ADD YOUR STRUCTURE HERE]' with your {seq_length}-character secondary structure")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python unwrap_stockholm.py input.sto output.sto")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    unwrap_stockholm(input_file, output_file)