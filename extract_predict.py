import json
import os

input_dir = 'model_outputs'
output_dir = 'modified_outputs'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with open(input_path, 'r') as file:
            data = json.load(file)

        for entry in data:
            if 'predict' in entry and isinstance(entry['predict'], list):
                entry['predict'] = entry['predict'][:1]

        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Processed and saved: {output_path}")

print("All files processed successfully!")
