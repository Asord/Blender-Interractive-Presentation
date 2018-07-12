"""This module contains utility functions specific to blender but
not associated with blenders internal data."""

def blend_paths(*argv):
	""".. function:: blend_paths(absolute=False, packed=False, local=False)

Returns a list of paths to external files referenced by the loaded .blend file.

:arg absolute: When true the paths returned are made absolute.
:type absolute: boolean
:arg packed: When true skip file paths for packed data.
:type packed: boolean
:arg local: When true skip linked library paths.
:type local: boolean
:return: path list.
:rtype: list of strings"""

def escape_identifier(*argv):
	""".. function:: escape_identifier(string)

Simple string escaping function used for animation paths.

:arg string: text
:type string: string
:return: The escaped string.
:rtype: string"""

def keyconfig_set(*argv):
	pass

def load_scripts(*argv):
	"""Load scripts and run each modules register function.

:arg reload_scripts: Causes all scripts to have their unregister method
   called before loading.
:type reload_scripts: bool
:arg refresh_scripts: only load scripts which are not already loaded
   as modules.
:type refresh_scripts: bool"""

def make_rna_paths(*argv):
	"""Create RNA "paths" from given names.

:arg struct_name: Name of a RNA struct (like e.g. "Scene").
:type struct_name: string
:arg prop_name: Name of a RNA struct's property.
:type prop_name: string
:arg enum_name: Name of a RNA enum identifier.
:type enum_name: string
:return: A triple of three "RNA paths"
   (most_complete_path, "struct.prop", "struct.prop:'enum'").
   If no enum_name is given, the third element will always be void.
:rtype: tuple of strings"""

def manual_map(*argv):
	pass

def modules_from_path(*argv):
	"""Load all modules in a path and return them as a list.

:arg path: this path is scanned for scripts and packages.
:type path: string
:arg loaded_modules: already loaded module names, files matching these
   names will be ignored.
:type loaded_modules: set
:return: all loaded modules.
:rtype: list"""

def preset_find(*argv):
	pass

def preset_paths(*argv):
	"""Returns a list of paths for a specific preset.

:arg subdir: preset subdirectory (must not be an absolute path).
:type subdir: string
:return: script paths.
:rtype: list"""

import previews
def refresh_script_paths(*argv):
	"""Run this after creating new script paths to update sys.path"""

def register_class(*argv):
	""".. method:: register_class(cls)

Register a subclass of a blender type in (:class:`bpy.types.Panel`,
:class:`bpy.types.UIList`, :class:`bpy.types.Menu`, :class:`bpy.types.Header`,
:class:`bpy.types.Operator`, :class:`bpy.types.KeyingSetInfo`,
:class:`bpy.types.RenderEngine`).

If the class has a *register* class method it will be called
before registration.

.. note::

   :exc:`ValueError` exception is raised if the class is not a
   subclass of a registerable blender class."""

def register_manual_map(*argv):
	pass

def register_module(*argv):
	pass

def resource_path(*argv):
	""".. function:: resource_path(type, major=bpy.app.version[0], minor=bpy.app.version[1])

Return the base path for storing system files.

:arg type: string in ['USER', 'LOCAL', 'SYSTEM'].
:type type: string
:arg major: major version, defaults to current.
:type major: int
:arg minor: minor version, defaults to current.
:type minor: string
:return: the resource path (not necessarily existing).
:rtype: string"""

def script_path_pref(*argv):
	"""returns the user preference or None"""

def script_path_user(*argv):
	"""returns the env var and falls back to home dir or None"""

def script_paths(*argv):
	"""Returns a list of valid script paths.

:arg subdir: Optional subdir.
:type subdir: string
:arg user_pref: Include the user preference script path.
:type user_pref: bool
:arg check_all: Include local, user and system paths rather just the paths
   blender uses.
:type check_all: bool
:return: script paths.
:rtype: list"""

def smpte_from_frame(*argv):
	"""Returns an SMPTE formatted string from the *frame*:
``HH:MM:SS:FF``.

If *fps* and *fps_base* are not given the current scene is used.

:arg frame: frame number.
:type frame: int or float.
:return: the frame string.
:rtype: string"""

def smpte_from_seconds(*argv):
	"""Returns an SMPTE formatted string from the *time*:
``HH:MM:SS:FF``.

If the *fps* is not given the current scene is used.

:arg time: time in seconds.
:type time: int, float or ``datetime.timedelta``.
:return: the frame string.
:rtype: string"""

def time_from_frame(*argv):
	"""Returns the time from a frame number .

If *fps* and *fps_base* are not given the current scene is used.

:arg frame: number.
:type frame: int or float.
:return: the time in seconds.
:rtype: datetime.timedelta"""

def time_to_frame(*argv):
	"""Returns a float frame number from a time given in seconds or
as a datetime.timedelta object.

If *fps* and *fps_base* are not given the current scene is used.

:arg time: time in seconds.
:type time: number or a ``datetime.timedelta`` object
:return: the frame.
:rtype: float"""

import units
def unregister_class(*argv):
	""".. method:: unregister_class(cls)

Unload the python class from blender.

If the class has an *unregister* class method it will be called
before unregistering."""

def unregister_manual_map(*argv):
	pass

def unregister_module(*argv):
	pass

def user_resource(*argv):
	"""Return a user resource path (normally from the users home directory).

:arg type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE'].
:type type: string
:arg subdir: Optional subdirectory.
:type subdir: string
:arg create: Treat the path as a directory and create
   it if its not existing.
:type create: boolean
:return: a path.
:rtype: string"""


