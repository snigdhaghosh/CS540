import os
import shutil

# Configurations
source_root = 'separated_output'
destination_folder = 'output/model_output'
target_domain = 'Management_Systems'  # <-- Change domain here

# Ensure destination exists
os.makedirs(destination_folder, exist_ok=True)

# Loop through each model folder
for model_dir in os.listdir(source_root):
    model_path = os.path.join(source_root, model_dir)
    if os.path.isdir(model_path):
        # Look for matching file
        matched = False
        for file in os.listdir(model_path):
            if target_domain in file and file.endswith('.json'):
                src_file = os.path.join(model_path, file)
                dest_file = os.path.join(destination_folder, file)  # file already includes model name
                shutil.copy(src_file, dest_file)
                print(f'Copied: {src_file} -> {dest_file}')
                matched = True
                break
        if not matched:
            print(f'[SKIP] No "{target_domain}" file found in {model_dir}')
