# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None


def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
        ('', '', 'bc_example.krb'):
            [1476737977.828, 'bc_example_bc.py'],
        ('', '', 'family.kfb'):
            [1476737977.843, 'family.fbc'],
        ('', '', 'example.krb'):
            [1476737977.912, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
        ('', '', 'fc_example.krb'):
            [1476737977.958, 'fc_example_fc.py'],
        ('', '', 'bc2_example.krb'):
            [1476737978.023, 'bc2_example_bc.py'],
    },
                                 compiler_version)
