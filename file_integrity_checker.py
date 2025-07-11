import os
import hashlib
import json
import argparse

HASH_FILE = "file_hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(4096)
            while chunk:
                sha256.update(chunk)
                chunk = f.read(4096)
        return sha256.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def scan_directory(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            file_hash = calculate_hash(path)
            if file_hash:
                hashes[path] = file_hash
    return hashes

def load_previous_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def check_integrity(current, previous):
    added = []
    modified = []
    deleted = []

    for path, hash_val in current.items():
        if path not in previous:
            added.append(path)
        elif hash_val != previous[path]:
            modified.append(path)

    for path in previous:
        if path not in current:
            deleted.append(path)

    return added, modified, deleted

def main(directory=".", update=False):
    print(f"Scanning directory: {directory}")
    current_hashes = scan_directory(directory)
    previous_hashes = load_previous_hashes()

    added, modified, deleted = check_integrity(current_hashes, previous_hashes)

    if update:
        save_hashes(current_hashes)
        print("Hash values updated and saved successfully.")
    else:
        print("\n--- File Integrity Report ---")
        if added:
            print("New files detected:")
            for f in added:
                print(f"  + {f}")
        if modified:
            print("Modified files:")
            for f in modified:
                print(f"  * {f}")
        if deleted:
            print("Deleted files:")
            for f in deleted:
                print(f"  - {f}")
        if not (added or modified or deleted):
            print("No changes detected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan (default: current folder)")
    parser.add_argument("-u", "--update", action="store_true", help="Update hash record")
    args = parser.parse_args()

    main(args.directory, args.update)
