import os

def merge_chunks(chunks_dir, output_file):
    part_files = sorted([
        os.path.join(chunks_dir, f)
        for f in os.listdir(chunks_dir)
        if f.endswith('.part') or 'part' in f
    ])

    with open(output_file, 'wb') as output:
        for part_file in part_files:
            with open(part_file, 'rb') as pf:
                output.write(pf.read())
            print(f"Merged: {part_file}")

    print(f"\n✅ Done. Reconstructed file saved as '{output_file}'.")

# Example usage
if __name__ == "__main__":
    merge_chunks("pneumonia_model.h5_chunks", "reconstructed_pneumonia_model.h5")
