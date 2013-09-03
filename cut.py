#!/bin/env python

from code import InteractiveConsole
from cutter.utils import bang_compile, cut_as_builtin
import codeop
import os


filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    exec(open(filename).read())


codeop.compile = bang_compile
cut_as_builtin()
InteractiveConsole().interact()
