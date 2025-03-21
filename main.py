import os
import config
from modules.scanner import run_scan
from multiprocessing import Pool, cpu_count

def read_domains(file_path):
    """Read domains from a text file"""
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def main():
    """Main function"""
    domains = read_domains(config.DOMAIN_FILE)
    if not domains:
        print("No domains found in the file.")
        return
    
     # Determine the number of processes based on CPU cores
    num_workers = min(len(domains), cpu_count())  # Don't exceed available CPU cores

    print(f"Starting parallel scanning with {num_workers} workers...")

    with Pool(num_workers) as pool:
        pool.map(run_scan, domains)

if __name__ == "__main__":
    main()
