# -*- coding: utf-8 -*-
"""
Tests for the NWChem input plugins.
"""
import os
import tempfile

from aiida.djsite.db.testbase import AiidaTestCase
from aiida.common.folders import SandboxFolder
from aiida.orm import CalculationFactory
from aiida.orm import DataFactory
from aiida.parsers.plugins.codtools.ciffilter import CiffilterParser
import aiida
from django.utils import unittest

from aiida.orm.calculation.job.nwchem.nwcpymatgen import _prepare_pymatgen_dict
from aiida.orm.data.structure import has_ase
from aiida.orm.data.cif import has_pycifrw

__copyright__ = u"Copyright (c), 2015, ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE (Theory and Simulation of Materials (THEOS) and National Centre for Computational Design and Discovery of Novel Materials (NCCR MARVEL)), Switzerland and ROBERT BOSCH LLC, USA. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file"
__version__ = "0.4.1"
__contributors__ = "Andrea Cepellotti, Andrius Merkys, Giovanni Pizzi"

class TestNwchem(AiidaTestCase):

    @unittest.skipIf(not has_ase(),"Unable to import ASE")
    def test_1(self):
        from ase import Atoms

        par = {
            'directives': [
                ['set nwpw:minimizer', '2'],
                ['set nwpw:psi_nolattice', '.true.'],
                ['set includestress', '.true.']
            ],
            'geometry_options': [
                'units',
                'au',
                'center',
                'noautosym',
                'noautoz',
                'print'
            ],
            'memory_options': [],
            'symmetry_options': [],
            'tasks': [
                {
                    'alternate_directives': {
                        'driver': {'clear': '', 'maxiter': 40},
                        'nwpw': {'ewald_ncut': 8, 'simulation_cell': '\n  ngrid 16 16 16\n end'}
                    },
                    'basis_set': {},
                    'charge': 0,
                    'operation': 'optimize',
                    'spin_multiplicity': None,
                    'theory': 'pspw',
                    'theory_directives': {},
                    'title': None
                }
            ]
        }

        a = Atoms(['Si', 'Si', 'Si' ,'Si', 'C', 'C', 'C', 'C'],
                  cell=[8.277, 8.277, 8.277])
        a.set_scaled_positions([
            (-0.5, -0.5, -0.5),
            (0.0, 0.0, -0.5),
            (0.0, -0.5, 0.0),
            (-0.5, 0.0, 0.0),
            (-0.25, -0.25, -0.25),
            (0.25 ,0.25 ,-0.25),
            (0.25, -0.25, 0.25),
            (-0.25 ,0.25 ,0.25),
        ])

        self.assertEquals(_prepare_pymatgen_dict(par,a),
'''set nwpw:minimizer 2
set nwpw:psi_nolattice .true.
set includestress .true.
geometry units au center noautosym noautoz print
 Si -4.1385 -4.1385 -4.1385
 Si 0.0 0.0 -4.1385
 Si 0.0 -4.1385 0.0
 Si -4.1385 0.0 0.0
 C -2.06925 -2.06925 -2.06925
 C 2.06925 2.06925 -2.06925
 C 2.06925 -2.06925 2.06925
 C -2.06925 2.06925 2.06925
end

title "pspw optimize"
charge 0
basis

end
driver
 clear 
 maxiter 40
end
nwpw
 ewald_ncut 8
 simulation_cell 
  ngrid 16 16 16
 end
end
task pspw optimize
''')
