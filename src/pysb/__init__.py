from __future__ import annotations

__all__ = ["__version__", "hello_main"]
__version__ = "0.1.0"


def hello_main() -> None:
    from .hello import main

    main()
