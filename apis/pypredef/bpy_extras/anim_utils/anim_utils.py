def bake_action(*argv):
	'''Return an image from the file path with options to search multiple paths
and return a placeholder if its not found.

:arg frame_start: First frame to bake.
:type frame_start: int
:arg frame_end: Last frame to bake.
:type frame_end: int
:arg frame_step: Frame step.
:type frame_step: int
:arg only_selected: Only bake selected bones.
:type only_selected: bool
:arg do_pose: Bake pose channels.
:type do_pose: bool
:arg do_object: Bake objects.
:type do_object: bool
:arg do_visual_keying: Use the final transformations for baking ('visual keying')
:type do_visual_keying: bool
:arg do_constraint_clear: Remove constraints after baking.
:type do_constraint_clear: bool
:arg do_parents_clear: Unparent after baking objects.
:type do_parents_clear: bool
:arg do_clean: Remove redundant keyframes after baking.
:type do_clean: bool
:arg action: An action to bake the data into, or None for a new action
   to be created.
:type action: :class:`bpy.types.Action` or None

:return: an action or None
:rtype: :class:`bpy.types.Action`'''

import bpy

