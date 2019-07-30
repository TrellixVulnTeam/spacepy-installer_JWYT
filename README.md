[![Build Status](https://dev.azure.com/mhirsch0512/spacepy-installer/_apis/build/status/scivision.spacepy-installer?branchName=master)](https://dev.azure.com/mhirsch0512/spacepy-installer/_build/latest?definitionId=7&branchName=master)

# SpacePy install script

SpacePy
[install procedure](https://pythonhosted.org/SpacePy/dependencies.html)
notes that several prereqs are required to get SpacePy installed.
Note that if you just need CDF read/write capability, consider
[CDFlib](https://pypi.org/project/cdflib/),
which is a pure Python CDF library.

```sh
python setup_spacepy.py
```

downloads, compiles and installs NASA CDF library on Linux or MacOS using:

* Python &ge; 3.6
* C compiler
* Fortran complier (for FFnet)
* GNU Make

and then installs SpacePy and verifies SpacePy can read a CDF file.
