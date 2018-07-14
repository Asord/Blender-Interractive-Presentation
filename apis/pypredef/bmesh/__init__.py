"""BMesh mesh manipulations (bmesh)
   This module provides access to blenders bmesh data structures.
   .. include:: include__bmesh.rst
   
"""
from .types import *

def from_edit_mesh(mesh):
   """Return a BMesh from this mesh, currently the mesh must already be in editmode.
      
      Arguments:
      @mesh (bpy.types.Mesh): The editmode mesh.

      @returns (types.BMesh): the BMesh associated with this mesh.
   """

   return types.BMesh

def new():
   """
      @returns (types.BMesh): Return a new, empty BMesh.
   """

   return types.BMesh

def update_edit_mesh(mesh, tessface=True, destructive=True):
   """Update the mesh after changes to the BMesh in editmode, 
      optionally recalculating n-gon tessellation.
      
      Arguments:
      @mesh (bpy.types.Mesh): The editmode mesh.
      @tessface (boolean): Option to recalculate n-gon tessellation.
      @destructive (boolean): Use when geometry has been added or removed.

   """

   pass

