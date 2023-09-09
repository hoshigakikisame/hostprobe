#!/usr/bin/env python3

import argparse
import subprocess
from ping3 import ping
import time
from colorama import Fore, Style

def displayBanner():
    banner = """
██╗░░██╗░█████╗░░██████╗████████╗██████╗░██████╗░░█████╗░██████╗░███████╗
██║░░██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██║░░██║╚█████╗░░░░██║░░░██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██╔══██║██║░░██║░╚═══██╗░░░██║░░░██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
██║░░██║╚█████╔╝██████╔╝░░░██║░░░██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝
    """
    author = "v4lentine"
    twitter = "https://twitter.com/ferdirianrk"
    print(banner)
    print(f"Author : {author}")
    print(f"twitter: {twitter}", end="\n\n")

def main():
    displayBanner()
    parser = argparse.ArgumentParser(description="Host Discovery using ICMP ping")
    parser.add_argument("-f", "--file", required=True, help="Input file containing a list of host IP addresses or domain names (one per line)")
    parser.add_argument("-r", "--retry", type=int, default=3, help="Number of ping retries for each host (default: 3)")
    parser.add_argument("-t", "--timeout", type=float, default=2.0, help="Timeout (in seconds) for each ping request (default: 2.0)")
    parser.add_argument("-o", "--output", help="Output file for results")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output (real-time)")
    parser.add_argument("-s", "--sleep", type=float, default=0.0, help="Sleep interval (in seconds) between probes (default: 0.0)")
    args = parser.parse_args()

    input_file = args.file
    retry_count = args.retry
    timeout_value = args.timeout
    output_file = args.output
    verbose_output = args.verbose
    sleep_interval = args.sleep

    try:
        with open(input_file, "r") as file:
            hosts = [line.strip() for line in file.readlines()]

        output = open(output_file, "w") if output_file else None
        
        for host in hosts:
            if verbose_output:
                print(f"Pinging {host}...")
            for _ in range(retry_count):
                response_time = ping(host, timeout=timeout_value)
                if response_time != False:
                    result = f"{host} is {Fore.GREEN}UP{Style.RESET_ALL} (Response Time: {response_time} ms)"
                    if verbose_output:
                        print(result)
                    if output:
                        output.write(result + "\n")
                    break
            else:
                result = f"{host} is {Fore.RED}DOWN{Style.RESET_ALL}"
                if verbose_output:
                    print(result)
                if output:
                    output.write(result + "\n")
            if sleep_interval > 0:
                time.sleep(sleep_interval)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

