import warnings
from mwk_traceback import compact_warn, super_compact_warn


def test_warn():

    warnings.formatwarning = compact_warn

    warnings.warn('This is warning', UserWarning)

    warnings.formatwarning = super_compact_warn

    warnings.warn('This is another warning', UserWarning)
