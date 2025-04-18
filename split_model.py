import os

def split_file(file_path, chunk_size_mb=10):
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    file_name = os.path.basename(file_path)
    output_dir = f"{file_name}_chunks"
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'rb') as f:
        i = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_filename = os.path.join(output_dir, f"{file_name}.part{i:03d}")
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            i += 1
            print(f"Created: {chunk_filename}")

    print(f"\n✅ Done. {i} chunks created in '{output_dir}'.")

# Example usage
if __name__ == "__main__":
    split_file("model/pneumonia_model.h5")
