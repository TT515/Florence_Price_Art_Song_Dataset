import os
import subprocess

# Renders audio from every musescore file in the given directory
# Renders to .wav file. If the user wishes another format (such as .mp3), change the script accordingly.

# CONFIGURE THESE:
musescore_path = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"  # Change as needed
root_folder = "/yourpath/Florence_Price_Art_Song_Dataset"  # Change as needed

def export_all_mscz_to_wav_recursive(folder_path, mscore_exec):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith(".mscz"):
                input_path = os.path.join(dirpath, filename)
                output_path = os.path.splitext(input_path)[0] + ".wav"
                print(f"Exporting {input_path} to WAV...")
                try:
                    subprocess.run([mscore_exec, input_path, "-o", output_path], check=True)
                    print(f"✓ {filename} exported as {output_path}")
                except subprocess.CalledProcessError as e:
                    print(f"✗ Failed to export {filename}: {e}")

export_all_mscz_to_wav_recursive(root_folder, musescore_path)
