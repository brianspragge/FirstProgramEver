# Dictionary of method counts by category
method_counts = {
    'List Methods': 12,
    'String Methods': 20,
    'Dictionary Methods': 9,
    'Tuple Methods': 2,
    'Set Methods': 13,
    'File Methods': 6,
    'Built-in Functions': 69,
}

# Dictionary of methods with descriptions categorized
methods = {
    'List Methods': {
        'append(x)': 'Adds an item to the end of the list.',
        'clear()': 'Removes all items from the list.',
        'copy()': 'Returns a shallow copy of the list.',
        'count(x)': 'Returns the number of times x appears in the list.',
        'extend(iterable)': 'Extends the list by appending elements from an '
            'iterable.',
        'index(x[, start[, end]])': 'Returns the index of the first item whose '
            'value is equal to x.',
        'insert(i, x)': 'Inserts an item at a given position.',
        'pop([i])': 'Removes and returns the item at the given position in the '
            'list (or the last item if i is not provided).',
        'remove(x)': 'Removes the first item from the list whose value is '
            'equal to x.',
        'reverse()': 'Reverses the elements of the list in place.',
        'sort(key=None, reverse=False)': 'Sorts the items of the list in ' 
            'place.',
    },
    
    'String Methods': {
        'capitalize()': 'Capitalizes the first character of the string.',
        'casefold()': 'Converts the string to lowercase, more aggressive than '
            'lower().',
        'center(width[, fillchar])': 'Centers the string in a field of a given '
            'width.',
        'count(sub[, start[, end]])': 'Returns the number of occurrences of a '
            'substring.',
        'encode(encoding=\'utf-8\', errors=\'strict\')': 'Encodes the string '
            'using the specified encoding.',
        'endswith(suffix[, start[, end]])': 'Returns True if the string ends '
            'with the specified suffix.',
        'expandtabs(tabsize=8)': 'Expands tabs in the string to spaces.',
        'find(sub[, start[, end]])': 'Returns the lowest index where substring '
            'is found, or -1 if not found.',
        'format(*args, **kwargs)': 'Formats the string using the specified '
            'arguments.',
        'index(sub[, start[, end]])': 'Returns the lowest index where '
            'substring is found, or raises ValueError if not found.',
        'isalnum()': 'Returns True if all characters in the string are '
            'alphanumeric.',
        'isalpha()': 'Returns True if all characters in the string are '
            'alphabetic.',
        'isdigit()': 'Returns True if all characters in the string are '
            'digits.',
        'islower()': 'Returns True if all characters in the string are '
            'lowercase.',
        'isnumeric()': 'Returns True if all characters in the string are '
            'numeric.',
        'isprintable()': 'Returns True if all characters in the string are '
            'printable.',
        'isupper()': 'Returns True if all characters in the string are '
            'uppercase.',
        'join(iterable)': 'Joins the elements of an iterable into a single '
            'string.',
        'ljust(width[, fillchar])': 'Left-justifies the string in a field of a '
            'given width.',
        'lstrip([chars])': 'Removes leading characters (space by default).',
        'lower()': 'Converts all characters in the string to lowercase.',
        'upper()': 'Converts all characters in the string to uppercase.',
        'partition(sep)': 'Splits the string at the first occurrence of the '
            'separator.',
        'replace(old, new[, count])': 'Returns a copy of the string with all '
            'occurrences of substring replaced.',
        'rfind(sub[, start[, end]])': 'Returns the highest index where '
            'substring is found, or -1 if not found.',
        'rindex(sub[, start[, end]])': 'Returns the highest index where '
            'substring is found, or raises ValueError if not found.',
        'rjust(width[, fillchar])': 'Right-justifies the string in a field of '
            'a given width.',
        'rsplit(sep=None, maxsplit=-1)': 'Splits the string into a list of '
            'substrings, starting from the right.',
        'rstrip([chars])': 'Removes trailing characters (space by default).',
        'split(sep=None, maxsplit=-1)': 'Splits the string into a list of '
            'substrings.',
        'splitlines([keepends])': 'Splits the string at line breaks.',
        'strip([chars])': 'Removes leading and trailing characters (space by '
            'default).',
        'title()': 'Returns a copy of the string with the first letter of each '
            'word capitalized.',
        'zfill(width)': 'Pads the string with zeros on the left, to a '
            'specified width.',
    },
    
    'Dictionary Methods': {
        'clear()': 'Removes all items from the dictionary.',
        'copy()': 'Returns a shallow copy of the dictionary.',
        'fromkeys(seq[, value])': 'Creates a new dictionary from a sequence of '
            'keys.',
        'get(key[, default])': 'Returns the value for key if key is in the '
            'dictionary; otherwise, default.',
        'items()': 'Returns a view object of dictionary’s key-value pairs.',
        'keys()': 'Returns a view object of dictionary’s keys.',
        'pop(key[, default])': 'Removes and returns the value for key; if key '
            'is not found, returns default if provided.',
        'popitem()': 'Removes and returns a (key, value) pair from the '
            'dictionary.',
        'setdefault(key[, default])': 'Returns the value for key if key is in '
            'the dictionary; otherwise, inserts key with a value of default.',
        'update([other])': 'Updates the dictionary with key-value pairs from '
            'another dictionary or iterable.',
        'values()': 'Returns a view object of dictionary’s values.',
    },
    
    'Tuple Methods': {
        'count(x)': 'Returns the number of occurrences of x in the tuple.',
        'index(x[, start[, end]])': 'Returns the index of the first occurrence '
            'of x in the tuple.',
    },
    
    'Set Methods': {
        'add(elem)': 'Adds an element to the set.',
        'clear()': 'Removes all elements from the set.',
        'copy()': 'Returns a shallow copy of the set.',
        'difference(*sets)': 'Returns a set containing elements present in the '
            'set but not in the specified sets.',
        'discard(elem)': 'Removes an element from the set if it is present.',
        'intersection(*sets)': 'Returns a set containing elements common to '
            'all specified sets.',
        'isdisjoint(set)': 'Returns True if the set has no elements in common '
            'with the specified set.',
        'issubset(set)': 'Returns True if the set is a subset of the specified '
            'set.',
        'issuperset(set)': 'Returns True if the set is a superset of the '
            'specified set.',
        'pop()': 'Removes and returns an arbitrary element from the set.',
        'remove(elem)': 'Removes an element from the set; raises KeyError if '
            'element is not present.',
        'symmetric_difference(set)': 'Returns a set with elements in either '
            'the set or the specified set but not both.',
        'union(*sets)': 'Returns a set with elements from the set and all '
            'specified sets.',
    },
    
    'File Methods': {
        'close()': 'Closes the file.',
        'read(size=-1)': 'Reads and returns the content of the file.',
        'readline(size=-1)': 'Reads and returns a single line from the file.',
        'readlines(hint=-1)': 'Reads and returns a list of lines from the '
            'file.',
        'write(string)': 'Writes a string to the file.',
        'writelines(lines)': 'Writes a list of lines to the file.',
    },

    'Built-in Functions': {
        'abs(x)': 'Returns the absolute value of a number.',
        'all(iterable)': 'Returns True if all elements of an iterable are '
            'true.',
        'any(iterable)': 'Returns True if any element of an iterable is true.',
        'ascii(object)': 'Returns a string containing a printable '
            'representation of an object.',
        'bin(x)': 'Converts an integer to a binary string.',
        'bool([x])': 'Converts a value to a Boolean (True or False).',
        'breakpoint()': 'Stops the program and starts the debugger.',
        'bytearray([source[, encoding[, errors]]])': 'Returns a new array of '
            'bytes.',
        'bytes([source[, encoding[, errors]]])': 'Returns a new bytes object.',
        'callable(object)': 'Checks if an object appears callable (i.e., can '
            'be called as a function).',
        'chr(i)': 'Converts an integer to a Unicode character.',
        'classmethod(func)': 'Converts a method into a class method.',
        'compile(source, filename, mode)': 'Compiles source code into a code '
            'object.',
        'complex([real[, imag]])': 'Creates a complex number.',
        'delattr(object, name)': 'Deletes an attribute from an object.',
        'dict([iterable]) or dict(mapping)': 'Creates a new dictionary.',
        'dir([object])': 'Attempts to return a list of valid attributes for an '
            'object.',
        'divmod(a, b)': 'Returns a tuple containing the quotient and remainder '
            'of dividing two numbers.',
        'enumerate(iterable, start=0)': 'Returns an enumerate object that adds '
            'a counter to an iterable.',
        'eval(expression[, globals[, locals]])': 'Evaluates a Python '
            'expression and returns the result.',
        'exec(object[, globals[, locals]])': 'Executes a dynamically created '
            'Python code.',
        'exit([status])': 'Exits the interpreter.',
        'filter(function, iterable)': 'Filters elements of an iterable based '
            'on a function.',
        'float([x[, base]])': 'Converts a number or string to a floating-point '
            'number.',
        'format(value[, format_spec])': 'Formats a value according to a format '
            'specification.',
        'frozenset([iterable])': 'Returns a new frozenset object, which is an '
            'immutable version of a set.',
        'getattr(object, name[, default])': 'Returns the value of a named '
            'attribute of an object.',
        'globals()': 'Returns a dictionary representing the current global '
            'symbol table.',
        'hasattr(object, name)': 'Checks if an object has a named attribute.',
        'hash(object)': 'Returns the hash value of an object.',
        'help([object])': 'Invokes the built-in help system.',
        'hex(x)': 'Converts an integer to a hexadecimal string.',
        'id(object)': 'Returns the identity of an object.',
        'input([prompt])': 'Reads a line of input from the user.',
        'int([x[, base]])': 'Converts a number or string to an integer.',
        'isinstance(object, classinfo)': 'Checks if an object is an instance '
            'or subclass of a class or type.',
        'issubclass(class, classinfo)': 'Checks if a class is a subclass of '
            'another class.',
        'iter([object[, sentinel]])': 'Returns an iterator object.',
        'len(s)': 'Returns the length of an object.',
        'list([iterable])': 'Creates a new list.',
        'locals()': 'Updates and returns a dictionary representing the current '
            'local symbol table.',
        'map(function, iterable, ...)': 'Applies a function to all items in an '
            'iterable.',
        'max(iterable, *[, key, default])': 'Returns the largest item from an '
            'iterable or among two or more arguments.',
        'memoryview(obj)': 'Returns a memory view object of a given object.',
        'min(iterable, *[, key, default])': 'Returns the smallest item from an '
            'iterable or among two or more arguments.',
        'next(iterator[, default])': 'Retrieves the next item from an '
            'iterator.',
        'object()': 'Returns a new featureless object.',
        'oct(x)': 'Converts an integer to an octal string.',
        'open(file, mode[, buffering])': 'Opens a file and returns a file '
            'object.',
        'ord(c)': 'Returns the Unicode code point for a given character.',
        'pow(x, y[, z])': 'Returns the value of a number raised to a power.',
        'print(*objects, sep=\' \', end=\'\\n\', file=sys.stdout)': 'Prints '
            'objects to the text stream file.',
        'property(fget=None, fset=None, fdel=None, doc=None)': 'Returns a '
            'property attribute.',
        'quit([status])': 'Exits the interpreter.',
        'range([start,] stop[, step])': 'Returns an immutable sequence of '
            'numbers.',
        'repr(object)': 'Returns a string representation of an object.',
        'reversed(seq)': 'Returns a reverse iterator over a sequence.',
        'round(number[, ndigits])': 'Rounds a number to a specified number of '
            'decimal places.',
        'set([iterable])': 'Creates a new set object.',
        'setattr(object, name, value)': 'Sets the value of a named attribute '
            'of an object.',
        'slice(start, stop[, step])': 'Creates a slice object.',
        'sorted(iterable, *, key=None, reverse=False)': 'Returns a new sorted '
            'list from an iterable.',
        'staticmethod(function)': 'Converts a method into a static method.',
        'str(object=\'\', encoding=\'utf-8\', errors=\'strict\')': 'Converts '
            'an object to a string.',
        'sum(iterable, /, start=0)': 'Returns the sum of an iterable or start.',
        'super([type[, object]])': 'Returns a proxy object to delegate method '
            'calls.',
        'tuple([iterable])': 'Creates a new tuple.',
        'type(object) or type(name, bases, dict)': 'Returns the type of an '
            'object or creates a new type.',
        'vars([object])': 'Returns the __dict__ attribute of an object.',
        'zip(*iterables)': 'Returns an iterator of tuples from iterables.',
        '__import__(name, globals=None, locals=None, fromlist=(), level=0)': 
            'Import a module.',
    }
}

