import subprocess

def scan(domain):
    """Run an Nmap scan and return results"""
    cmd = f"nmap -Pn -sV {domain}"
    return subprocess.getoutput(cmd)
