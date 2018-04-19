'''This module provides access to the math classes:

- :class:`Color`,
- :class:`Euler`,
- :class:`Matrix`,
- :class:`Quaternion`,
- :class:`Vector`,

.. note::

   Classes, methods and attributes that accept vectors also accept other numeric sequences,
   such as tuples, lists.'''

class Color:
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	b = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this color.

:return: A copy of the color.
:rtype: :class:`Color`

.. note:: use this to get a copy of a wrapped color with
   no reference to the original data.'''

	def freeze(*argv):
		'''.. function:: freeze()

Make this object immutable.

After this the object can be hashed, used in dictionaries & sets.

:return: An instance of this object.'''

	g = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	h = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	hsv = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	is_frozen = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	is_wrapped = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	owner = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	r = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	s = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''

	v = getset_descriptor
	'''.. class:: Color(rgb)

This object gives access to Colors in Blender.

:param rgb: (r, g, b) color values
:type rgb: 3d vector'''


class Euler:
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this euler.

:return: A copy of the euler.
:rtype: :class:`Euler`

.. note:: use this to get a copy of a wrapped euler with
   no reference to the original data.'''

	def freeze(*argv):
		'''.. function:: freeze()

Make this object immutable.

After this the object can be hashed, used in dictionaries & sets.

:return: An instance of this object.'''

	is_frozen = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	is_wrapped = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	def make_compatible(*argv):
		'''.. method:: make_compatible(other)

Make this euler compatible with another,
so interpolating between them works as intended.

.. note:: the rotation order is not taken into account for this function.'''

	order = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	owner = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the euler by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotate_axis(*argv):
		'''.. method:: rotate_axis(axis, angle)

Rotates the euler a certain amount and returning a unique euler rotation
(no 720 degree pitches).

:arg axis: single character in ['X, 'Y', 'Z'].
:type axis: string
:arg angle: angle in radians.
:type angle: float'''

	def to_matrix(*argv):
		'''.. method:: to_matrix()

Return a matrix representation of the euler.

:return: A 3x3 roation matrix representation of the euler.
:rtype: :class:`Matrix`'''

	def to_quaternion(*argv):
		'''.. method:: to_quaternion()

Return a quaternion representation of the euler.

:return: Quaternion representation of the euler.
:rtype: :class:`Quaternion`'''

	x = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	y = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	z = getset_descriptor
	'''.. class:: Euler(angles, order='XYZ')

This object gives access to Eulers in Blender.

:param angles: Three angles, in radians.
:type angles: 3d vector
:param order: Optional order of the angles, a permutation of ``XYZ``.
:type order: str'''

	def zero(*argv):
		'''.. method:: zero()

Set all values to zero.'''


