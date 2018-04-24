'''This module has a similar scope to os.path, containing utility
functions for dealing with paths in Blender.'''

def abspath(*argv):
	'''Returns the absolute path relative to the current blend file
using the "//" prefix.

:arg start: Relative to this path,
   when not set the current filename is used.
:type start: string or bytes
:arg library: The library this path is from. This is only included for
   convenience, when the library is not None its path replaces *start*.
:type library: :class:`bpy.types.Library`'''

def basename(*argv):
	'''Equivalent to os.path.basename, but skips a "//" prefix.

Use for Windows compatibility.'''

def clean_name(*argv):
	'''Returns a name with characters replaced that
may cause problems under various circumstances,
such as writing to a file.
All characters besides A-Z/a-z, 0-9 are replaced with "_"
or the *replace* argument if defined.'''

def display_name(*argv):
	'''Creates a display string from name to be used menus and the user Interface.
Capitalize the first letter in all lowercase names,
mixed case names are kept as is. Intended for use with
filenames and module names.'''

def display_name_from_filepath(*argv):
	'''Returns the path stripped of directory and extension,
ensured to be utf8 compatible.'''

def ensure_ext(*argv):
	'''Return the path with the extension added if it is not already set.

:arg ext: The extension to check for, can be a compound extension. Should
          start with a dot, such as '.blend' or '.tar.gz'.
:type ext: string
:arg case_sensitive: Check for matching case when comparing extensions.
:type case_sensitive: bool'''

extensions_audio = frozenset
extensions_image = frozenset
extensions_movie = frozenset
def is_subdir(*argv):
	'''Returns true if *path* in a subdirectory of *directory*.
Both paths must be absolute.

:arg path: An absolute path.
:type path: string or bytes'''

def module_names(*argv):
	'''Return a list of modules which can be imported from *path*.

:arg path: a directory to scan.
:type path: string
:arg recursive: Also return submodule names for packages.
:type recursive: bool
:return: a list of string pairs (module_name, module_file).
:rtype: list'''

def native_pathsep(*argv):
	'''Replace the path separator with the systems native ``os.sep``.'''

def reduce_dirs(*argv):
	'''Given a sequence of directories, remove duplicates and
any directories nested in one of the other paths.
(Useful for recursive path searching).

:arg dirs: Sequence of directory paths.
:type dirs: sequence
:return: A unique list of paths.
:rtype: list'''

def relpath(*argv):
	'''Returns the path relative to the current blend file using the "//" prefix.

:arg path: An absolute path.
:type path: string or bytes
:arg start: Relative to this path,
   when not set the current filename is used.
:type start: string or bytes'''

def resolve_ncase(*argv):
	'''Resolve a case insensitive path on a case sensitive system,
returning a string with the path if found else return the original path.'''


