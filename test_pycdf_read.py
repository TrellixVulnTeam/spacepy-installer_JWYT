#!/usr/bin/env python
"""
check demo.cdf file to know if SpacePy CDF read is OK

If CDF libs aren't found after running setup_spacepy.py, try putting at the top:

import os
os.environ['CDF_LIB'] = ~/cdf37_0-dist/lib

or whatever directory CDF is installed under.
"""
from spacepy import pycdf
from pathlib import Path

R = Path(__file__).parent
fn = R / "demo.cdf"


def test_cdf_read():
    if not fn.is_file():
        raise FileNotFoundError(fn)

    h = pycdf.CDF(str(fn))
    vars = list(h.keys())

    assert vars == ["foo", "magic5"]

    foo = h["foo"][:].squeeze()
    assert foo.size == 2
    assert (foo == [42, 43]).all()

    magic5 = h["magic5"][:].squeeze()
    assert magic5.shape == (5, 5)


if __name__ == "__main__":
    test_cdf_read()
    print("OK: SpacePy CDF read")
