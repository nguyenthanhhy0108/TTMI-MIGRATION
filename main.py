import argparse
import os
import subprocess

def get_max_version():
    files = os.listdir("migration/core")
    
    migration_files = [f for f in files if f.endswith('-up.py') and f[:6].isdigit()]
    
    versions = [int(f[:6]) for f in migration_files]
    
    if versions:
        max_version = max(versions)
        return max_version 
    else:
        return 0

def save_version_to_file(version, file_path="__version__.txt"):
    with open(file_path, 'w') as f:
        f.write(str(version))

def load_version_from_file(file_path="__version__.txt"):
    try:
        with open(file_path, 'r') as f:
            version = int(f.read().strip())
        return version
    except FileNotFoundError:
        return 0
    except ValueError:
        print(f"Invalid version data in {file_path}.")
        return None

def run_migrate_up(version):
    path = 'migration.core'
    files = os.listdir("migration/core")
    migration_files = [f for f in files if f.endswith('-up.py') and f[:6].isdigit()]

    for migration_file in migration_files:
        if int(migration_file[:6]) == version:
            result = subprocess.run(f"python -m {path}.{migration_file[:-3]}",shell=True,text=True)
            print(result.stderr)
            return

def run_migrate_down(version):
    path = 'migration.core'
    files = os.listdir("migration/core")
    migration_files = [f for f in files if f.endswith('-down.py') and f[:6].isdigit()]

    for migration_file in migration_files:
        if int(migration_file[:6]) == version:
            result = subprocess.run(f"python -m {path}.{migration_file[:-3]}",shell=True,text=True)
            print(result.stderr)
            return


def migrate(version):
    version = int(version)
    current_version = int(load_version_from_file())
    while (current_version < version):
        current_version += 1
        run_migrate_up(current_version)

    while (current_version > version):
        run_migrate_down(current_version)
        current_version -= 1

    save_version_to_file(version)


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Migration")

    # Add command-line arguments
    parser.add_argument("-v", "--version", type=str, help="migration version", required=False)

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments
    if args.version:
        migrate(args.version)
        return
    else:
        migrate(get_max_version())
        return

if __name__ == "__main__":
    main()
