#!/usr/bin/env python3
"""
mirror_packages.py
-------------------

Utility script to download a set of Python packages from PyPI into a local
directory.  Use this script to build a mini‑mirror of critical packages
defined in ``requirements.txt`` so that you always have access to known‑good
archives.  The script reads the package list from the adjacent
``requirements.txt`` file, creates a ``packages`` directory if it does not
exist and uses ``pip download`` to fetch each archive without installing it.

Usage::

    python mirror_packages.py

You can then install packages from the ``packages`` directory with::

    pip install --no-index --find-links=packages <package>

This will force pip to look only in your local mirror rather than contacting
the public PyPI repository.
"""

import os
import subprocess
import sys
from pathlib import Path



def read_requirements(file_path: str = "requirements.txt") -> list[str]:
    """Read package names from a requirements file.

    Lines starting with ``#`` are ignored, and empty lines are skipped.

    Args:
        file_path: Path to the requirements file.

    Returns:
        A list of package names or package==version strings.
    """
    reqs: list[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            reqs.append(line)
    return reqs


def download_packages(packages: list[str], dest_dir: str = "packages") -> None:
    """Download each package into the given destination directory.

    Args:
        packages: A list of package specifiers.
        dest_dir: Directory into which packages will be downloaded.

    Raises:
        subprocess.CalledProcessError: If ``pip download`` fails for a package.
    """
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    for pkg in packages:
        print(f"Downloading {pkg}...")
        cmd = [sys.executable, "-m", "pip", "download", "--dest", dest_dir, pkg]
        subprocess.check_call(cmd)
    print(f"Downloaded {len(packages)} package(s) into {dest_dir}")


def main() -> None:
    """Entry point for the script."""
    requirements_file = Path(__file__).parent / "requirements.txt"
    if not requirements_file.exists():
        print(f"Error: requirements file {requirements_file} not found", file=sys.stderr)
        sys.exit(1)
    packages = read_requirements(str(requirements_file))
    if not packages:
        print("No packages found in requirements file.")
        return
    download_packages(packages)


if __name__ == "__main__":
    main()