class Matrix:
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def Identity(*argv):
		'''.. classmethod:: Identity(size)

Create an identity matrix.

:arg size: The size of the identity matrix to construct [2, 4].
:type size: int
:return: A new identity matrix.
:rtype: :class:`Matrix`'''

	def OrthoProjection(*argv):
		'''.. classmethod:: OrthoProjection(axis, size)

Create a matrix to represent an orthographic projection.

:arg axis: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
   where a single axis is for a 2D matrix.
   Or a vector for an arbitrary axis
:type axis: string or :class:`Vector`
:arg size: The size of the projection matrix to construct [2, 4].
:type size: int
:return: A new projection matrix.
:rtype: :class:`Matrix`'''

	def Rotation(*argv):
		'''.. classmethod:: Rotation(angle, size, axis)

Create a matrix representing a rotation.

:arg angle: The angle of rotation desired, in radians.
:type angle: float
:arg size: The size of the rotation matrix to construct [2, 4].
:type size: int
:arg axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object
   (optional when size is 2).
:type axis: string or :class:`Vector`
:return: A new rotation matrix.
:rtype: :class:`Matrix`'''

	def Scale(*argv):
		'''.. classmethod:: Scale(factor, size, axis)

Create a matrix representing a scaling.

:arg factor: The factor of scaling to apply.
:type factor: float
:arg size: The size of the scale matrix to construct [2, 4].
:type size: int
:arg axis: Direction to influence scale. (optional).
:type axis: :class:`Vector`
:return: A new scale matrix.
:rtype: :class:`Matrix`'''

	def Shear(*argv):
		'''.. classmethod:: Shear(plane, size, factor)

Create a matrix to represent an shear transformation.

:arg plane: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
   where a single axis is for a 2D matrix only.
:type plane: string
:arg size: The size of the shear matrix to construct [2, 4].
:type size: int
:arg factor: The factor of shear to apply. For a 3 or 4 *size* matrix
   pass a pair of floats corresponding with the *plane* axis.
:type factor: float or float pair
:return: A new shear matrix.
:rtype: :class:`Matrix`'''

	def Translation(*argv):
		'''.. classmethod:: Translation(vector)

Create a matrix representing a translation.

:arg vector: The translation vector.
:type vector: :class:`Vector`
:return: An identity matrix with a translation.
:rtype: :class:`Matrix`'''

	def adjugate(*argv):
		'''.. method:: adjugate()

Set the matrix to its adjugate.

.. note:: When the matrix cant be adjugated a :exc:`ValueError` exception is raised.

.. seealso:: <https://en.wikipedia.org/wiki/Adjugate_matrix>'''

	def adjugated(*argv):
		'''.. method:: adjugated()

Return an adjugated copy of the matrix.

:return: the adjugated matrix.
:rtype: :class:`Matrix`

.. note:: When the matrix cant be adjugated a :exc:`ValueError` exception is raised.'''

	col = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def copy(*argv):
		'''.. method:: copy()

Returns a copy of this matrix.

:return: an instance of itself
:rtype: :class:`Matrix`'''

	def decompose(*argv):
		'''.. method:: decompose()

Return the location, rotation and scale components of this matrix.

:return: loc, rot, scale triple.
:rtype: (:class:`Vector`, :class:`Quaternion`, :class:`Vector`)'''

	def determinant(*argv):
		'''.. method:: determinant()

Return the determinant of a matrix.

:return: Return the determinant of a matrix.
:rtype: float

.. seealso:: <https://en.wikipedia.org/wiki/Determinant>'''

	def freeze(*argv):
		'''.. function:: freeze()

Make this object immutable.

After this the object can be hashed, used in dictionaries & sets.

:return: An instance of this object.'''

	def identity(*argv):
		'''.. method:: identity()

Set the matrix to the identity matrix.

.. note:: An object with zero location and rotation, a scale of one,
   will have an identity matrix.

.. seealso:: <https://en.wikipedia.org/wiki/Identity_matrix>'''

	def invert(*argv):
		'''.. method:: invert(fallback=None)

Set the matrix to its inverse.

:arg fallback: Set the matrix to this value when the inverse can't be calculated
   (instead of raising a :exc:`ValueError` exception).
:type fallback: :class:`Matrix`

.. seealso:: <https://en.wikipedia.org/wiki/Inverse_matrix>'''

	def invert_safe(*argv):
		'''.. method:: invert_safe()

Set the matrix to its inverse, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, set to the identity matrix instead.

.. seealso:: <https://en.wikipedia.org/wiki/Inverse_matrix>'''

	def inverted(*argv):
		'''.. method:: inverted(fallback=None)

Return an inverted copy of the matrix.

:arg fallback: return this when the inverse can't be calculated
   (instead of raising a :exc:`ValueError`).
:type fallback: any
:return: the inverted matrix or fallback when given.
:rtype: :class:`Matrix`'''

	def inverted_safe(*argv):
		'''.. method:: inverted_safe()

Return an inverted copy of the matrix, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, return the identity matrix instead.

:return: the inverted matrix.
:rtype: :class:`Matrix`'''

	is_frozen = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	is_negative = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	is_orthogonal = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	is_orthogonal_axis_vectors = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	is_wrapped = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def lerp(*argv):
		'''.. function:: lerp(other, factor)

Returns the interpolation of two matrices.

:arg other: value to interpolate with.
:type other: :class:`Matrix`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated matrix.
:rtype: :class:`Matrix`'''

	median_scale = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def normalize(*argv):
		'''.. method:: normalize()

Normalize each of the matrix columns.'''

	def normalized(*argv):
		'''.. method:: normalized()

Return a column normalized matrix

:return: a column normalized matrix
:rtype: :class:`Matrix`'''

	owner = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def resize_4x4(*argv):
		'''.. method:: resize_4x4()

Resize the matrix to 4x4.'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the matrix by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`

.. note:: If any of the columns are not unit length this may not have desired results.'''

	row = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def to_3x3(*argv):
		'''.. method:: to_3x3()

Return a 3x3 copy of this matrix.

:return: a new matrix.
:rtype: :class:`Matrix`'''

	def to_4x4(*argv):
		'''.. method:: to_4x4()

Return a 4x4 copy of this matrix.

:return: a new matrix.
:rtype: :class:`Matrix`'''

	def to_euler(*argv):
		'''.. method:: to_euler(order, euler_compat)

Return an Euler representation of the rotation matrix
(3x3 or 4x4 matrix only).

:arg order: Optional rotation order argument in
   ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
:type order: string
:arg euler_compat: Optional euler argument the new euler will be made
   compatible with (no axis flipping between them).
   Useful for converting a series of matrices to animation curves.
:type euler_compat: :class:`Euler`
:return: Euler representation of the matrix.
:rtype: :class:`Euler`'''

	def to_quaternion(*argv):
		'''.. method:: to_quaternion()

Return a quaternion representation of the rotation matrix.

:return: Quaternion representation of the rotation matrix.
:rtype: :class:`Quaternion`'''

	def to_scale(*argv):
		'''.. method:: to_scale()

Return the scale part of a 3x3 or 4x4 matrix.

:return: Return the scale of a matrix.
:rtype: :class:`Vector`

.. note:: This method does not return negative a scale on any axis because it is not possible to obtain this data from the matrix alone.'''

	def to_translation(*argv):
		'''.. method:: to_translation()

Return the translation part of a 4 row matrix.

:return: Return the translation of a matrix.
:rtype: :class:`Vector`'''

	translation = getset_descriptor
	'''.. class:: Matrix([rows])

This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

:param rows: Sequence of rows.
   When ommitted, a 4x4 identity matrix is constructed.
:type rows: 2d number sequence'''

	def transpose(*argv):
		'''.. method:: transpose()

Set the matrix to its transpose.

.. seealso:: <https://en.wikipedia.org/wiki/Transpose>'''

	def transposed(*argv):
		'''.. method:: transposed()

Return a new, transposed matrix.

:return: a transposed matrix
:rtype: :class:`Matrix`'''

	def zero(*argv):
		'''.. method:: zero()

Set all the matrix values to zero.

:rtype: :class:`Matrix`'''


