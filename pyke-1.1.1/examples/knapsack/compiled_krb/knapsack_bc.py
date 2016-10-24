# knapsack_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1


def subseq_done(rule, arg_patterns, arg_context):
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


def subseq_1(rule, arg_patterns, arg_context):
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
                with engine.prove(rule.rule_base.root_name, 'subseq', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "knapsack.subseq_1: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def subseq_2(rule, arg_patterns, arg_context):
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
                with engine.prove(rule.rule_base.root_name, 'subseq', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "knapsack.subseq_2: got unexpected plan from when clause 1"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def knapsack_decision(rule, arg_patterns, arg_context):
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
                with engine.prove(rule.rule_base.root_name, 'subseq', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "knapsack.knapsack_decision: got unexpected plan from when clause 1"
                        if sum(map(lambda x: x[1], context.lookup_data('Knapsack'))) <= context.lookup_data('Capacity'):
                            if sum(map(lambda x: x[2], context.lookup_data('Knapsack'))) >= context.lookup_data('Goal'):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def legal_knapsack(rule, arg_patterns, arg_context):
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
                with engine.prove(rule.rule_base.root_name, 'subseq', context,
                                  (rule.pattern(0),
                                   rule.pattern(1),)) \
                        as gen_1:
                    for x_1 in gen_1:
                        assert x_1 is None, \
                            "knapsack.legal_knapsack: got unexpected plan from when clause 1"
                        if sum(map(lambda x: x[1], context.lookup_data('Knapsack'))) <= context.lookup_data('Capacity'):
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                rule.rule_base.num_bc_rule_failures += 1
        finally:
            context.done()


def populate(engine):
    This_rule_base = engine.get_create('knapsack')

    bc_rule.bc_rule('subseq_done', This_rule_base, 'subseq',
                    subseq_done, None,
                    (pattern.pattern_literal(()),
                     pattern.pattern_literal(()),),
                    (),
                    ())

    bc_rule.bc_rule('subseq_1', This_rule_base, 'subseq',
                    subseq_1, None,
                    (pattern.pattern_tuple((contexts.variable('Item'),), contexts.variable('RestX')),
                     pattern.pattern_tuple((contexts.variable('Item'),), contexts.variable('RestY')),),
                    (),
                    (contexts.variable('RestX'),
                     contexts.variable('RestY'),))

    bc_rule.bc_rule('subseq_2', This_rule_base, 'subseq',
                    subseq_2, None,
                    (contexts.variable('X'),
                     pattern.pattern_tuple((contexts.anonymous('_'),), contexts.variable('RestY')),),
                    (),
                    (contexts.variable('X'),
                     contexts.variable('RestY'),))

    bc_rule.bc_rule('knapsack_decision', This_rule_base, 'knapsack_decision',
                    knapsack_decision, None,
                    (contexts.variable('Pantry'),
                     contexts.variable('Capacity'),
                     contexts.variable('Goal'),
                     contexts.variable('Knapsack'),),
                    (),
                    (contexts.variable('Knapsack'),
                     contexts.variable('Pantry'),))

    bc_rule.bc_rule('legal_knapsack', This_rule_base, 'legal_knapsack',
                    legal_knapsack, None,
                    (contexts.variable('Pantry'),
                     contexts.variable('Capacity'),
                     contexts.variable('Knapsack'),),
                    (),
                    (contexts.variable('Knapsack'),
                     contexts.variable('Pantry'),))


Krb_filename = '..\\knapsack.krb'
Krb_lineno_map = (
    ((16, 20), (8, 8)),
    ((34, 38), (11, 11)),
    ((40, 46), (13, 13)),
    ((59, 63), (16, 16)),
    ((65, 71), (18, 18)),
    ((84, 88), (22, 22)),
    ((90, 96), (24, 24)),
    ((97, 97), (25, 25)),
    ((98, 98), (26, 26)),
    ((111, 115), (30, 30)),
    ((117, 123), (32, 32)),
    ((124, 124), (33, 33)),
)
