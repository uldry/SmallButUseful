#!/bin/bash

# This scripts archives the 5 last versions of a file in a different location

set -e

# Set log file
log_file="C:\\Users\\<NAME>\\<FOLDER>\\logfile.log"

# Set source and destination directories
source_dir="Z:\\<FOLDER>\\"
dest_dir="//<FOLDER>"

# Get the file name
file_name=$(basename "$1")

# Check if source and destination directories exist
if [ ! -d "$source_dir" ] || [ ! -d "$dest_dir" ]; then
  echo "$(date) - Error: Source or destination directory is not available." >> "$log_file"
  echo "Error: Source or destination directory is not available." 
  exit 1
fi

# Check if file exists in source directory
if [ ! -f "$source_dir/$file_name" ]; then
  echo "$(date) - Error: Source file '$file_name' does not exist or partition not mounted." >> "$log_file"
  echo "$Error: File '$file_name' does not exist in source directory '$source_dir'." 
  exit 1
fi

# Check if file exists in destination directory
if [ -f "$dest_dir/$file_name" ]; then
  # Compare files
  if cmp -s "$source_dir/$file_name" "$dest_dir/$file_name"; then
    #echo "$(date) - Skipping copy: Source and destination files are identical." >> "$log_file"
	echo "Skipping copy: Source and destination files are identical." 
    exit 0
  else
    # Archive previous version
    timestamp=$(date -r "$dest_dir/$file_name" "+%Y-%m-%d-%H%M%S")
    echo "$(date) - Archiving previous version with the following date: '${timestamp}'" >> "$log_file"
	echo "Archiving previous version with the following date: '${timestamp}'"
    if ! mv "$dest_dir/$file_name" "$dest_dir/${timestamp}_${file_name}"; then
	 echo "$(date) - Could not rename current file" >> "$log_file"
	 echo "Could not rename current file"
	 exit 1
	fi
  fi
fi

# Copy the new version to the destination
if cp "$source_dir/$file_name" "$dest_dir/${file_name}"; then
 echo "$(date) - Copied '$file_name' to destination directory." >> "$log_file"
 echo "Copied '$file_name' to destination directory."
else
 echo "$(date) - Could not copy to destination" >> "$log_file"
 echo " Could not copy to destination"
 exit 1
fi 


# Keep only the last 5 version
find "$dest_dir" -name "*_$file_name" -type f -printf '%T@ %p\n' | sort -rn | tail -n +6 | cut -d' ' -f2- | xargs -d '\n' rm
#echo "$(date) - Removed old versions of '$file_name' if any." >> "$log_file"
echo "Removed old versions of '$file_name'." 