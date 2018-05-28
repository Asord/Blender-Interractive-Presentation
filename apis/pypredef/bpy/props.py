"""This module defines properties to extend Blender's internal data. The result of these functions is used to assign properties to classes registered with Blender and can't be used directly.

.. note:: All parameters to these functions must be passed as keywords."""

def BoolProperty(*argv, **kwargs):
	""".. function:: BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

Returns a new boolean property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
:type subtype: string
:arg update: Function to be called	 when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function"""

def BoolVectorProperty(*argv, **kwargs):
	""".. function:: BoolVectorProperty(name="", description="", default=(False, False, False), options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None)

Returns a new vector boolean property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg default: sequence of booleans the length of *size*.
:type default: sequence
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
:type subtype: string
:arg size: Vector dimensions in [1, 32].
:type size: int
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function"""

def CollectionProperty(*argv, **kwargs):
	""".. function:: CollectionProperty(type=None, name="", description="", options={'ANIMATABLE'})

Returns a new collection property definition.

:arg type: A subclass of :class:`bpy.types.PropertyGroup`.
:type type: class
:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set"""

def EnumProperty(*argv, **kwargs):
	""".. function:: EnumProperty(items, name="", description="", default=None, options={'ANIMATABLE'}, update=None, get=None, set=None)

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
:arg name: Name used in the user Interface.
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
:type set: function"""

def FloatProperty(*argv, **kwargs):
	""".. function:: FloatProperty(name="", description="", default=0.0, min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', update=None, get=None, set=None)

Returns a new float property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
:type min: float
:arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
:type max: float
:arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
:type soft_min: float
:arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
:type soft_max: float
:arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
:type step: int
:arg precision: Maximum number of decimal digits to display, in [0, 6].
:type precision: int
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
:type subtype: string
:arg unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
:type unit: string
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function"""

def FloatVectorProperty(*argv, **kwargs):
	""".. function:: FloatVectorProperty(name="", description="", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None)

Returns a new vector float property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg default: sequence of floats the length of *size*.
:type default: sequence
:arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
:type min: float
:arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
:type max: float
:arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
:type soft_min: float
:arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
:type soft_max: float
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
:type step: int
:arg precision: Maximum number of decimal digits to display, in [0, 6].
:type precision: int
:arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
:type subtype: string
:arg unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
:type unit: string
:arg size: Vector dimensions in [1, 32].
:type size: int
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function"""

def IntProperty(*argv, **kwargs):
	""".. function:: IntProperty(name="", description="", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

Returns a new int property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
:type min: int
:arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
:type max: int
:arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
:type soft_min: int
:arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
:type soft_max: int
:arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
:type step: int
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
:type set: function"""

def IntVectorProperty(*argv, **kwargs):
	""".. function:: IntVectorProperty(name="", description="", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None)

Returns a new vector int property definition.

:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg default: sequence of ints the length of *size*.
:type default: sequence
:arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
:type min: int
:arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
:type max: int
:arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
:type soft_min: int
:arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
:type soft_max: int
:arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
:type step: int
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
:type subtype: string
:arg size: Vector dimensions in [1, 32].
:type size: int
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function
:arg get: Function to be called when this value is 'read',
   This function must take 1 value (self) and return the value of the property.
:type get: function
:arg set: Function to be called when this value is 'written',
   This function must take 2 values (self, value) and return None.
:type set: function"""

def PointerProperty(*argv, **kwargs):
	""".. function:: PointerProperty(type=None, name="", description="", options={'ANIMATABLE'}, update=None)

Returns a new pointer property definition.

:arg type: A subclass of :class:`bpy.types.PropertyGroup`.
:type type: class
:arg name: Name used in the user Interface.
:type name: string
:arg description: Text used for the tooltip and api documentation.
:type description: string
:arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
:type options: set
:arg update: Function to be called when this value is modified,
   This function must take 2 values (self, context) and return None.
   *Warning* there are no safety checks to avoid infinite recursion.
:type update: function"""

def RemoveProperty(*argv, **kwargs):
	""".. function:: RemoveProperty(cls, attr=)

   Removes a dynamically defined property.

   :arg cls: The class containing the property (must be a positional argument).
   :type cls: type
   :arg attr: Property name (must be passed as a keyword).
   :type attr: string

.. note:: Typically this function doesn't need to be accessed directly.
   Instead use ``del cls.attr``"""

def StringProperty(*argv, **kwargs):
	""".. function:: StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

Returns a new string property definition.

:arg name: Name used in the user Interface.
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
:type set: function"""


