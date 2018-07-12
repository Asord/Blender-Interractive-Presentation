class IDPropertyArray:
	def to_list(*argv):
		""".. method:: to_list()

Return the array as a list."""

	typecode = object()
	"""None"""


class IDPropertyGroup:
	def clear(*argv):
		""".. method:: clear()

Clear all members from this group."""

	def get(*argv):
		""".. method:: get(key, default=None)

Return the value for key, if it exists, else default."""

	def items(*argv):
		""".. method:: items()

Return the items associated with this group."""

	def iteritems(*argv):
		""".. method:: iteritems()

Iterate through the items in the dict; behaves like dictionary method iteritems."""

	def keys(*argv):
		""".. method:: keys()

Return the keys associated with this group as a list of strings."""

	name = object()
	"""None"""

	def pop(*argv):
		""".. method:: pop(key)

Remove an item from the group, returning a Python representation.

:raises KeyError: When the item doesn't exist.

:arg key: Name of item to remove.
:type key: string"""

	def to_dict(*argv):
		""".. method:: to_dict()

Return a purely python version of the group."""

	def update(*argv):
		""".. method:: update(other)

Update key, values.

:arg other: Updates the values in the group with this.
:type other: :class:`IDPropertyGroup` or dict"""

	def values(*argv):
		""".. method:: values()

Return the values associated with this group."""


class IDPropertyGroupIter:
	pass


