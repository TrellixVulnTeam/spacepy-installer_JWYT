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
* GNU Make

and then installs SpacePy and verifies SpacePy can read a CDF file.
