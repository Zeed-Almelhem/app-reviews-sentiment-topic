import pandas as pd
import os

# Load the large dataset 
large_dataset_path = r''
large_df = pd.read_csv(large_dataset_path)

# Set the desired chunk size
chunk_size = 50000

# Create a directory to save the smaller datasets
output_directory = r''
os.makedirs(output_directory, exist_ok=True)

# Split the large dataset into smaller chunks
for i, chunk in enumerate(pd.read_csv(large_dataset_path, chunksize=chunk_size)):
    output_path = os.path.join(output_directory, f'small_dataset_{i + 1}.csv')
    chunk.to_csv(output_path, index=False)
    print(f'Saved {chunk_size} rows to {output_path}')

print('Splitting and saving complete.')