class Quaternion:
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	angle = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	axis = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	def conjugate(*argv):
		'''.. function:: conjugate()

Set the quaternion to its conjugate (negate x, y, z).'''

	def conjugated(*argv):
		'''.. function:: conjugated()

Return a new conjugated quaternion.

:return: a new quaternion.
:rtype: :class:`Quaternion`'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this quaternion.

:return: A copy of the quaternion.
:rtype: :class:`Quaternion`

.. note:: use this to get a copy of a wrapped quaternion with
   no reference to the original data.'''

	def cross(*argv):
		'''.. method:: cross(other)

Return the cross product of this quaternion and another.

:arg other: The other quaternion to perform the cross product with.
:type other: :class:`Quaternion`
:return: The cross product.
:rtype: :class:`Quaternion`'''

	def dot(*argv):
		'''.. method:: dot(other)

Return the dot product of this quaternion and another.

:arg other: The other quaternion to perform the dot product with.
:type other: :class:`Quaternion`
:return: The dot product.
:rtype: :class:`Quaternion`'''

	def freeze(*argv):
		'''.. function:: freeze()

Make this object immutable.

After this the object can be hashed, used in dictionaries & sets.

:return: An instance of this object.'''

	def identity(*argv):
		'''.. function:: identity()

Set the quaternion to an identity quaternion.

:rtype: :class:`Quaternion`'''

	def invert(*argv):
		'''.. function:: invert()

Set the quaternion to its inverse.'''

	def inverted(*argv):
		'''.. function:: inverted()

Return a new, inverted quaternion.

:return: the inverted value.
:rtype: :class:`Quaternion`'''

	is_frozen = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	is_wrapped = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	magnitude = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	def negate(*argv):
		'''.. function:: negate()

Set the quaternion to its negative.

:rtype: :class:`Quaternion`'''

	def normalize(*argv):
		'''.. function:: normalize()

Normalize the quaternion.'''

	def normalized(*argv):
		'''.. function:: normalized()

Return a new normalized quaternion.

:return: a normalized copy.
:rtype: :class:`Quaternion`'''

	owner = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	def rotate(*argv):
		'''.. method:: rotate(other)

Rotates the quaternion by another mathutils value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotation_difference(*argv):
		'''.. function:: rotation_difference(other)

