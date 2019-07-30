#!/usr/bin/env python
import urllib.request
import tarfile
from pathlib import Path
import sys
import shutil
import os
import subprocess

if sys.version_info < (3, 6):
    raise SystemExit("Python >= 3.6 required")

if os.name == "nt":
    raise SystemExit("Windows can use the PyPi wheel: \n pip install spacepy")

make = shutil.which("make")
if not make:
    raise SystemExit("GNU Make not found.")


def url_retrieve(url: str, outfile: Path, overwrite: bool = False):
    """
    Parameters
    ----------
    url: str
        URL to download from
    outfile: pathlib.Path
        output filepath (including name)
    overwrite: bool
        overwrite if file exists
    """
    outfile = Path(outfile).expanduser().resolve()
    if outfile.is_dir():
        raise ValueError("Please specify full filepath, including filename")
    # need .resolve() in case intermediate relative dir doesn't exist
    if overwrite or not outfile.is_file():
        outfile.parent.mkdir(parents=True, exist_ok=True)

        urllib.request.urlretrieve(url, str(outfile))


def setup_spacepy():
    R = Path("~").expanduser()
    # %% download libcdf
    url = "https://spdf.sci.gsfc.nasa.gov/pub/software/cdf/dist/latest-release/cdf-dist-all.tar.gz"

    ofn = R / url.split("/")[-1]

    url_retrieve(url, ofn)

    with tarfile.open(ofn, mode="r") as f:
        f.extractall(R)
    # %% build
    if sys.platform == "linux":
        cmd = "OS=linux ENV=gnu CURSES=no FORTRAN=no UCOPTIONS=-O2 SHARED=yes -j -l4 all".split(
            " "
        )
    elif sys.platform == "darwin":
        print('CDF Makefiles are obsolete and no longer work with current OSX versions. Suggest CDFlib instead.', file=sys.stderr)
        cmd = "OS=macosx ENV=gnu CURSES=no FORTRAN=no UCOPTIONS=-O2 SHARED=yes -j -l4 all".split(
            " "
        )
    else:
        raise SystemExit(f"I dont know how to install SpacePy on {sys.platform}")

    cwd = list(R.glob("cdf*dist"))[0].resolve()
    print(f"\nbuilding CDF in {cwd}\n")
    build_cmd = [make, "-C", str(cwd), "--silent"] + cmd
    print(" ".join(build_cmd), "\n")
    subprocess.check_call(build_cmd)
    subprocess.check_call([make, "-C", str(cwd), "--silent", "install"])  # no sudo
    # %% install spacepy
    subprocess.check_call([sys.executable, "-m", "pip", "install", "spacepy"])
    # %% verify
    print("verifying SpacePy CDF read")

    subprocess.check_call(
        [sys.executable, str(Path(__file__).parent / "test_pycdf_read.py")]
    )


if __name__ == "__main__":
    setup_spacepy()
