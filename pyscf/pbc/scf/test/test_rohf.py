#!/usr/bin/env python
# Copyright 2014-2018 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import numpy as np
from pyscf import lib
from pyscf.pbc import gto as pgto
from pyscf.pbc import scf as pscf
from pyscf.pbc.scf import krohf

cell = pgto.Cell()
cell.atom = '''
He 0 0 1
He 1 0 1
'''
cell.basis = '321g'
cell.a = np.eye(3) * 3
cell.mesh = [8] * 3
cell.verbose = 7
cell.output = '/dev/null'
cell.spin = 2
cell.build()

def tearDownModule():
    global cell
    cell.stdout.close()
    del cell

class KnownValues(unittest.TestCase):
    def test_krohf_kernel(self):
        nk = [1, 1, 3]
        kpts = cell.make_kpts(nk, wrap_around=True)
        mf = pscf.KROHF(cell, kpts)
        mf.kernel()
        self.assertAlmostEqual(mf.e_tot, -3.381819789636646, 8)

    def test_rohf_kernel(self):
        mf = pscf.ROHF(cell).run()
        self.assertAlmostEqual(mf.e_tot, -3.3633746534777718, 8)


if __name__ == '__main__':
    print("Tests for PBC ROHF and PBC KROHF")
    unittest.main()
