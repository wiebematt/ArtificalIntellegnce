# pattern_matching_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1


def knows_pattern_matching(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                engine.get_ke('questions', 'pat_master').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_pat_master', context,
                                  ()) \
                        as gen_2:
                    for x_2 in gen_2:
                        assert x_2 is None, \
                            "pattern_matching.knows_pattern_matching: got unexpected plan from when clause 2"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_pattern_matching_2(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'learned_pattern_matching', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_pattern_matching_2: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_pat_master(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_master', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_pat_master: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def learned_pattern_matching(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'taught_pattern_matching', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_pattern_matching', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def taught_pattern_matching_3_5_6_9_15(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_master', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 1"
                        if context.lookup_data('ans') in (3, 5, 6, 9, 15):
                            with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                              ()) \
                                    as gen_3:
                                for x_3 in gen_3:
                                    assert x_3 is None, \
                                        "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 3"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def taught_pattern_matching_7_8_10(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_master', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 1"
                        if context.lookup_data('ans') in (7, 8, 10):
                            with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                              ()) \
                                    as gen_3:
                                for x_3 in gen_3:
                                    assert x_3 is None, \
                                        "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 3"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def taught_pattern_matching_11_12(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_master', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 1"
                        if context.lookup_data('ans') in (11, 12):
                            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                              ()) \
                                    as gen_3:
                                for x_3 in gen_3:
                                    assert x_3 is None, \
                                        "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 3"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def taught_pattern_matching_14(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_master', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 1"
                        if context.lookup_data('ans') in (14,):
                            with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                              ()) \
                                    as gen_3:
                                for x_3 in gen_3:
                                    assert x_3 is None, \
                                        "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 3"
                                    with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                                      ()) \
                                            as gen_4:
                                        for x_4 in gen_4:
                                            assert x_4 is None, \
                                                "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 4"
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_pattern_variable_syntax(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pat_var_syntax', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_pattern_variable_syntax: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def reset_if_wrong__right(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('special', 'claim_goal', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.reset_if_wrong__right: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def reset_if_wrong__wrong(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                engine.get_ke('questions', context.lookup_data('question')).reset()
                rule.rule_base.num_bc_rule_successes += 1
                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_patterns(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_patterns: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variables', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_patterns: got unexpected plan from when clause 2"
                                with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                                  ()) \
                                        as gen_3:
                                    for x_3 in gen_3:
                                        assert x_3 is None, \
                                            "pattern_matching.knows_patterns: got unexpected plan from when clause 3"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_literal_patterns(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_literal_patterns: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def ask_until_correct__ask(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', context.lookup_data('question'), context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 1"
                        with engine.prove('special', 'claim_goal', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def ask_until_correct__try_again(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                engine.get_ke('questions', context.lookup_data('question')).reset()
                print "Try again:"
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_3:
                    for x_3 in gen_3:
                        assert x_3 is None, \
                            "pattern_matching.ask_until_correct__try_again: got unexpected plan from when clause 3"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_pattern_variables(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_pattern_variable_scope(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 1"
                        with engine.prove('questions', 'anonymous_syntax', context,
                                          (rule.pattern(2),)) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 2"
                                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                                  (rule.pattern(3),
                                                   rule.pattern(4),)) \
                                        as gen_3:
                                    for x_3 in gen_3:
                                        assert x_3 is None, \
                                            "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 3"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_how_patterns_match(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'pattern_scope', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'post_process_pattern_scope', context,
                                          (rule.pattern(0),)) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 2"
                                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                                  (rule.pattern(1),
                                                   rule.pattern(2),)) \
                                        as gen_3:
                                    for x_3 in gen_3:
                                        assert x_3 is None, \
                                            "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 3"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_1(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 2"
                                engine.get_ke('questions', 'pattern_scope').reset()
                                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                                  ()) \
                                        as gen_4:
                                    for x_4 in gen_4:
                                        assert x_4 is None, \
                                            "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 4"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_2(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 1"
                        engine.get_ke('questions', 'pattern_scope').reset()
                        with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                          ()) \
                                as gen_3:
                            for x_3 in gen_3:
                                assert x_3 is None, \
                                    "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 3"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_3(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                rule.rule_base.num_bc_rule_successes += 1
                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_4(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 1"
                        with engine.prove('questions', 'same_var_different_rules', context,
                                          (rule.pattern(0),)) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 2"
                                engine.get_ke('questions', 'pattern_scope').reset()
                                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                                  ()) \
                                        as gen_4:
                                    for x_4 in gen_4:
                                        assert x_4 is None, \
                                            "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 4"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_5(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'same_var_different_rules', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 1"
                        engine.get_ke('questions', 'pattern_scope').reset()
                        with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                          ()) \
                                as gen_3:
                            for x_3 in gen_3:
                                assert x_3 is None, \
                                    "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 3"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_pattern_scope_6(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove(rule.rule_base.root_name, 'knows_patterns', context,
                                  ()) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 2"
                                engine.get_ke('questions', 'pattern_scope').reset()
                                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                                  ()) \
                                        as gen_4:
                                    for x_4 in gen_4:
                                        assert x_4 is None, \
                                            "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 4"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_rest_variable(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'rest_pattern_variable_syntax', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_rest_variable: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_rest_variable: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_rest_match(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'rest_match', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_rest_match: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'post_process_rest_match', context,
                                          (rule.pattern(0),)) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_rest_match: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_rest_match_1(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                engine.get_ke('questions', 'rest_match').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                                  ()) \
                        as gen_2:
                    for x_2 in gen_2:
                        assert x_2 is None, \
                            "pattern_matching.post_process_rest_match_1: got unexpected plan from when clause 2"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_rest_match_4_5(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                if context.lookup_data('ans') in (4, 5):
                    with engine.prove('special', 'claim_goal', context,
                                      ()) \
                            as gen_2:
                        for x_2 in gen_2:
                            assert x_2 is None, \
                                "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 2"
                            engine.get_ke('questions', 'rest_match').reset()
                            with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                              ()) \
                                    as gen_4:
                                for x_4 in gen_4:
                                    assert x_4 is None, \
                                        "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 4"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def post_process_rest_match_correct(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                if context.lookup_data('ans') in (2, 3):
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knows_tuple_patterns(rule, arg_patterns, arg_context):
    engine = rule.rule_base.engine
    patterns = rule.goal_arg_patterns()
    if len(arg_patterns) == len(patterns):
        context = contexts.bc_context(rule)
        try:
            if all(itertools.imap(lambda pat, arg:
                                  pat.match_pattern(context, context,
                                                    arg, arg_context),
                                  patterns,
                                  arg_patterns)):
                rule.rule_base.num_bc_rules_matched += 1
                with engine.prove('questions', 'tuple_pattern_syntax', context,
                                  (rule.pattern(0),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 1"
                        with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                          ()) \
                                as gen_2:
                            for x_2 in gen_2:
                                assert x_2 is None, \
                                    "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 2"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def populate(engine):
    This_rule_base = engine.get_create('pattern_matching')

    bc_rule.bc_rule('knows_pattern_matching', This_rule_base, 'knows_pattern_matching',
                    knows_pattern_matching, None,
                    (),
                    (),
                    ())

    bc_rule.bc_rule('knows_pattern_matching_2', This_rule_base, 'knows_pattern_matching',
                    knows_pattern_matching_2, None,
                    (),
                    (),
                    ())

    bc_rule.bc_rule('knows_pat_master', This_rule_base, 'knows_pat_master',
                    knows_pat_master, None,
                    (),
                    (),
                    (pattern.pattern_literal(13),))

    bc_rule.bc_rule('learned_pattern_matching', This_rule_base, 'learned_pattern_matching',
                    learned_pattern_matching, None,
                    (),
                    (),
                    ())

    bc_rule.bc_rule('taught_pattern_matching_3_5_6_9_15', This_rule_base, 'taught_pattern_matching',
                    taught_pattern_matching_3_5_6_9_15, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('taught_pattern_matching_7_8_10', This_rule_base, 'taught_pattern_matching',
                    taught_pattern_matching_7_8_10, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('taught_pattern_matching_11_12', This_rule_base, 'taught_pattern_matching',
                    taught_pattern_matching_11_12, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('taught_pattern_matching_14', This_rule_base, 'taught_pattern_matching',
                    taught_pattern_matching_14, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('knows_pattern_variable_syntax', This_rule_base, 'knows_pattern_variable_syntax',
                    knows_pattern_variable_syntax, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('reset_if_wrong__right', This_rule_base, 'reset_if_wrong',
                    reset_if_wrong__right, None,
                    (contexts.anonymous('_'),
                     contexts.variable('right_ans'),
                     contexts.variable('right_ans'),),
                    (),
                    ())

    bc_rule.bc_rule('reset_if_wrong__wrong', This_rule_base, 'reset_if_wrong',
                    reset_if_wrong__wrong, None,
                    (contexts.variable('question'),
                     contexts.anonymous('_'),
                     contexts.anonymous('_'),),
                    (),
                    ())

    bc_rule.bc_rule('knows_patterns', This_rule_base, 'knows_patterns',
                    knows_patterns, None,
                    (),
                    (),
                    ())

    bc_rule.bc_rule('knows_literal_patterns', This_rule_base, 'knows_literal_patterns',
                    knows_literal_patterns, None,
                    (),
                    (),
                    (pattern.pattern_literal('pat_literal'),
                     pattern.pattern_literal(6),))

    bc_rule.bc_rule('ask_until_correct__ask', This_rule_base, 'ask_until_correct',
                    ask_until_correct__ask, None,
                    (contexts.variable('question'),
                     contexts.variable('right_ans'),),
                    (),
                    (contexts.variable('right_ans'),))

    bc_rule.bc_rule('ask_until_correct__try_again', This_rule_base, 'ask_until_correct',
                    ask_until_correct__try_again, None,
                    (contexts.variable('question'),
                     contexts.variable('right_ans'),),
                    (),
                    (contexts.variable('question'),
                     contexts.variable('right_ans'),))

    bc_rule.bc_rule('knows_pattern_variables', This_rule_base, 'knows_pattern_variables',
                    knows_pattern_variables, None,
                    (),
                    (),
                    ())

    bc_rule.bc_rule('knows_pattern_variable_scope', This_rule_base, 'knows_pattern_variable_scope',
                    knows_pattern_variable_scope, None,
                    (),
                    (),
                    (pattern.pattern_literal('multiple_matching'),
                     pattern.pattern_literal(4),
                     contexts.anonymous('_'),
                     pattern.pattern_literal('anonymous_matching'),
                     pattern.pattern_literal(3),))

    bc_rule.bc_rule('knows_how_patterns_match', This_rule_base, 'knows_how_patterns_match',
                    knows_how_patterns_match, None,
                    (),
                    (),
                    (contexts.variable('ans'),
                     pattern.pattern_literal('anonymous_matching'),
                     pattern.pattern_literal(3),))

    bc_rule.bc_rule('post_process_pattern_scope_1', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_1, None,
                    (pattern.pattern_literal(1),),
                    (),
                    ())

    bc_rule.bc_rule('post_process_pattern_scope_2', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_2, None,
                    (pattern.pattern_literal(2),),
                    (),
                    ())

    bc_rule.bc_rule('post_process_pattern_scope_3', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_3, None,
                    (pattern.pattern_literal(3),),
                    (),
                    ())

    bc_rule.bc_rule('post_process_pattern_scope_4', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_4, None,
                    (pattern.pattern_literal(4),),
                    (),
                    (contexts.anonymous('_'),))

    bc_rule.bc_rule('post_process_pattern_scope_5', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_5, None,
                    (pattern.pattern_literal(5),),
                    (),
                    (contexts.anonymous('_'),))

    bc_rule.bc_rule('post_process_pattern_scope_6', This_rule_base, 'post_process_pattern_scope',
                    post_process_pattern_scope_6, None,
                    (pattern.pattern_literal(6),),
                    (),
                    ())

    bc_rule.bc_rule('knows_rest_variable', This_rule_base, 'knows_rest_variable',
                    knows_rest_variable, None,
                    (),
                    (),
                    (contexts.anonymous('_'),))

    bc_rule.bc_rule('knows_rest_match', This_rule_base, 'knows_rest_match',
                    knows_rest_match, None,
                    (),
                    (),
                    (contexts.variable('ans'),))

    bc_rule.bc_rule('post_process_rest_match_1', This_rule_base, 'post_process_rest_match',
                    post_process_rest_match_1, None,
                    (pattern.pattern_literal(1),),
                    (),
                    ())

    bc_rule.bc_rule('post_process_rest_match_4_5', This_rule_base, 'post_process_rest_match',
                    post_process_rest_match_4_5, None,
                    (contexts.variable('ans'),),
                    (),
                    ())

    bc_rule.bc_rule('post_process_rest_match_correct', This_rule_base, 'post_process_rest_match',
                    post_process_rest_match_correct, None,
                    (contexts.variable('ans'),),
                    (),
                    ())

    bc_rule.bc_rule('knows_tuple_patterns', This_rule_base, 'knows_tuple_patterns',
                    knows_tuple_patterns, None,
                    (),
                    (),
                    (contexts.anonymous('_'),))


Krb_filename = '..\\pattern_matching.krb'
Krb_lineno_map = (
    ((16, 20), (41, 41)),
    ((22, 22), (43, 43)),
    ((23, 28), (44, 44)),
    ((41, 45), (47, 47)),
    ((47, 52), (49, 49)),
    ((65, 69), (52, 52)),
    ((71, 76), (54, 54)),
    ((89, 93), (57, 57)),
    ((95, 100), (59, 59)),
    ((101, 106), (60, 60)),
    ((119, 123), (73, 73)),
    ((125, 130), (75, 75)),
    ((131, 131), (76, 76)),
    ((132, 137), (77, 77)),
    ((150, 154), (80, 80)),
    ((156, 161), (82, 82)),
    ((162, 162), (83, 83)),
    ((163, 168), (84, 84)),
    ((181, 185), (87, 87)),
    ((187, 192), (89, 89)),
    ((193, 193), (90, 90)),
    ((194, 199), (91, 91)),
    ((212, 216), (94, 94)),
    ((218, 223), (96, 96)),
    ((224, 224), (97, 97)),
    ((225, 230), (98, 98)),
    ((231, 236), (99, 99)),
    ((249, 253), (102, 102)),
    ((255, 260), (104, 104)),
    ((273, 277), (108, 108)),
    ((279, 284), (110, 110)),
    ((297, 301), (113, 113)),
    ((303, 303), (115, 115)),
    ((316, 320), (118, 118)),
    ((322, 327), (120, 120)),
    ((328, 333), (121, 121)),
    ((334, 339), (122, 122)),
    ((352, 356), (125, 125)),
    ((358, 364), (127, 127)),
    ((377, 381), (130, 130)),
    ((383, 388), (132, 132)),
    ((389, 394), (133, 133)),
    ((407, 411), (136, 136)),
    ((413, 413), (138, 138)),
    ((414, 414), (139, 139)),
    ((415, 421), (140, 140)),
    ((434, 438), (143, 143)),
    ((440, 445), (145, 145)),
    ((446, 451), (146, 146)),
    ((464, 468), (149, 149)),
    ((470, 476), (151, 151)),
    ((477, 482), (152, 152)),
    ((483, 489), (153, 153)),
    ((502, 506), (156, 156)),
    ((508, 513), (158, 158)),
    ((514, 519), (159, 159)),
    ((520, 526), (160, 160)),
    ((539, 543), (163, 163)),
    ((545, 550), (165, 165)),
    ((551, 556), (166, 166)),
    ((557, 557), (167, 167)),
    ((558, 563), (168, 168)),
    ((576, 580), (171, 171)),
    ((582, 587), (173, 173)),
    ((588, 588), (174, 174)),
    ((589, 594), (175, 175)),
    ((607, 611), (178, 178)),
    ((625, 629), (181, 181)),
    ((631, 636), (183, 183)),
    ((637, 642), (184, 184)),
    ((643, 643), (185, 185)),
    ((644, 649), (186, 186)),
    ((662, 666), (189, 189)),
    ((668, 673), (191, 191)),
    ((674, 674), (192, 192)),
    ((675, 680), (193, 193)),
    ((693, 697), (196, 196)),
    ((699, 704), (198, 198)),
    ((705, 710), (199, 199)),
    ((711, 711), (200, 200)),
    ((712, 717), (201, 201)),
    ((730, 734), (204, 204)),
    ((736, 741), (206, 206)),
    ((742, 747), (207, 207)),
    ((760, 764), (210, 210)),
    ((766, 771), (212, 212)),
    ((772, 777), (213, 213)),
    ((790, 794), (216, 216)),
    ((796, 796), (218, 218)),
    ((797, 802), (219, 219)),
    ((815, 819), (222, 222)),
    ((821, 821), (224, 224)),
    ((822, 827), (225, 225)),
    ((828, 828), (226, 226)),
    ((829, 834), (227, 227)),
    ((847, 851), (230, 230)),
    ((853, 853), (232, 232)),
    ((866, 870), (235, 235)),
    ((872, 877), (237, 237)),
    ((878, 883), (238, 238)),
)
