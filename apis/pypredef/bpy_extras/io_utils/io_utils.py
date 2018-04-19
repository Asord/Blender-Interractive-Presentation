def BoolProperty(*argv):
	'''.. function:: BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

Returns a new boolean property definition.

:arg name: Name used in the user interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
:type subtype: string
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function'''

def EnumProperty(*argv):
	'''.. function:: EnumProperty(items, name="", description="", default=None, options={'ANIMATABLE'}, update=None, get=None, set=None)

Returns a new enumerator property definition.

:arg items: sequence of enum items formatted:
   ``[(identifier, name, description, icon, number), ...]``.

   The first three elements of the tuples are mandatory.

   :identifier: The identifier is used for Python access.
   :name: Name for the interace.
   :description: Used for documentation and tooltips.
   :icon: An icon string identifier or integer icon value
      (e.g. returned by :class:`bpy.types.UILayout.icon`)
   :number: Unique value used as the identifier for this item (stored in file data).
      Use when the identifier may need to change.

   When an item only contains 4 items they define ``(identifier, name, description, number)``.

   For dynamic values a callback can be passed which returns a list in
   the same format as the static list.
   This function must take 2 arguments ``(self, context)``, **context may be None**.

   .. warning::

      There is a known bug with using a callback,
      Python must keep a reference to the strings returned or Blender will misbehave
      or even crash.
:type items: sequence of string tuples or a function
:arg name: Name used in the user interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg default: The default value for this enum, a string from the identifiers used in *items*.
   If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead.
   WARNING: It shall not be specified (or specified to its default *None* value) for dynamic enums
   (i.e. if a callback function is given as *items* parameter).
:type default: string or set
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
:type options: set
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function'''

class ExportHelper:
	def check(*argv):
		pass

	check_existing = tuple
	check_extension = bool
	filepath = tuple
	def invoke(*argv):
		pass

	order = list

class ImportHelper:
	def check(*argv):
		pass

	filepath = tuple
	def invoke(*argv):
		pass

	order = list

def StringProperty(*argv):
	'''.. function:: StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

Returns a new string property definition.

:arg name: Name used in the user interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg default: initializer string.
:type default: string
:arg maxlen: maximum length of the string.
:type maxlen: int
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
:type subtype: string
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function'''

def axis_conversion(*argv):
	'''Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
where the first 2 are a source and the second 2 are the target.'''

def axis_conversion_ensure(*argv):
	'''Function to ensure an operator has valid axis conversion settings, intended
to be used from :class:`bpy.types.Operator.check`.

:arg operator: the operator to access axis attributes from.
:type operator: :class:`bpy.types.Operator`
:arg forward_attr: attribute storing the forward axis
:type forward_attr: string
:arg up_attr: attribute storing the up axis
:type up_attr: string
:return: True if the value was modified.
:rtype: boolean'''

import bpy
def create_derived_objects(*argv):
	pass

def free_derived_objects(*argv):
	pass

def orientation_helper_factory(*argv):
	pass

def path_reference(*argv):
	'''Return a filepath relative to a destination directory, for use with
exporters.

:arg filepath: the file path to return,
   supporting blenders relative '//' prefix.
:type filepath: string
:arg base_src: the directory the *filepath* is relative too
   (normally the blend file).
:type base_src: string
:arg base_dst: the directory the *filepath* will be referenced from
   (normally the export path).
:type base_dst: string
:arg mode: the method used get the path in
   ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
:type mode: string
:arg copy_subdir: the subdirectory of *base_dst* to use when mode='COPY'.
:type copy_subdir: string
:arg copy_set: collect from/to pairs when mode='COPY',
   pass to *path_reference_copy* when exporting is done.
:type copy_set: set
:arg library: The library this path is relative to.
:type library: :class:`bpy.types.Library` or None
:return: the new filepath.
:rtype: string'''

def path_reference_copy(*argv):
	'''Execute copying files of path_reference

:arg copy_set: set of (from, to) pairs to copy.
:type copy_set: set
:arg report: function used for reporting warnings, takes a string argument.
:type report: function'''

path_reference_mode = tuple
def unique_name(*argv):
	'''Helper function for storing unique names which may have special characters
stripped and restricted to a maximum length.

:arg key: unique item this name belongs to, name_dict[key] will be reused
   when available.
   This can be the object, mesh, material, etc instance its self.
:type key: any hashable object associated with the *name*.
:arg name: The name used to create a unique value in *name_dict*.
:type name: string
:arg name_dict: This is used to cache namespace to ensure no collisions
   occur, this should be an empty dict initially and only modified by this
   function.
:type name_dict: dict
:arg clean_func: Function to call on *name* before creating a unique value.
:type clean_func: function
:arg sep: Separator to use when between the name and a number when a
   duplicate name is found.
:type sep: string'''

def unpack_face_list(*argv):
	pass

def unpack_list(*argv):
	pass


