#!/bin/bash
OUTPUT_BASE="PATH/TO/alignment_results"

touch scaffoldsCheck.txt
for dir in $(ls -d $OUTPUT_BASE/*/ | head -n 1)/*; do
  # gains species ID from name of species folder
  SPECIES=$(basename "$dir")
  # allows vector to be accessed through another name
  declare -n current_species="CONTIGS${SPECIES}"
  # creates vector for the results from this species
  current_species=()
  for d in $OUTPUT_BASE/*; do
    # creates variable with path to species folder
    LOG_PATH="$d/$SPECIES"
    # finds scaffold in .log file
    mapfile -t -O "${#current_species[@]}" current_species < <(
      awk '/Scaffold:/ {print $2}' "$LOG_PATH"/*.log
    )
  done
  # counts for number of unique items in species/scaffold array
  unique_total=$(printf "%s\n" "${current_species[@]}" | sort -u | wc -l)

  # returns text based on if scaffolds are shared
  if [ "$unique_total" -eq 1 ]; then
    echo "All exons in ${SPECIES} are found on the same scaffold (${current_species[1]})." >> scaffoldsCheck.txt
  else
    echo "Warning: ${SPECIES} contains multiple different scaffolds" >> scaffoldsCheck.txt
    printf "Scaffolds found: %s\n" "$(printf "%s\n" "${current_species[@]}" | sort -u)" >> scaffoldsCheck.txt
  fi
done
