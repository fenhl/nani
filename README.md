**nani** is a Python 3 script that provides an information overview for a given command line tool. It currently only calls `type`, but future versions will display more information, such as usage patterns or man pages.

Requirements
============

To run nani, you will need [docopt][].

[docopt]: http://docopt.org/ (docopt)

Usage
=====

It is recommended that you move `nani.py` to your [`PATH`][PATH] and rename it to `nani`. Then, call `nani` from the command line, with the command you want to learn more about as its argument. For example:

    nani nano

[PATH]: http://en.wikipedia.org/wiki/PATH_(variable) (Wikipedia: PATH (variable))
