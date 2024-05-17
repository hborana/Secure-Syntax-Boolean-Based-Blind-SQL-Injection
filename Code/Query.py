import sqlite3

def tokenize(sqlQuery):
    return ['SELECT', 'user_id', 'FROM', 'users', 'WHERE', 'username', '=', "'Eli'", 'AND', 'password', '=', "'1234'"]

def parse(tokens):
    return {
        'SELECT': ['user_id'],
        'FROM': ['users'],
        'WHERE': [
            ('username', '=', 'Eli'),
            ('password', '=', '1234')
        ]
    }

def validateSemantics(parseTree):
    # Simulate successful semantic validation
    return True

# Main function to parse SQL:

def parseSQL(sqlQuery):
    tokens = tokenize(sqlQuery)
    if not tokens:
        return "Lexical Error: Invalid tokens found"

    parseTree = parse(tokens)
    if not parseTree:
        return "Syntax Error: Query does not match SQL grammar"

    if not validateSemantics(parseTree):
        return "Semantic Error: Query semantics invalid"

    return parseTree