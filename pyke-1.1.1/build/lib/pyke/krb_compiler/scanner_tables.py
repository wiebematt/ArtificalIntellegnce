# pyke.krb_compiler.scanner_tables.py. This file automatically created by PLY (version 3.3). Don't edit!
_tabversion = '3.3'
_lextokens = {'AS_TOK': 1, 'LP_TOK': 1, 'FOREACH_TOK': 1, 'TAKING_TOK': 1, 'PYTHON_TOK': 1, 'NUMBER_TOK': 1,
              'DEINDENT_TOK': 1, 'STEP_TOK': 1, 'EXTENDING_TOK': 1, 'ASSERT_TOK': 1, 'ANONYMOUS_VAR_TOK': 1,
              'RP_TOK': 1, 'NOTANY_TOK': 1, 'WITHOUT_TOK': 1, 'INDENT_TOK': 1, 'BC_EXTRAS_TOK': 1, 'CODE_TOK': 1,
              'REQUIRE_TOK': 1, 'IN_TOK': 1, 'TRUE_TOK': 1, 'PLAN_EXTRAS_TOK': 1, 'NOT_NL_TOK': 1, 'NONE_TOK': 1,
              'WHEN_TOK': 1, 'WITH_TOK': 1, 'FALSE_TOK': 1, 'PATTERN_VAR_TOK': 1, 'CHECK_TOK': 1, 'IDENTIFIER_TOK': 1,
              'USE_TOK': 1, 'FC_EXTRAS_TOK': 1, 'STRING_TOK': 1, 'FIRST_TOK': 1, 'NL_TOK': 1, 'FORALL_TOK': 1}
