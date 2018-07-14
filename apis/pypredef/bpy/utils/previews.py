'''This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


Custom Icon Example
-------------------

.. literalinclude:: __/__/__/release/scripts/templates_py/ui_previews_custom_icon.py'''

class ImagePreviewCollection:
	'''Dictionary-like class of previews.

This is a subclass of Python's built-in dict type,
used to store multiple image previews.

.. note::

    - instance with :mod:`bpy.utils.previews.new`
    - keys must be ``str`` type.
    - values will be :class:`bpy.types.ImagePreview`'''

	def clear(*argv):
		'''Clear all previews.'''

	def close(*argv):
		'''Close the collection and clear all previews.'''

	def copy(*argv):
		'''D.copy() -> a shallow copy of D'''

	def fromkeys(*argv):
		'''Returns a new dict with keys from iterable and values equal to value.'''

	def get(*argv):
		'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'''

	def items(*argv):
		'''D.items() -> a set-like object providing a view on D's items'''

	def keys(*argv):
		'''D.keys() -> a set-like object providing a view on D's keys'''

	def load(*argv):
		'''.. method:: load(name, filepath, filetype, force_reload=False)

Generate a new preview from given file path, or return existing one matching ``name``.

:arg name: The name (unique id) identifying the preview.
:type name: string
:arg filepath: The file path to generate the preview from.
:type filepath: string
:arg filetype: The type of file, needed to generate the preview in ['IMAGE', 'MOVIE', 'BLEND', 'FONT'].
:type filetype: string
:arg force_reload: If True, force running thumbnail manager even if preview already exists in cache.
:type force_reload: bool
:return: The Preview matching given name, or a new empty one.
:rtype: :class:`bpy.types.ImagePreview`'''

	def new(*argv):
		'''.. method:: new(name)

Generate a new empty preview, or return existing one matching ``name``.

:arg name: The name (unique id) identifying the preview.
:type name: string
:return: The Preview matching given name, or a new empty one.
:rtype: :class:`bpy.types.ImagePreview`'''

	def pop(*argv):
		'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised'''

	def popitem(*argv):
		'''D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.'''

	def setdefault(*argv):
		'''D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D'''

	def update(*argv):
		'''D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]'''

	def values(*argv):
		'''D.values() -> an object providing a view on D's values'''


def new(*argv):
	''':return: a new preview collection.
:rtype: :class:`ImagePreviewCollection`'''

def remove(*argv):
	'''Remove the specified previews collection.

:arg pcoll: Preview collection to close.
:type pcoll: :class:`ImagePreviewCollection`'''