Returns a quaternion representing the rotational difference.

:arg other: second quaternion.
:type other: :class:`Quaternion`
:return: the rotational difference between the two quat rotations.
:rtype: :class:`Quaternion`'''

	def slerp(*argv):
		'''.. function:: slerp(other, factor)

Returns the interpolation of two quaternions.

:arg other: value to interpolate with.
:type other: :class:`Quaternion`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated rotation.
:rtype: :class:`Quaternion`'''

	def to_axis_angle(*argv):
		'''.. method:: to_axis_angle()

Return the axis, angle representation of the quaternion.

:return: axis, angle.
:rtype: (:class:`Vector`, float) pair'''

	def to_euler(*argv):
		'''.. method:: to_euler(order, euler_compat)

Return Euler representation of the quaternion.

:arg order: Optional rotation order argument in
   ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
:type order: string
:arg euler_compat: Optional euler argument the new euler will be made
   compatible with (no axis flipping between them).
   Useful for converting a series of matrices to animation curves.
:type euler_compat: :class:`Euler`
:return: Euler representation of the quaternion.
:rtype: :class:`Euler`'''

	def to_exponential_map(*argv):
		'''.. method:: to_exponential_map()

Return the exponential map representation of the quaternion.

This representation consist of the rotation axis multiplied by the rotation angle.   Such a representation is useful for interpolation between multiple orientations.

:return: exponential map.
:rtype: :class:`Vector` of size 3

To convert back to a quaternion, pass it to the :class:`Quaternion` constructor.'''

	def to_matrix(*argv):
		'''.. method:: to_matrix()

Return a matrix representation of the quaternion.

:return: A 3x3 rotation matrix representation of the quaternion.
:rtype: :class:`Matrix`'''

	w = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	x = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	y = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''

	z = getset_descriptor
	'''.. class:: Quaternion([seq, [angle]])

This object gives access to Quaternions in Blender.

:param seq: size 3 or 4
:type seq: :class:`Vector`
:param angle: rotation angle, in radians
:type angle: float

The constructor takes arguments in various forms:

(), *no args*
    Create an identity quaternion
