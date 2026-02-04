# Python Package Backup Mirror

This repository provides a script and guidance for creating a local backup of
critical Python packages.  Maintaining your own mirror ensures that you can
install known‑good versions of popular packages even if the public PyPI
repository is compromised or temporarily unavailable.

## Background

The Top PyPI Packages dataset shows that a handful of libraries account for the
majority of downloads【50887308542579†L76-L87】.  Popular networking and packaging
tools like `boto3`, `urllib3`, `requests`, `setuptools` and `numpy` are
downloaded hundreds of millions of times each month【50887308542579†L76-L87】.
By mirroring these high‑use packages locally, you reduce the risk of
supply‑chain attacks and avoid downtime caused by corrupted package uploads.

## Packages included

The default configuration backs up the following high‑traffic packages (see
the Top PyPI Packages list【50887308542579†L76-L87】 for download counts):

- `boto3`
- `urllib3`
- `botocore`
- `packaging`
- `certifi`
- `typing-extensions`
- `requests`
- `setuptools`
- `idna`
- `charset-normalizer`
- `numpy`
- `python-dateutil`
- `six`
- `pandas`
- `cryptography`
- `pyyaml`
- `cffi`
- `click`
- `pydantic`
- `pytest`
- `jinja2`
- `pillow`
- `wheel`

You can modify `requirements.txt` to add or remove packages.

## # Python Package Backup Mirror

This repository provides a script and guidance for creating a local backup of
critical Python packages.  Maintaining your own mirror ensures that you can
install known‑good versions of popular packages even if the public PyPI
repository is compromised or temporarily unavailable.

## Background

The Top PyPI Packages dataset shows that a handful of libraries account for the
majority of downloads【50887308542579†L76-L87】.  Popular networking and packaging
tools like `boto3`, `urllib3`, `requests`, `setuptools` and `numpy` are
downloaded hundreds of millions of times each month【50887308542579†L76-L87】.
By mirroring these high‑use packages locally, you reduce the risk of
supply‑chain attacks and avoid downtime caused by corrupted package uploads.

## Packages included

The default configuration backs up the following high‑traffic packages (see
the Top PyPI Packages list【50887308542579†L76-L87】 for download counts):

- `boto3`
- `urllib3`
- `botocore`
- `packaging`
- `certifi`
- `typing-extensions`
- `requests`
- `setuptools`
- `idna`
- `charset-normalizer`
- `numpy`
- `python-dateutil`
- `six`
- `pandas`
- `cryptography`
- `pyyaml`
- `cffi`
- `click`
- `pydantic`
- `pytest`
- `jinja2`
- `pillow`
- `wheel`

You can modify `requirements.txt` to add or remove packages.

## Usage

1. Ensure that you have a working installation of Python and pip.
   If `pip` is missing, run:

   ```sh
   python -m ensurepip --upgrade
   ```

2. Run the mirroring script to download the packages listed in
   `requirements.txt` into a local `packages/` directory:

   ```sh
   python mirror_packages.py
   ```

3. Install packages from your local mirror using the `--no-index` flag and
   `--find-links` to point pip to the directory containing the downloaded
   archives.  For example, to install `requests` from the mirror:

   ```sh
   pip install --no-index --find-links=packages requests
   ```

## Notes

* The script downloads the latest version of each package at the time it is
  run.  To pin specific versions, edit `requirements.txt` by appending a
  version specifier (for example, `requests==2.31.0`).
* Large packages (such as `numpy` or `pandas`) can consume significant
  storage.  If you commit downloaded archives to a version control system,
  consider using Git LFS or storing them outside of your repository.Usage

1. Ensure that you have a working installation of Python and pip.
   If `pip` is missing, run:

   ```sh
   python -m ensurepip --upgrade
   ```

2. Run the mirroring script to download the packages listed in
   `requirements.txt` into a local `packages/` directory:

   ```sh
   python mirror_packages.py
   ```

3. Install packages from your local mirror using the `--no-index` flag and
   `--find-links` to point pip to the directory containing the downloaded
   archives.  For example, to install `requests` from the mirror:

   ```sh
   pip install --no-index --find-links=packages requests
   ```

## Notes

* The script downloads the latest version of each package at the time it is
  run.  To pin specific versions, edit `requirements.txt` by appending a
  version specifier (for example, `requests==2.31.0`).
* Large packages (such as `numpy` or `pandas`) can consume significant
  storage.  If you commit downloaded archives to a version control system,
  consider using Git LFS or storing them outside of your repository.
