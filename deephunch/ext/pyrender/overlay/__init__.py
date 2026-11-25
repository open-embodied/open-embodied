"""ImGui overlay package. Re-exports :class:`ImGuiOverlayPlugin` so callers can keep importing
``from deephunch.ext.pyrender.overlay import ImGuiOverlayPlugin``."""

from deephunch.ext.pyrender.overlay.plugin import ImGuiOverlayPlugin

__all__ = ["ImGuiOverlayPlugin"]
