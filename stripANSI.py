from re import sub

r""" Documented RegEx for my sainty and yours :)
        \x1B                  # literal ESC
        [\[()#;?]*            # Match a single character present in set until it can't anymore
        (?:                   # Non-capturing group
            [0-9]{1,4}        # Match any number 0 - 9, 1 to 4 times (greedy)
            (?:               # Non-capturing group
                ;             # literal ;
                [0-9]{0,4}    # Match any number 0 - 9, 0 to 4 times (greedy)
            )                 # End of Non-capturing group
            *                 # Quantifier repeating until it can't
        )                     # End of Non-capturing group
        ?                     # Quantifier repeating until it can't
        [0-9A-ORZcf-nqry=><]  # Match a single character present in set
"""
ANSI_REGEX = r"\x1B[\[()#;?]*(?:[0-9]{1,4}(?:;[0-9]{0,4})*)?[0-9A-ORZcf-nqry=><]"

def stripANSI(s: str) -> str: return sub(ANSI_REGEX, "", s)

# Prints "Hello World"
if __name__ == "__main__": 
    print(stripANSI("\x1B[31mH\x1B[0m\x1B[32me\x1B[0m\x1B[33ml\x1B[0m\x1B[34ml\x1B[0m\x1B[35mo\x1B[0m\x1B[36m \x1B[0m\x1B[31mW\x1B[0m\x1B[32mo\x1B[0m\x1B[33mr\x1B[0m\x1B[34ml\x1B[0m\x1B[35md\x1B[0m"))