# List of learned methods
learned = [
    'append(x)', 'clear()', 'insert(i, x)', 'pop([i])', 'remove(i)', 
    'reverse()', 'sort(key=None, reverse=False)', 'lstrip([chars])', 
    'lower()', 'rstrip([chars])', 'strip([chars])', 'title()', 
    'items()', 'keys()', 'upper()', 'dict()', 'help()', 'len()', 
    'list()', 'print()', 'range()', 'reversed()', 'sorted()', 
    'slice()', 'str()', 'sum()', 'tuple()', 'set([iterable])', 
    'list([iterable])', 'dict([iterable]) or dict(mapping)', 
    'tuple([iterable])', 'sum(iterable, /, start=0)', 'reversed(seq)', 
    'range([start,] stop[, step])', 'min(iterable, *[, key, default])', 
    'max(iterable, *[, key, default])', 'abs(x)', 'index(sub[, start[, end]])',
]

learned_count = str(abs(len(learned)))

# Program's opening statement
print("Be sure to copy/paste methods'/functions' key you've learned into the "
    "learned dictionary.\n\n")


# Print method counts by category
for category, count in method_counts.items():
    print(f"{category}: {count}")
print(f"Learned Methods: ~{learned_count}\n")

# Print methods and descriptions by category
for category, methods_dict in methods.items():
    if any(method in learned for method in methods_dict):
        print(f"{category}:")
        for method, description in methods_dict.items():
            if method in learned:
                print(f"  {method.title()}: {description}")
        print("")




print("\n\n\nProgrammed By:  Brian S.\n\nTools:\n\tPython Crash Course " +
    "2nd Edition!\n\tSublime Text (Scripting software)\n\tChatgpt (Speedline " +
    "dictionary generation and PEP8 cleanup)\n\tText-compare.com (Quickly " +
    "verify Chatgpt wasn't deleting or harming my code unecessarily)")
