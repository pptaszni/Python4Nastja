"""
© Copyright CERN 2019.  All rights reserved. This software is released under a CERN proprietary
software licence. Any permission to use it shall be granted in writing. Requests shall be
addressed to CERN through mail-KT@cern.ch

Author: Pawel Ptasznik CERN EN/SMM/MRO
"""
from .context import example_module # pylint: disable=E0611

def test_square_returns_correct_square_for_32(): # pylint: disable=invalid-name
    assert example_module.helpers.square(32) == 1024
