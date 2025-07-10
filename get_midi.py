import os
import zipfile
from pathlib import Path

def extract_midi_to_single_folder(zip_path, output_dir):
    """
    Extracts all MIDI files from ZIP and puts them directly in one folder.
    Skips empty directories and non-MIDI files.
    
    Args:
        zip_path (str): Path to input ZIP file
        output_dir (str): Output directory for MIDI files
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Supported MIDI extensions (case insensitive)
    midi_extensions = {'.mid', '.midi'}
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get all files in ZIP
        file_list = zip_ref.namelist()
        
        # Counter for renamed duplicates
        counter = 1
        
        for file in file_list:
            # Skip directories
            if file.endswith('/'):
                continue
                
            # Check if file is MIDI (case insensitive)
            file_lower = file.lower()
            if any(file_lower.endswith(ext) for ext in midi_extensions):
                try:
                    # Extract file to memory
                    file_data = zip_ref.read(file)
                    
                    # Create clean filename (no path)
                    base_name = os.path.basename(file)
                    output_path = os.path.join(output_dir, base_name)
                    
                    # Handle duplicate filenames
                    while os.path.exists(output_path):
                        name, ext = os.path.splitext(base_name)
                        output_path = os.path.join(output_dir, f"{name}_{counter}{ext}")
                        counter += 1
                    
                    # Write file directly to output folder
                    with open(output_path, 'wb') as f:
                        f.write(file_data)
                        
                    print(f"Extracted: {base_name} -> {os.path.basename(output_path)}")
                    
                except Exception as e:
                    print(f"Error extracting {file}: {str(e)}")
    
    print(f"\nAll MIDI files extracted to: {output_dir}")

# Example usage:
if __name__ == "__main__":
    # Input ZIP file path (change this to your file)
    input_zip = "/Users/tao-taohe/Desktop/price_songs_main_copy.zip"
    
    # Output directory (will be created if doesn't exist)
    output_directory = "/Users/tao-taohe/Desktop/midis"
    
    # Run extraction
    extract_midi_to_single_folder(input_zip, output_directory)