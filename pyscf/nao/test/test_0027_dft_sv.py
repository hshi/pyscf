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

from __future__ import print_function, division
import os,unittest,numpy as np

class KnowValues(unittest.TestCase):

  def test_dft_sv(self):
    """ Try to run DFT with system_vars_c """
    from pyscf.nao import system_vars_c
    from pyscf.nao.m_comp_dm import comp_dm
    from pyscf.nao.m_fermi_dirac import fermi_dirac_occupations
    
    sv = system_vars_c().init_siesta_xml(label='water', cd=os.path.dirname(os.path.abspath(__file__)))
    ksn2fd = fermi_dirac_occupations(sv.hsx.telec, sv.wfsx.ksn2e, sv.fermi_energy)
    ksn2f = (3-sv.nspin)*ksn2fd
    dm = comp_dm(sv.wfsx.x, ksn2f)
    vxc = sv.vxc_lil(dm, 'LDA,PZ')
  
if __name__ == "__main__": unittest.main()
