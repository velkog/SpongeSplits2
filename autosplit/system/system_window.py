from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from system.linux.window import Window

    SystemWindow = Window
else:
    from system.win.window import Window

    SystemWindow = Window
