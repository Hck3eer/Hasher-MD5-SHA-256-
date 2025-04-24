import hashlib

def calculate_hashes(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            sha256 = hashlib.sha256(file_data).hexdigest()
            md5 = hashlib.md5(file_data).hexdigest()
            return sha256, md5
    except Exception as e:
        print(f"Error: Could not read file - {e}")
        return None, None

def main():
    file_path = input("Enter the path to the text file: ")
    sha256, md5 = calculate_hashes(file_path)
    
    if sha256 and md5:
        print(f"\nSHA-256 Hash: {sha256}")
        print(f"MD5 Hash: {md5}")
    else:
        print("Failed to generate hashes.")

if __name__ == "__main__":
    main()