(*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.
(*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    .. seealso:: :meth:`to_exponential_map`
(*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    .. seealso:: :meth:`to_axis_angle`'''


class Vector:
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	def Fill(*argv):
		'''.. classmethod:: Fill(size, fill=0.0)

Create a vector of length size with all values set to fill.

:arg size: The length of the vector to be created.
:type size: int
:arg fill: The value used to fill the vector.
:type fill: float'''

	def Linspace(*argv):
		'''.. classmethod:: Linspace(start, stop, size)

Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

:arg start: The start of the range used to fill the vector.
:type start: int
:arg stop: The end of the range used to fill the vector.
:type stop: int
:arg size: The size of the vector to be created.
:type size: int'''

	def Range(*argv):
		'''.. classmethod:: Range(start=0, stop, step=1)

Create a filled with a range of values.

:arg start: The start of the range used to fill the vector.
:type start: int
:arg stop: The end of the range used to fill the vector.
:type stop: int
:arg step: The step between successive values in the vector.
:type step: int'''

	def Repeat(*argv):
		'''.. classmethod:: Repeat(vector, size)

Create a vector by repeating the values in vector until the required size is reached.

:arg tuple: The vector to draw values from.
:type tuple: :class:`mathutils.Vector`
:arg size: The size of the vector to be created.
:type size: int'''

	def angle(*argv):
		'''.. function:: angle(other, fallback=None)

Return the angle between two vectors.

:arg other: another vector to compare the angle with
:type other: :class:`Vector`
:arg fallback: return this when the angle can't be calculated (zero length vector),
   (instead of raising a :exc:`ValueError`).
:type fallback: any
:return: angle in radians or fallback when given
:rtype: float'''

	def angle_signed(*argv):
		'''.. function:: angle_signed(other, fallback)

Return the signed angle between two 2D vectors (clockwise is positive).

:arg other: another vector to compare the angle with
:type other: :class:`Vector`
:arg fallback: return this when the angle can't be calculated (zero length vector),
   (instead of raising a :exc:`ValueError`).
:type fallback: any
:return: angle in radians or fallback when given
:rtype: float'''

	def copy(*argv):
		'''.. function:: copy()

Returns a copy of this vector.

:return: A copy of the vector.
:rtype: :class:`Vector`

.. note:: use this to get a copy of a wrapped vector with
   no reference to the original data.'''

	def cross(*argv):
		'''.. method:: cross(other)

Return the cross product of this vector and another.

:arg other: The other vector to perform the cross product with.
:type other: :class:`Vector`
:return: The cross product.
:rtype: :class:`Vector` or float when 2D vectors are used

.. note:: both vectors must be 2D or 3D'''

	def dot(*argv):
		'''.. method:: dot(other)

Return the dot product of this vector and another.

:arg other: The other vector to perform the dot product with.
:type other: :class:`Vector`
:return: The dot product.
:rtype: :class:`Vector`'''

	def freeze(*argv):
		'''.. function:: freeze()

Make this object immutable.

After this the object can be hashed, used in dictionaries & sets.

:return: An instance of this object.'''

	is_frozen = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	is_wrapped = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	length = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	length_squared = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	def lerp(*argv):
		'''.. function:: lerp(other, factor)

Returns the interpolation of two vectors.

:arg other: value to interpolate with.
:type other: :class:`Vector`
:arg factor: The interpolation value in [0.0, 1.0].
:type factor: float
:return: The interpolated vector.
:rtype: :class:`Vector`'''

	magnitude = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	def negate(*argv):
		'''.. method:: negate()

Set all values to their negative.'''

	def normalize(*argv):
		'''.. method:: normalize()

Normalize the vector, making the length of the vector always 1.0.

.. warning:: Normalizing a vector where all values are zero has no effect.

.. note:: Normalize works for vectors of all sizes,
   however 4D Vectors w axis is left untouched.'''

	def normalized(*argv):
		'''.. method:: normalized()

Return a new, normalized vector.

:return: a normalized copy of the vector
:rtype: :class:`Vector`'''

	def orthogonal(*argv):
		'''.. method:: orthogonal()

Return a perpendicular vector.

:return: a new vector 90 degrees from this vector.
:rtype: :class:`Vector`

.. note:: the axis is undefined, only use when any orthogonal vector is acceptable.'''

	owner = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	def project(*argv):
		'''.. function:: project(other)

Return the projection of this vector onto the *other*.

:arg other: second vector.
:type other: :class:`Vector`
:return: the parallel projection vector
:rtype: :class:`Vector`'''

	def reflect(*argv):
		'''.. method:: reflect(mirror)

Return the reflection vector from the *mirror* argument.

:arg mirror: This vector could be a normal from the reflecting surface.
:type mirror: :class:`Vector`
:return: The reflected vector matching the size of this vector.
:rtype: :class:`Vector`'''

	def resize(*argv):
		'''.. method:: resize(size=3)

Resize the vector to have size number of elements.'''

	def resize_2d(*argv):
		'''.. method:: resize_2d()

Resize the vector to 2D  (x, y).'''

	def resize_3d(*argv):
		'''.. method:: resize_3d()

Resize the vector to 3D  (x, y, z).'''

	def resize_4d(*argv):
		'''.. method:: resize_4d()

Resize the vector to 4D (x, y, z, w).'''

	def resized(*argv):
		'''.. method:: resized(size=3)

Return a resized copy of the vector with size number of elements.

:return: a new vector
:rtype: :class:`Vector`'''

	def rotate(*argv):
		'''.. function:: rotate(other)

Rotate the vector by a rotation value.

:arg other: rotation component of mathutils value
:type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`'''

	def rotation_difference(*argv):
		'''.. function:: rotation_difference(other)

Returns a quaternion representing the rotational difference between this
vector and another.

:arg other: second vector.
:type other: :class:`Vector`
:return: the rotational difference between the two vectors.
:rtype: :class:`Quaternion`

.. note:: 2D vectors raise an :exc:`AttributeError`.'''

	def slerp(*argv):
		'''.. function:: slerp(other, factor, fallback=None)

Returns the interpolation of two non-zero vectors (spherical coordinates).

:arg other: value to interpolate with.
:type other: :class:`Vector`
:arg factor: The interpolation value typically in [0.0, 1.0].
:type factor: float
:arg fallback: return this when the vector can't be calculated (zero length vector or direct opposites),
   (instead of raising a :exc:`ValueError`).
:type fallback: any
:return: The interpolated vector.
:rtype: :class:`Vector`'''

	def to_2d(*argv):
		'''.. method:: to_2d()

Return a 2d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_3d(*argv):
		'''.. method:: to_3d()

Return a 3d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_4d(*argv):
		'''.. method:: to_4d()

Return a 4d copy of the vector.

:return: a new vector
:rtype: :class:`Vector`'''

	def to_track_quat(*argv):
		'''.. method:: to_track_quat(track, up)

Return a quaternion rotation from the vector and the track and up axis.

:arg track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
:type track: string
:arg up: Up axis in ['X', 'Y', 'Z'].
:type up: string
:return: rotation from the vector and the track and up axis.
:rtype: :class:`Quaternion`'''

	def to_tuple(*argv):
		'''.. method:: to_tuple(precision=-1)

Return this vector as a tuple with.

:arg precision: The number to round the value to in [-1, 21].
:type precision: int
:return: the values of the vector rounded by *precision*
:rtype: tuple'''

	w = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	ww = getset_descriptor
	www = getset_descriptor
	wwww = getset_descriptor
	wwwx = getset_descriptor
	wwwy = getset_descriptor
	wwwz = getset_descriptor
	wwx = getset_descriptor
	wwxw = getset_descriptor
	wwxx = getset_descriptor
	wwxy = getset_descriptor
	wwxz = getset_descriptor
	wwy = getset_descriptor
	wwyw = getset_descriptor
	wwyx = getset_descriptor
	wwyy = getset_descriptor
	wwyz = getset_descriptor
	wwz = getset_descriptor
	wwzw = getset_descriptor
	wwzx = getset_descriptor
	wwzy = getset_descriptor
	wwzz = getset_descriptor
	wx = getset_descriptor
	wxw = getset_descriptor
	wxww = getset_descriptor
	wxwx = getset_descriptor
	wxwy = getset_descriptor
	wxwz = getset_descriptor
	wxx = getset_descriptor
	wxxw = getset_descriptor
	wxxx = getset_descriptor
	wxxy = getset_descriptor
	wxxz = getset_descriptor
	wxy = getset_descriptor
	wxyw = getset_descriptor
	wxyx = getset_descriptor
	wxyy = getset_descriptor
	wxyz = getset_descriptor
	wxz = getset_descriptor
	wxzw = getset_descriptor
	wxzx = getset_descriptor
	wxzy = getset_descriptor
	wxzz = getset_descriptor
	wy = getset_descriptor
	wyw = getset_descriptor
	wyww = getset_descriptor
	wywx = getset_descriptor
	wywy = getset_descriptor
	wywz = getset_descriptor
	wyx = getset_descriptor
	wyxw = getset_descriptor
	wyxx = getset_descriptor
	wyxy = getset_descriptor
	wyxz = getset_descriptor
	wyy = getset_descriptor
	wyyw = getset_descriptor
	wyyx = getset_descriptor
	wyyy = getset_descriptor
	wyyz = getset_descriptor
	wyz = getset_descriptor
	wyzw = getset_descriptor
	wyzx = getset_descriptor
	wyzy = getset_descriptor
	wyzz = getset_descriptor
	wz = getset_descriptor
	wzw = getset_descriptor
	wzww = getset_descriptor
	wzwx = getset_descriptor
	wzwy = getset_descriptor
	wzwz = getset_descriptor
	wzx = getset_descriptor
	wzxw = getset_descriptor
	wzxx = getset_descriptor
	wzxy = getset_descriptor
	wzxz = getset_descriptor
	wzy = getset_descriptor
	wzyw = getset_descriptor
	wzyx = getset_descriptor
	wzyy = getset_descriptor
	wzyz = getset_descriptor
	wzz = getset_descriptor
	wzzw = getset_descriptor
	wzzx = getset_descriptor
	wzzy = getset_descriptor
	wzzz = getset_descriptor
	x = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	xw = getset_descriptor
	xww = getset_descriptor
	xwww = getset_descriptor
	xwwx = getset_descriptor
	xwwy = getset_descriptor
	xwwz = getset_descriptor
	xwx = getset_descriptor
	xwxw = getset_descriptor
	xwxx = getset_descriptor
	xwxy = getset_descriptor
	xwxz = getset_descriptor
	xwy = getset_descriptor
	xwyw = getset_descriptor
	xwyx = getset_descriptor
	xwyy = getset_descriptor
	xwyz = getset_descriptor
	xwz = getset_descriptor
	xwzw = getset_descriptor
	xwzx = getset_descriptor
	xwzy = getset_descriptor
	xwzz = getset_descriptor
	xx = getset_descriptor
	xxw = getset_descriptor
	xxww = getset_descriptor
	xxwx = getset_descriptor
	xxwy = getset_descriptor
	xxwz = getset_descriptor
	xxx = getset_descriptor
	xxxw = getset_descriptor
	xxxx = getset_descriptor
	xxxy = getset_descriptor
	xxxz = getset_descriptor
	xxy = getset_descriptor
	xxyw = getset_descriptor
	xxyx = getset_descriptor
	xxyy = getset_descriptor
	xxyz = getset_descriptor
	xxz = getset_descriptor
	xxzw = getset_descriptor
	xxzx = getset_descriptor
	xxzy = getset_descriptor
	xxzz = getset_descriptor
	xy = getset_descriptor
	xyw = getset_descriptor
	xyww = getset_descriptor
	xywx = getset_descriptor
	xywy = getset_descriptor
	xywz = getset_descriptor
	xyx = getset_descriptor
	xyxw = getset_descriptor
	xyxx = getset_descriptor
	xyxy = getset_descriptor
	xyxz = getset_descriptor
	xyy = getset_descriptor
	xyyw = getset_descriptor
	xyyx = getset_descriptor
	xyyy = getset_descriptor
	xyyz = getset_descriptor
	xyz = getset_descriptor
	xyzw = getset_descriptor
	xyzx = getset_descriptor
	xyzy = getset_descriptor
	xyzz = getset_descriptor
	xz = getset_descriptor
	xzw = getset_descriptor
	xzww = getset_descriptor
	xzwx = getset_descriptor
	xzwy = getset_descriptor
	xzwz = getset_descriptor
	xzx = getset_descriptor
	xzxw = getset_descriptor
	xzxx = getset_descriptor
	xzxy = getset_descriptor
	xzxz = getset_descriptor
	xzy = getset_descriptor
	xzyw = getset_descriptor
	xzyx = getset_descriptor
	xzyy = getset_descriptor
	xzyz = getset_descriptor
	xzz = getset_descriptor
	xzzw = getset_descriptor
	xzzx = getset_descriptor
	xzzy = getset_descriptor
	xzzz = getset_descriptor
	y = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	yw = getset_descriptor
	yww = getset_descriptor
	ywww = getset_descriptor
	ywwx = getset_descriptor
	ywwy = getset_descriptor
	ywwz = getset_descriptor
	ywx = getset_descriptor
	ywxw = getset_descriptor
	ywxx = getset_descriptor
	ywxy = getset_descriptor
	ywxz = getset_descriptor
	ywy = getset_descriptor
	ywyw = getset_descriptor
	ywyx = getset_descriptor
	ywyy = getset_descriptor
	ywyz = getset_descriptor
	ywz = getset_descriptor
	ywzw = getset_descriptor
	ywzx = getset_descriptor
	ywzy = getset_descriptor
	ywzz = getset_descriptor
	yx = getset_descriptor
	yxw = getset_descriptor
	yxww = getset_descriptor
	yxwx = getset_descriptor
	yxwy = getset_descriptor
	yxwz = getset_descriptor
	yxx = getset_descriptor
	yxxw = getset_descriptor
	yxxx = getset_descriptor
	yxxy = getset_descriptor
	yxxz = getset_descriptor
	yxy = getset_descriptor
	yxyw = getset_descriptor
	yxyx = getset_descriptor
	yxyy = getset_descriptor
	yxyz = getset_descriptor
	yxz = getset_descriptor
	yxzw = getset_descriptor
	yxzx = getset_descriptor
	yxzy = getset_descriptor
	yxzz = getset_descriptor
	yy = getset_descriptor
	yyw = getset_descriptor
	yyww = getset_descriptor
	yywx = getset_descriptor
	yywy = getset_descriptor
	yywz = getset_descriptor
	yyx = getset_descriptor
	yyxw = getset_descriptor
	yyxx = getset_descriptor
	yyxy = getset_descriptor
	yyxz = getset_descriptor
	yyy = getset_descriptor
	yyyw = getset_descriptor
	yyyx = getset_descriptor
	yyyy = getset_descriptor
	yyyz = getset_descriptor
	yyz = getset_descriptor
	yyzw = getset_descriptor
	yyzx = getset_descriptor
	yyzy = getset_descriptor
	yyzz = getset_descriptor
	yz = getset_descriptor
	yzw = getset_descriptor
	yzww = getset_descriptor
	yzwx = getset_descriptor
	yzwy = getset_descriptor
	yzwz = getset_descriptor
	yzx = getset_descriptor
	yzxw = getset_descriptor
	yzxx = getset_descriptor
	yzxy = getset_descriptor
	yzxz = getset_descriptor
	yzy = getset_descriptor
	yzyw = getset_descriptor
	yzyx = getset_descriptor
	yzyy = getset_descriptor
	yzyz = getset_descriptor
	yzz = getset_descriptor
	yzzw = getset_descriptor
	yzzx = getset_descriptor
	yzzy = getset_descriptor
	yzzz = getset_descriptor
	z = getset_descriptor
	'''.. class:: Vector(seq)

This object gives access to Vectors in Blender.

:param seq: Components of the vector, must be a sequence of at least two
:type seq: sequence of numbers'''

	def zero(*argv):
		'''.. method:: zero()

Set all values to zero.'''

	zw = getset_descriptor
	zww = getset_descriptor
	zwww = getset_descriptor
	zwwx = getset_descriptor
	zwwy = getset_descriptor
	zwwz = getset_descriptor
	zwx = getset_descriptor
	zwxw = getset_descriptor
	zwxx = getset_descriptor
	zwxy = getset_descriptor
	zwxz = getset_descriptor
	zwy = getset_descriptor
	zwyw = getset_descriptor
	zwyx = getset_descriptor
	zwyy = getset_descriptor
	zwyz = getset_descriptor
	zwz = getset_descriptor
	zwzw = getset_descriptor
	zwzx = getset_descriptor
	zwzy = getset_descriptor
	zwzz = getset_descriptor
	zx = getset_descriptor
	zxw = getset_descriptor
	zxww = getset_descriptor
	zxwx = getset_descriptor
	zxwy = getset_descriptor
	zxwz = getset_descriptor
	zxx = getset_descriptor
	zxxw = getset_descriptor
	zxxx = getset_descriptor
	zxxy = getset_descriptor
	zxxz = getset_descriptor
	zxy = getset_descriptor
	zxyw = getset_descriptor
	zxyx = getset_descriptor
	zxyy = getset_descriptor
	zxyz = getset_descriptor
	zxz = getset_descriptor
	zxzw = getset_descriptor
	zxzx = getset_descriptor
	zxzy = getset_descriptor
	zxzz = getset_descriptor
	zy = getset_descriptor
	zyw = getset_descriptor
	zyww = getset_descriptor
	zywx = getset_descriptor
	zywy = getset_descriptor
	zywz = getset_descriptor
	zyx = getset_descriptor
	zyxw = getset_descriptor
	zyxx = getset_descriptor
	zyxy = getset_descriptor
	zyxz = getset_descriptor
	zyy = getset_descriptor
	zyyw = getset_descriptor
	zyyx = getset_descriptor
	zyyy = getset_descriptor
	zyyz = getset_descriptor
	zyz = getset_descriptor
	zyzw = getset_descriptor
	zyzx = getset_descriptor
	zyzy = getset_descriptor
	zyzz = getset_descriptor
	zz = getset_descriptor
	zzw = getset_descriptor
	zzww = getset_descriptor
	zzwx = getset_descriptor
	zzwy = getset_descriptor
	zzwz = getset_descriptor
	zzx = getset_descriptor
	zzxw = getset_descriptor
	zzxx = getset_descriptor
	zzxy = getset_descriptor
	zzxz = getset_descriptor
	zzy = getset_descriptor
	zzyw = getset_descriptor
	zzyx = getset_descriptor
	zzyy = getset_descriptor
	zzyz = getset_descriptor
	zzz = getset_descriptor
	zzzw = getset_descriptor
	zzzx = getset_descriptor
	zzzy = getset_descriptor
	zzzz = getset_descriptor

import bvhtree
import geometry
import interpolate
import kdtree
import noise

