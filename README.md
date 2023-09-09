# Host Probe

Host Probe is a Python script that performs host discovery using ICMP ping. It allows you to determine which hosts are up and which are down from a list of IP addresses or domain names.

## Installation

You can use [pipenv](https://pipenv.pypa.io/en/latest/) to create a virtual environment and install the required dependencies. If you don't have pipenv installed, you can install it using pip:

```bash
pip install pipenv
```

Once pipenv is installed, navigate to the project directory and run:

```bash
pipenv install
```

This will create a virtual environment and install the required dependencies listed in the `Pipfile`.

## Usage

```bash
pipenv run python hostprobe.py [OPTIONS]
```

## Options
- `-f, --file FILE`: Input file containing a list of host IP addresses or domain names (one per line). (Required)
- `-r, --retry INT`: Number of ping retries for each host (default: 3).
- `-t, --timeout FLOAT`: Timeout (in seconds) for each ping request (default: 2.0).
- `-o, --output FILE`: Output file for results.
- `-v, --verbose:` Enable verbose output (real-time).
- `-s, --sleep FLOAT`: Sleep interval (in seconds) between probes (default: 0.0).

## Example
Perform host discovery using a host list file named `hostlist.txt`, save the results to `output.txt`, enable verbose (real-time) output, and add a 1-second sleep interval between probes:

```bash
pipenv run python hostprobe.py -f hostlist.txt -o output.txt -v -s 1.0
```

## Dependencies
- [ping3](https://pypi.org/project/ping3/): Python 3 ICMP ping implementation.
- [colorama](https://pypi.org/project/colorama/): Library for colored text output.