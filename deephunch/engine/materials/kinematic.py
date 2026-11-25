from typing import TYPE_CHECKING, ClassVar

from deephunch.constants import STRUCTURE

from .base import Material

if TYPE_CHECKING:
    from deephunch.engine.entities.base_entity import Entity


class Kinematic[EntityT: "Entity"](Material[EntityT]):
    """
    Visualization-only material for ghost/reference entities.

    Kinematic entities are rendered but do not participate in physics simulation, collision detection, or constraint
    solving.

    Parameters
    ----------
    use_visual_raycasting : bool | None, optional
        Deprecated: use ``use_visual_raycasting`` of the entity spec (see ``gs.entities.Kinematic``).
    """

    structure: ClassVar[STRUCTURE] = STRUCTURE.RIGID
