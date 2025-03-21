import importlib
import os
import config
from datetime import datetime

# Ensure results directory exists
os.makedirs(config.RESULTS_DIR, exist_ok=True)

def run_scan(domain):
    """Run all enabled scan modules on a domain"""
    # Create a directory for this domain inside results/
    domain_dir = os.path.join(config.RESULTS_DIR, domain)
    os.makedirs(domain_dir, exist_ok=True)

    # Timestamped output file inside the domain folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(domain_dir, f"{domain}_{timestamp}.txt")

    with open(output_file, "w") as out:
        out.write(f"Scan results for {domain} - {timestamp}\n\n")

        for module_name in config.SCAN_MODULES:
            try:
                module = importlib.import_module(f"modules.{module_name}")
                out.write(f"[+] Running {module_name.upper()} scan...\n")
                result = module.scan(domain)
                out.write(result + "\n\n")
            except Exception as e:
                out.write(f"[-] Error running {module_name}: {e}\n\n")

    print(f"Scan completed for {domain}, results saved to {domain_dir}/")
