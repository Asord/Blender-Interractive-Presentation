"""This module provides access to offscreen rendering functions."""

class GPUOffScreen:
	""".. class:: GPUOffscreen
This object gives access to off screen buffers."""

	def bind(*argv):
		"""bind(save=True)

Bind the offscreen object.

:param save: save OpenGL current states.
:type save: bool"""

	color_texture = object()
	""".. class:: GPUOffscreen
This object gives access to off screen buffers."""

	def draw_view3d(*argv):
		"""draw_view3d(scene, view3d, region, modelview_matrix, projection_matrix)

Draw the 3d viewport in the offscreen object.

:param scene: Scene to draw.
:type scene: :class:`bpy.types.Scene`
:param view3d: 3D View to get the drawing settings from.
:type view3d: :class:`bpy.types.SpaceView3D`
:param region: Region of the 3D View.
:type region: :class:`bpy.types.Region`
:param modelview_matrix: ModelView Matrix.
:type modelview_matrix: :class:`mathutils.Matrix`
:param projection_matrix: Projection Matrix.
:type projection_matrix: :class:`mathutils.Matrix`"""

	def free(*argv):
		"""free()

Free the offscreen object
The framebuffer, texture and render objects will no longer be accessible."""

	height = object()
	""".. class:: GPUOffscreen
This object gives access to off screen buffers."""

	def unbind(*argv):
		"""unbind(restore=True)

Unbind the offscreen object.

:param restore: restore OpenGL previous states.
:type restore: bool"""

	width = object()
	""".. class:: GPUOffscreen
This object gives access to off screen buffers."""


def new(*argv):
	"""new(width, height, samples=0)

Return a GPUOffScreen.

:param width: Horizontal dimension of the buffer.
:type width: int`
:param height: Vertical dimension of the buffer.
:type height: int`
:param samples: OpenGL samples to use for MSAA or zero to disable.
:type samples: int
:return: Newly created off-screen buffer.
:rtype: :class:`gpu.GPUOffscreen`"""


