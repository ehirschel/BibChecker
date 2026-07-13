class patterns:
    acm_pattern_3 = r'''
        ^(?P<authors>
            (?:\b[A-Z]\.|[^.\d])*?     # No periods unless they follow 1 capital letter (initial)            
            ,\s*and\b\s*             # Must find `, and` before last author
            (?:\b[A-Z]\.|[^.\d]+)*?
        )
        [\.]\s*                         # period after authors
            (?P<year>(19|20)\d{2})\b
        [\.]\s*                         # period after year
        (?P<title>
            (?:[^.?]|\.(?!\s))+
        )
        .*$
        '''
    acm_pattern_2 = r'''
            ^
            (?P<authors>
                (?:
                    \b[A-Z]\.                 # allowed initial
                  | (?!\.) .                  # any char except a period
                )*
                \sand\s+(?=[A-Z])             # " and " must occur before first real period
                (?:
                    \b[A-Z]\.
                  | (?!\.) .
                )*
                \b[A-Za-z]{2,}                # final author word
            )
            \.\s*                             # FIRST real period — end of authors
            (?P<year>(19|20)\d{2})
            \.\s*
            (?P<title>[^.]+)                  # title has NO periods
            \.
            .*$
        '''
    acm_pattern_et_al = r'''
            ^(?P<authors>
                (?:\b[A-Z]\.|[^.\d])*?     # same looseness as other patterns
                \bet\s+al\s*\.?                 # literal "et al."
            )
            \s*
            (?P<year>(19|20)\d{2})\b
            [\.]\s*
            (?P<title>
                (?:[^.?]|\.(?!\s))+
            )
            .*$
            '''    

    acm_pattern_1 = r'''
            ^
            (?P<authors>
                (?:
                    \b[A-Z]\.            # single-letter initial
                  | [^.\d]               # anything else but period/digit
                )*
                \b[A-Za-z]{2,}           # final author word (≥2 letters)
            )
            \.\s*
            (?P<year>(19|20)\d{2})
            \.\s*
            (?P<title>[^.]+)
            \.
            .*$
        '''  

    siam_pattern_3 = r'''
            ^
            (?P<authors>
                (?:\s*[^\s,]+(?:\s+[^\s,]+){0,2}\s*,){2,}
                \s*and\s+
                [^\s,]+(?:\s+[^\s,]+){0,2}
            )
            \s*,\s*                    # comma after authors
            (?P<title>.+?)                   # title up to next comma
            \s*,\s*
            (?P<rest>.+?)                    # everything after title
            (?:                              # year may appear in two forms
                \(\s*(?P<year_paren>(19|20)\d{2})\s*\)   # (2015)
              |
                \b(?P<year_plain>(19|20)\d{2})\b         # 2011
            )
            .*$
        '''
    siam_pattern_2 = r'''
            ^
            (?P<authors>
                [^\s,]+(?:\s+[^\s,]+){0,2}
                \s+and\s+
                [^\s,]+(?:\s+[^\s,]+){0,2}
            )
            \s*,\s*                # comma after authors
            (?P<title>.+?)                   # title up to next comma
            \s*,\s*
            (?P<rest>.+?)                    # everything after title
            (?:                              # year may appear in two forms
                \(\s*(?P<year_paren>(19|20)\d{2})\s*\)   # (2015)
              |
                \b(?P<year_plain>(19|20)\d{2})\b         # 2011
            )
            .*$
        '''
    siam_pattern_et_al = r'''
            ^
            (?P<authors>
                [^\s,]+(?:\s+[^\s,]+){0,2}
                \s+et\s+al\.?
            )
            \s*,\s*
            (?P<title>.+?)                   # title up to next comma
            \s*,\s*
            (?P<rest>.+?)                    # everything after title
            (?:                              # year may appear in two forms
                \(\s*(?P<year_paren>(19|20)\d{2})\s*\)   # (2015)
              |
                \b(?P<year_plain>(19|20)\d{2})\b         # 2011
            )
            .*$
        '''
        
    siam_pattern_1 = r'''
            ^
            (?P<authors>
                [^,]+?
            )
            \s*,\s*
            (?P<title>.+?)                   # title up to next comma
            \s*,\s*
            (?P<rest>.+?)                    # everything after title
            (?:                              # year may appear in two forms
                \(\s*(?P<year_paren>(19|20)\d{2})\s*\)   # (2015)
              |
                \b(?P<year_plain>(19|20)\d{2})\b         # 2011
            )
            .*$
        '''

    springer_pattern = r'''
            ^
            (?P<authors>[^:\d]+?)          # authors cannot contain colon
            \s*:\s*
            (?P<title>.*?)
            (?=                          # stop title right before...
                \.\s*                    # 1) a period
              | \s*\(                    # 2) an opening parenthesis
              | \s+(?:19|20)\d{2}\b      # 3) a 4-digit year
            )
            .*$
        '''
    springer_pattern_3 = springer_pattern
    springer_pattern_2 = springer_pattern
    springer_pattern_et_al = springer_pattern
    springer_pattern_1 = springer_pattern

    ieee_pattern = r'^(?P<authors>.*?)\s*[\u201C\u201D"](?P<title>[^"\u201C\u201D]+)[\u201C\u201D"]'
    ieee_pattern_3 = ieee_pattern
    ieee_pattern_2 = ieee_pattern
    ieee_pattern_et_al = ieee_pattern
    ieee_pattern_1 = ieee_pattern


    gen_pattern_3 = r'''
        ^(?P<authors>
            .*?,\s*and\s+.*?[A-Za-z]{2,}\.
            )
            \s+
            (?P<title>
                [^.,]+
            )
            [\.,]
            .*$
            '''
    gen_pattern_2 = r'''
            ^(?P<authors>
                (?:
                    \b[A-Z]\.                 # allowed initial
                  | (?![.]) .                # any char except period or comma
                )*
                \sand\s+(?=[A-Z])             # " and " must occur before first real delimiter
                (?:
                    \b[A-Z]\.
                  | (?![.]) .
                )*
                \b[A-Za-z]{2,}                # final author word
            )
            [\.,]\s*                          # author–title separator: period OR comma
            (?P<title>[^.,]+)                 # title has NO periods or commas
            [\.,]
            .*$
        '''
    gen_pattern_et_al = r'''
            ^
            (?P<authors>
                .*?\bet\s+al\s*\.?
            )
            \s+
            (?P<title>
                [^.,]+
            )
            [\.,]
            .*$
        '''
    # AAAI style: "Last, F.; Last2, F.; and Last3, F. 2020. Title. Venue."
    aaai_pattern_3 = r'''
        ^(?P<authors>
            .+?
            ;\s*and\s+                     # authors are ;-separated, "; and" before last
            .+?
        )
        \.\s*                              # period after authors
        (?P<year>(19|20)\d{2}[a-z]?)       # year, may carry a disambiguator (2020a)
        \.\s*                              # period after year
        (?P<title>(?:[^.]|\.(?!\s))+)
        \.
        .*$
        '''
    aaai_pattern_2 = aaai_pattern_3
    aaai_pattern_et_al = r'''
        ^(?P<authors>
            .+?\bet\s+al\s*\.?             # literal "et al."
        )
        \s*
        (?P<year>(19|20)\d{2}[a-z]?)
        \.\s*
        (?P<title>(?:[^.]|\.(?!\s))+)
        \.
        .*$
        '''
    aaai_pattern_1 = r'''
        ^(?P<authors>
            .+?
        )
        \.\s*
        (?P<year>(19|20)\d{2}[a-z]?)
        \.\s*
        (?P<title>(?:[^.]|\.(?!\s))+)
        \.
        .*$
        '''

    # Start of one AAAI entry ("Last, F.; ...; and Last, F. 2020."), used to
    # split the unnumbered reference list. Surnames may be accented (\p{L}),
    # multi-word, or lowercase particles ("van den Oord"); a corporate author
    # ("OpenAI. 2023.") has no initials at all. regex module syntax.
    _aaai_word = r"[\p{L}][\p{L}’']*(?:-\s*[\p{L}’']+)*"      # may break at a hyphen across lines
    _aaai_initials = r"\p{Lu}\.(?:[-\s]?\p{Lu}\.)*"
    _aaai_name = rf"{_aaai_word}(?:\s+{_aaai_word}){{0,3}},\s*{_aaai_initials}"
    _aaai_org = r"\p{Lu}[\p{L}\d&@-]*(?:\s+\p{Lu}[\p{L}\d&@-]*){0,3}"
    aaai_entry_pattern = rf'''
        (?P<authors>
            (?:{_aaai_name}\s*;\s*)*
            (?:and\s+)?{_aaai_name}
          |
            (?:{_aaai_name}\s*;\s*)+et\s+al\.
          |
            {_aaai_org}\.
        )
        \s*(?P<year>(19|20)\d{{2}}[a-z]?)\.
        '''

    gen_pattern_1 = r'''
            ^
            (?P<authors>
                (?:                             # consume chars that are NOT the boundary start
                    (?!\b[A-Za-z]{2,}[\.])     # don't step over a WORD{2,} + . or , boundary
                    .                           # consume one char
                )*
                \b[A-Za-z]{2,}                  # final word before separator: >= 2 letters
            )
            (?=[\.,])                           # next char must be . or ,
            [\.,]\s*                            # consume the punctuation
            (?P<title>[^.]+)
            .*$
        '''  

