import traceback
import logging
from mwk_traceback import compact_tb as c_tb

traceback.print_exception = c_tb.traceback_print_exception_hook


def test_tb_pr_exc():

    logging.warning('traceback.print_exception checking')

    try:
        x = 1 / 0
    except Exception as exc:
        pass
        logging.exception('Traceback when logging exception')

    logging.exception('There was no exception')
