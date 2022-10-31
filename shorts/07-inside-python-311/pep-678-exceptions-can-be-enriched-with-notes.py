# PEP 678: Exceptions can be enriched with notes

# The add_note() method is added to BaseException. It can be used to enrich
# exceptions with context information that is not available at the time when
# the exception is raised. The added notes appear in the default traceback.

def some_system_func(val):
    # noinspection PyUnusedLocal
    x = val * 2
    raise ValueError("Cannot convert to text")


# noinspection PyUnresolvedReferences
def our_function(val):
    try:
        results = some_system_func(val)
        return results > 0
    except ValueError as ve:
        ve.add_note(f"This didn't work for value '{val}'")
        raise


if __name__ == '__main__':
    our_function("abc")
