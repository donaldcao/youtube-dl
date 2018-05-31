from __future__ import unicode_literals

from youtube_dl.jsinterp2.jsgrammar import Token

tests = [
    {
        'code': 'return 42;',
        'asserts': [{'value': 42}],
        'ast': [(Token.RETURN,
                 (Token.EXPR, [
                     (Token.ASSIGN,
                      None,
                      (Token.OPEXPR, [(Token.MEMBER, (Token.INT, 42), None, None)]),
                      None)
                 ]))]
    },
    {
        'code': ';',
        'asserts': [{'value': None}],
        'ast': [None]
    },
    {
        'code': 'var x5 = function(){return 42;}',
        'asserts': [{'value': 42, 'call': ('x5',)}]
    }
]
