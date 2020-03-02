import sqlparse


def query_starts_with(query, prefixes):
    """Check if the query starts with any item from *prefixes*."""
    prefixes = [prefix.lower() for prefix in prefixes]
    formatted_sql = sqlparse.format(query.lower(), strip_comments=True)
    return bool(formatted_sql) and formatted_sql.split()[0] in prefixes


def queries_start_with(queries, prefixes):
    """Check if any queries start with any item from *prefixes*."""
    for query in sqlparse.split(queries):
        if query and query_starts_with(query, prefixes) is True:
            return True
    return False


def query_has_where_clause(query):
    """Check if the query contains a where-clause."""
    return any(
        isinstance(token, sqlparse.sql.Where)
        for token_list in sqlparse.parse(query)
        for token in token_list
    )


def is_destructive(queries):
    """Returns if any of the queries in *queries* is destructive."""
    keywords = ('drop', 'shutdown', 'delete', 'truncate', 'alter')
    for query in sqlparse.split(queries):
        if query:
            if query_starts_with(query, keywords) is True:
                return True
            elif query_starts_with(
                query, ['update']
            ) is True and not query_has_where_clause(query):
                return True

    return False
