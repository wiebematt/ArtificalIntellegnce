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
        ('', '', 'fc_forall.krb'):
            [1476842048.193, 'fc_forall_fc.py'],
        ('', '', 'family.kfb'):
            [1476842048.198, 'family.fbc'],
        ('', '', 'bc_forall.krb'):
            [1476842048.211, 'bc_forall_bc.py'],
    },
                                 compiler_version)
