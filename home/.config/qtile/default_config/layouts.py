from libqtile import layout
from libqtile.config import Match


class Layouts(object):
    def setup_layouts(self):
        layouts = [
            layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),  # type: ignore
            layout.Max(),  # type: ignore
            # Try more layouts by unleashing below layouts.
            # layout.Stack(num_stacks=2),
            # layout.Bsp(),
            # layout.Matrix(),
            # layout.MonadTall(),
            # layout.MonadWide(),
            # layout.RatioTile(),
            # layout.Tile(),
            # layout.TreeTab(),
            # layout.VerticalTile(),
            # layout.Zoomy(),
        ]

        return layouts


class FloatingLayouts(object):
    def setup_floating_layouts(self):
        floating_layout = layout.Floating(  # type: ignore
            float_rules=[
                # Run the utility of `xprop` to see the wm class and name of an X client.
                *layout.Floating.default_float_rules,  # type: ignore
                Match(wm_class="confirmreset"),  # gitk
                Match(wm_class="makebranch"),  # gitk
                Match(wm_class="maketag"),  # gitk
                Match(wm_class="ssh-askpass"),  # ssh-askpass
                Match(title="branchdialog"),  # gitk
                Match(title="pinentry"),  # GPG key password entry
            ]
        )

        return floating_layout