_lexreflags = 0
_lexliterals = '*:,!.='
_lexstateinfo = {'code': 'exclusive', 'checknl': 'exclusive', 'INITIAL': 'inclusive', 'indent': 'exclusive'}
_lexstatere = {'checknl': [('(?P<t_checknl_nl>(\\#.*)?(\\r)?\\n)|(?P<t_checknl_other>[^\\#\\r\\n])',
                            [None, ('t_checknl_nl', 'nl'), None, None, ('t_checknl_other', 'other')])], 'code': [(
                                                                                                                 '(?P<t_code_string>\'\'\'([^\\\\]|\\\\.)*?\'\'\'|"""([^\\\\]|\\\\.)*?"""|\'([^\'\\\\\\n\\r]|\\\\.|\\\\(\\r)?\\n)*?\'|"([^"\\\\\\n\\r]|\\\\.|\\\\(\\r)?\\n)*?")|(?P<t_code_comment>[ \\t\\f\\r]*\\#.*)|(?P<t_code_plan>\\$\\$)|(?P<t_code_pattern_var>\\$[a-zA-Z_][a-zA-Z0-9_]*\\b)|(?P<t_code_continuation>\\\\(\\r)?\\n)|(?P<t_code_open>[{([])|(?P<t_code_close>[]})])|(?P<t_code_symbol>[0-9a-zA-Z_]+)|(?P<t_code_space>[ \\t]+)|(?P<t_code_other>[^][(){}$\\\\\'"\\r\\n0-9a-zA-Z_ \\t]+)|(?P<t_code_NL_TOK>(\\r)?\\n([ \\t]*(\\#.*)?(\\r)?\\n)*[ \\t]*)',
                                                                                                                 [None,
                                                                                                                  (
                                                                                                                  't_code_string',
                                                                                                                  'string'),
                                                                                                                  None,
                                                                                                                  None,
                                                                                                                  None,
                                                                                                                  None,
                                                                                                                  None,
                                                                                                                  None,
                                                                                                                  (
                                                                                                                  't_code_comment',
                                                                                                                  'comment'),
                                                                                                                  (
                                                                                                                  't_code_plan',
                                                                                                                  'plan'),
                                                                                                                  (
                                                                                                                  't_code_pattern_var',
                                                                                                                  'pattern_var'),
                                                                                                                  (
                                                                                                                  't_code_continuation',
                                                                                                                  'continuation'),
                                                                                                                  None,
                                                                                                                  (
                                                                                                                  't_code_open',
                                                                                                                  'open'),
                                                                                                                  (
                                                                                                                  't_code_close',
                                                                                                                  'close'),
                                                                                                                  (
                                                                                                                  't_code_symbol',
                                                                                                                  'symbol'),
                                                                                                                  (
                                                                                                                  't_code_space',
                                                                                                                  'space'),
                                                                                                                  (
                                                                                                                  't_code_other',
                                                                                                                  'other'),
                                                                                                                  (
                                                                                                                  't_code_NL_TOK',
                                                                                                                  'NL_TOK')])],
               'INITIAL': [(
                           '(?P<t_continuation>\\\\(\\r)?\\n)|(?P<t_NL_TOK>(\\r)?\\n([ \\t]*(\\#.*)?(\\r)?\\n)*)|(?P<t_tsqstring>[uU]?[rR]?\'\'\'([^\\\\]|\\\\.)*?\'\'\')|(?P<t_tdqstring>[uU]?[rR]?"""([^\\\\]|\\\\.)*?""")|(?P<t_sqstring>[uU]?[rR]?\'([^\'\\\\\\n\\r]|\\\\.|\\\\(\\r)?\\n)*?\')|(?P<t_dqstring>[uU]?[rR]?"([^"\\\\\\n\\r]|\\\\.|\\\\(\\r)?\\n)*?")|(?P<t_ANONYMOUS_VAR_TOK>\\$_([a-zA-Z_][a-zA-Z0-9_]*)?)|(?P<t_PATTERN_VAR_TOK>\\$[a-zA-Z][a-zA-Z0-9_]*)|(?P<t_IDENTIFIER_TOK>[a-zA-Z_][a-zA-Z0-9_]*)|(?P<t_float>[-+]?([0-9]+(\\.[0-9]*([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)|\\.[0-9]+([eE][-+]?[0-9]+)?))|(?P<t_hexint>[-+]?0[xX][0-9a-fA-F]+)|(?P<t_octalint>[-+]?0[0-7]*)|(?P<t_int>[-+]?[1-9][0-9]*)|(?P<t_LB_TOK>\\[)|(?P<t_LC_TOK>\\{)|(?P<t_LP_TOK>\\()|(?P<t_RB_TOK>\\])|(?P<t_RC_TOK>\\})|(?P<t_RP_TOK>\\))|(?P<t_ignore_comment>\\#.*)',
                           [None, ('t_continuation', 'continuation'), None, ('t_NL_TOK', 'NL_TOK'), None, None, None,
                            None, ('t_tsqstring', 'tsqstring'), None, ('t_tdqstring', 'tdqstring'), None,
                            ('t_sqstring', 'sqstring'), None, None, ('t_dqstring', 'dqstring'), None, None,
                            ('t_ANONYMOUS_VAR_TOK', 'ANONYMOUS_VAR_TOK'), None,
                            ('t_PATTERN_VAR_TOK', 'PATTERN_VAR_TOK'), ('t_IDENTIFIER_TOK', 'IDENTIFIER_TOK'),
                            ('t_float', 'float'), None, None, None, None, ('t_hexint', 'hexint'),
                            ('t_octalint', 'octalint'), ('t_int', 'int'), ('t_LB_TOK', 'LB_TOK'),
                            ('t_LC_TOK', 'LC_TOK'), ('t_LP_TOK', 'LP_TOK'), ('t_RB_TOK', 'RB_TOK'),
                            ('t_RC_TOK', 'RC_TOK'), ('t_RP_TOK', 'RP_TOK'), (None, None)])],
               'indent': [('(?P<t_indent_sp>\\n[ \\t]*)', [None, ('t_indent_sp', 'sp')])]}
_lexstateignore = {'code': '', 'checknl': ' \t', 'INITIAL': ' \t', 'indent': ''}
_lexstateerrorf = {'checknl': 't_ANY_error', 'code': 't_ANY_error', 'INITIAL': 't_ANY_error', 'indent': 't_ANY_error'}
