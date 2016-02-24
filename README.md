# cutter

Cutter is a small python module that add some sugar on top of list like objects to ease list traversal.

## Usage

```python
from cutter import cut

numbers = [
  ['one', 'two', 'three'],
  ['un', 'deux', 'trois'],
  ['uno', 'due', 'tre']
]

>>> cut(numbers)[1]  # Take the second element of every sublist
['two', 'deux', 'due']*

>>> cut(numbers)[1, 2]  # Take the third letter of every second element of every sublist
['o', 'u', 'e'].

>>> cut(numbers)[1][2]  # Idem
['o', 'u', 'e'].

>>> cut(numbers)[1, 2].upper()  # Upper case the third letter of every second element of every sublist
['O', 'U', 'E']

>>> cut(numbers)[...]  # Flatten the list for one level
['one', 'two', 'three', 'un', 'deux', 'trois', 'uno', 'due', 'tre']

>>> cut(numbers)[..., 0]  # First letter of every elements
['o', 't', 't', 'u', 'd', 't', 'u', 'd', 't'].
```

## Syntaxic sugars

There are two syntaxic sugars for an even easier use:

### The |_ syntax

```python
from cutter import _

>>> numbers |_ [1]
['two', 'deux', 'due']*

>>> (numbers |_ [1] |_ [2] |_ .upper)()
['O', 'U', 'E']

>>> numbers |_ [...]
['one', 'two', 'three', 'un', 'deux', 'trois', 'uno', 'due', 'tre']

>>> numbers |_ [..., 0]
['o', 't', 't', 'u', 'd', 't', 'u', 'd', 't'].

```
### The ! syntax
This syntax is meant for use in shells.

It is for example used in [wdb](https://github.com/Kozea/wdb) and the bundled cut.py interpreter.

Cutter provide a `bang_compile` function which is a wrapper of the python builtin `compile` function.


```python
# This code muste be compiled with cutter.utils.bang_compile

>>> numbers!1
['two', 'deux', 'due']*

>>> numbers!1!2!upper()                                                                                                                                                                       
['O', 'U', 'E']

>>> numbers!*
['one', 'two', 'three', 'un', 'deux', 'trois', 'uno', 'due', 'tre']

>>> numbers!*!0
['o', 't', 't', 'u', 'd', 't', 'u', 'd', 't'].
```

This syntax use the python tokenizer and ast to make it work. This is really useful when debugging to inspect list content.

### Use the ! syntax in interpreter

This is at your own risk but you can add:

```python

    try:
        from cutter.utils import bang_compile, cut_as_builtin
        from code import InteractiveConsole
        import codeop
    except ImportError:
        pass
    else:
        sys.ps1 = "\001\033[1;36m\002!\001\033[1;32m\002>> \001\033[1;37m\002"
        codeop.compile = bang_compile
        cut_as_builtin()
        try:
            InteractiveConsole().interact('')
        except Exception:
            from traceback import print_exc
            print_exc()
        sys.exit(0)
```

in your `~/.pythonrc`

### More

Cutter works with dictionaries too:
```python
cut(dict)['key']
```

slices:
```python
cut(list)[:5]
```


For more examples see the test files : [test](/test)

Cutter is compatible with at least: python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy and is licensed under [lgpl v3](http://www.gnu.org/licenses/lgpl.html)
