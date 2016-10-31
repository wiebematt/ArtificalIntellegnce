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
        ('', '', 'pattern_matching.krb'):
            [1477766260.113, 'pattern_matching_bc.py'],
        ('', '', 'questions.kqb'):
            [1477766260.16, 'questions.qbc'],
    },
                                 compiler_version)
