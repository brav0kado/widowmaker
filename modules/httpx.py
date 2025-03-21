import subprocess

def scan(domain):
    """Run HTTPX to detect technologies and status"""
    cmd = f"httpx -title -status -tech-detect -silent -u {domain}"
    return subprocess.getoutput(cmd)
