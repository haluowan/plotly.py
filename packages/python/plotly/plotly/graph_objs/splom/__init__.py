import sys

if sys.version_info < (3, 7):
    from ._unselected import Unselected
    from ._stream import Stream
    from ._selected import Selected
    from ._marker import Marker
    from ._hoverlabel import Hoverlabel
    from ._dimension import Dimension
    from ._diagonal import Diagonal
    from . import unselected
    from . import selected
    from . import marker
    from . import hoverlabel
    from . import dimension
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".unselected", ".selected", ".marker", ".hoverlabel", ".dimension"],
        [
            "._unselected.Unselected",
            "._stream.Stream",
            "._selected.Selected",
            "._marker.Marker",
            "._hoverlabel.Hoverlabel",
            "._dimension.Dimension",
            "._diagonal.Diagonal",
        ],
    )
