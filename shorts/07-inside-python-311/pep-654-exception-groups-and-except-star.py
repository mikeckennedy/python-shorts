# PEP 654: Exception Groups and except*
from tarfile import StreamError

# PEP 654 introduces language features that enable a program to
# raise and handle multiple unrelated exceptions simultaneously.
# The builtin types ExceptionGroup and BaseExceptionGroup make it
# possible to group exceptions and raise them together, and the new
# except* syntax generalizes except to match subgroups of exception groups.

def crazy_async_function():
    raise ExceptionGroup(
     "Something bad",
     [
         ValueError("Cannot read abc as int"),
         FileNotFoundError(),
         StreamError()
     ]
 )

try:
    crazy_async_function()
except* ValueError:
    print("We've hit a ValueError!")
except* KeyError as e:
    print("We've hit a KeyError!")
except* (FileNotFoundError, StreamError) as e:
    e: ExceptionGroup
    for ex in e.exceptions:
        print(f"Another error, something with files: {type(ex).__name__}")







