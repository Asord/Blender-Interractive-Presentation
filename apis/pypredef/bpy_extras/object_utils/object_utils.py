class AddObjectHelper:
	layers = tuple
	location = tuple
	def poll(*argv):
		pass

	rotation = tuple
	view_align = tuple
	def view_align_update_callback(*argv):
		pass


def BoolProperty(*argv):
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

def BoolVectorProperty(*argv):
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

def FloatVectorProperty(*argv):
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

def add_object_align_init(*argv):
	"""Return a matrix using the operator settings and view context.

:arg context: The context to use.
:type context: :class:`bpy.types.Context`
:arg operator: The operator, checked for location and rotation properties.
:type operator: :class:`bpy.types.Operator`
:return: the matrix from the context and settings.
:rtype: :class:`mathutils.Matrix`"""

import bpy
def object_add_grid_scale(*argv):
	"""Return scale which should be applied on object
data to align it to grid scale"""

def object_add_grid_scale_apply_operator(*argv):
	"""Scale an operators distance values by the grid size."""

def object_data_add(*argv):
	"""Add an object using the view context and preference to to initialize the
location, rotation and layer.

:arg context: The context to use.
:type context: :class:`bpy.types.Context`
:arg obdata: the data used for the new object.
:type obdata: valid object data type or None.
:arg operator: The operator, checked for location and rotation properties.
:type operator: :class:`bpy.types.Operator`
:arg name: Optional name
:type name: string
:return: the newly created object in the scene.
:rtype: :class:`bpy.types.ObjectBase`"""

def object_image_guess(*argv):
	"""Return a single image used by the object,
first checking the texture-faces, then the material."""

def world_to_camera_view(*argv):
	"""Returns the camera space coords for a 3d point.
(also known as: normalized device coordinates - NDC).

Where (0, 0) is the bottom left and (1, 1)
is the top right of the camera frame.
values outside 0-1 are also supported.
A negative 'z' value means the point is behind the camera.

Takes shift-x/y, lens angle and sensor size into account
as well as perspective/ortho projections.

:arg scene: Scene to use for frame size.
:type scene: :class:`bpy.types.Scene`
:arg obj: Camera object.
:type obj: :class:`bpy.types.Object`
:arg coord: World space location.
:type coord: :class:`mathutils.Vector`
:return: a vector where X and Y map to the view plane and
   Z is the depth on the view axis.
:rtype: :class:`mathutils.Vector`"""


