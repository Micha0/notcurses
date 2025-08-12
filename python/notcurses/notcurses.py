# SPDX-License-Identifier: Apache-2.0

# Copyright 2020, 2021 igo95862

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

from typing import Optional, Tuple
import importlib

_c = importlib.import_module("notcurses.notcurses")

# Stub file for typing and docs

# region misc


def notcurses_version() -> str:
    """Get human readable string of running Notcurses version."""
    return _c.notcurses_version()


def notcurses_version_components() -> Tuple[int, int, int, int]:
    """Get a tuple of major, minor, patch, tweak integer
    of the running Notcurses version"""
    return _c.notcurses_version_components()


def ncstrwidth(text: str, /) -> int:
    """Returns the number of columns occupied by a string,
    or -1 if a non-printable/illegal character is encountered."""
    return _c.ncstrwidth(text)


# endregion misc

# region ncchannel


def ncchannels_rgb_initializer(
        fr: int, fg: int, fb: int,
        br: int, bg: int, bb: int,
        /) -> int:
    """Initialize a 64-bit ncchannel pair with specified RGB fg/bg."""
    return _c.ncchannels_rgb_initializer(fr, fg, fb, br, bg, bb)


def ncchannel_rgb_initializer(
        r: int, g: int, b: int,
        /) -> int:
    """Initialize a 32-bit single ncchannel with specified RGB."""
    return _c.ncchannel_rgb_initializer(r, g, b)


def ncchannel_r(channel: int, /) -> int:
    """Extract the 8-bit red component from a 32-bit ncchannel."""
    return _c.ncchannel_r(channel)


def ncchannel_g(channel: int, /) -> int:
    """Extract the 8-bit green component from a 32-bit ncchannel."""
    return _c.ncchannel_g(channel)


def ncchannel_b(channel: int, /) -> int:
    """Extract the 8-bit blue component from a 32-bit ncchannel."""
    return _c.ncchannel_b(channel)


def ncchannel_rgb8(channel: int, /) -> Tuple[int, int, int]:
    """Extract the three 8-bit R/G/B components from a 32-bit ncchannel."""
    return _c.ncchannel_rgb8(channel)


def ncchannel_set_rgb8(channel: int, r: int, g: int, b: int, /) -> int:
    """Set the three 8-bit components of a 32-bit ncchannel.

    Mark it as not using the default color.
    Retain the other bits unchanged.
    """
    return _c.ncchannel_set_rgb8(channel, r, g, b)


def ncchannel_set_rgb8_clipped(channel: int, r: int, g: int, b: int, /) -> int:
    """Set the three 8-bit components of a 32-bit ncchannel.

    Mark it as not using the default color.
    Retain the other bits unchanged. r, g, and b will be clipped to
    the range [0..255].
    """
    return _c.ncchannel_set_rgb8_clipped(channel, r, g, b)


def ncchannel_set(channel: int, rdb: int, /) -> int:
    """Set the three 8-bit components of a 32-bit ncchannel
    from a provide an assembled, packed 24 bits of rgb.
    """
    return _c.ncchannel_set(channel, rdb)


def ncchannel_alpha(channel: int, /) -> int:
    """Extract 2 bits of foreground alpha from channel"""
    return _c.ncchannel_alpha(channel)


def ncchannel_palindex(channel: int, /) -> int:
    """Extract 2 bits of palindex from channel"""
    return _c.ncchannel_palindex(channel)


def ncchannel_set_alpha(channel: int, alpha: int, /) -> int:
    """Set the 2-bit alpha component of the 32-bit channel."""
    return _c.ncchannel_set_alpha(channel, alpha)


def ncchannel_set_palindex(channel: int, palindex: int, /) ->int:
    """Set the 2-bit palindex of the 32-bit channel."""
    return _c.ncchannel_set_palindex(channel, palindex)


def ncchannel_default_p(channel: int, /) -> bool:
    """Is this ncchannel using the \"default color\" rather
    than RGB/palette-indexed?
    """
    return _c.ncchannel_default_p(channel)


def ncchannel_palindex_p(channel: int, /) -> bool:
    """Is this ncchannel using palette-indexed color rather than RGB?"""
    return _c.ncchannel_palindex_p(channel)


def ncchannel_set_default(channel: int, /) ->int:
    """Mark the ncchannel as using its default color, which also
    marks it opaque."""
    return _c.ncchannel_set_default(channel)


def ncchannels_bchannel(channel: int, /) -> int:
    """Extract the 32-bit background ncchannel from a channel pair."""
    return _c.ncchannels_bchannel(channel)


def ncchannels_fchannel(channel: int, /) -> int:
    """Extract the 32-bit foreground ncchannel from a channel pair."""
    return _c.ncchannels_fchannel(channel)


def ncchannels_set_bchannel(channels: int, channel: int, /) -> int:
    """Set the 32-bit background ncchannel of a channels pair."""
    return _c.ncchannels_set_bchannel(channels, channel)


def ncchannels_set_fchannel(channels: int, channel: int, /) -> int:
    """Set the 32-bit foreground ncchannel of a channels pair."""
    return _c.ncchannels_set_fchannel(channels, channel)


def ncchannels_combine(fchan: int, bchan: int, /) ->int:
    """Combine foreground and background channels in to channels pair."""
    return _c.ncchannels_combine(fchan, bchan)


def ncchannels_fg_palindex(channels: int, /) -> int:
    """Extract the 2-bit palindex from foreground channel of channels pair."""
    return _c.ncchannels_fg_palindex(channels)


def ncchannels_bg_palindex(channels: int, /) -> int:
    """Extract the 2-bit palindex from background channel of channels pair."""
    return _c.ncchannels_bg_palindex(channels)


def ncchannels_fg_rgb(channels: int, /) -> int:
    """Extract 24 bits of foreground RGB from channels pair."""
    return _c.ncchannels_fg_rgb(channels)


def ncchannels_bg_rgb(channels: int, /) -> int:
    """Extract 24 bits of background RGB from channels pair."""
    return _c.ncchannels_bg_rgb(channels)


def ncchannels_fg_alpha(channels: int, /) -> int:
    """Extract the 2-bit alpha from foreground channel of channels pair."""
    return _c.ncchannels_fg_alpha(channels)


def ncchannels_bg_alpha(channels: int, /) -> int:
    """Extract the 2-bit alpha from background channel of channels pair."""
    return _c.ncchannels_bg_alpha(channels)


def ncchannels_fg_rgb8(channels: int, /) -> Tuple[int, int, int]:
    """Extract 24 bits of foreground RGB from channels pair, split into
    subncchannels."""
    return _c.ncchannels_fg_rgb8(channels)


def ncchannels_bg_rgb8(channels: int, /) -> Tuple[int, int, int]:
    """Extract 24 bits of background RGB from channels pair, split into
    subncchannels."""
    return _c.ncchannels_bg_rgb8(channels)


def ncchannels_set_fg_rgb8(channels: int, r: int, g: int, b: int, /) -> int:
    """Set the red, green and blue of foreground channel of channels pair."""
    return _c.ncchannels_set_fg_rgb8(channels, r, g, b)


def ncchannels_set_fg_rgb8_clipped(channels: int, r: int, g: int, b: int,
                                   /) -> int:
    """Set the red, green and blue of foreground channel of channels pair.

    Clipped to 0..255
    """
    return _c.ncchannels_set_fg_rgb8_clipped(channels, r, g, b)


def ncchannels_set_fg_alpha(channels: int, alpha: int, /) -> int:
    """Set the 2-bit alpha of the foreground channel of channels pair."""
    return _c.ncchannels_set_fg_alpha(channels, alpha)


def ncchannels_set_fg_palindex(channels: int, alpha: int, /) -> int:
    """Set the 2-bit paliindex of the foreground channel of channels pair."""
    return _c.ncchannels_set_fg_palindex(channels, alpha)


def ncchannels_set_fg_rgb(channels: int, rgb: int, /) -> int:
    """Set the RGB assembled 24 bit channel of the foreground channel of
    channels pair."""
    return _c.ncchannels_set_fg_rgb(channels, rgb)


def ncchannels_set_bg_rgb8(channels: int, r: int, g: int, b: int, /) -> int:
    """Set the red, green and blue of background channel of channels pair."""
    return _c.ncchannels_set_bg_rgb8(channels, r, g, b)


def ncchannels_set_bg_rgb8_clipped(channels: int, r: int, g: int, b: int,
                                   /) -> int:
    """Set the red, green and blue of background channel of channels pair.

    Clipped to 0..255
    """
    return _c.ncchannels_set_bg_rgb8_clipped(channels, r, g, b)


def ncchannels_set_bg_alpha(channels: int, alpha: int, /) -> int:
    """Set the 2-bit alpha of the background channel of channels pair."""
    return _c.ncchannels_set_bg_alpha(channels, alpha)


def ncchannels_set_bg_palindex(channels: int, alpha: int, /) -> int:
    """Set the 2-bit paliindex of the background channel of channels pair."""
    return _c.ncchannels_set_bg_palindex(channels, alpha)


def ncchannels_set_bg_rgb(channels: int, rgb: int, /) -> int:
    """Set the RGB assembled 24 bit channel of the background channel of
    channels pair."""
    return _c.ncchannels_set_bg_rgb(channels, rgb)


def ncchannels_fg_default_p(channels: int, /) ->bool:
    """Is the foreground using the default color?"""
    return _c.ncchannels_fg_default_p(channels)


def ncchannels_fg_palindex_p(channels: int, /) ->bool:
    """Is the foreground using indexed palette color?"""
    return _c.ncchannels_fg_palindex_p(channels)


def ncchannels_bg_default_p(channels: int, /) ->bool:
    """Is the foreground using the default color?"""
    return _c.ncchannels_bg_default_p(channels)


def ncchannels_bg_palindex_p(channels: int, /) ->bool:
    """Is the foreground using indexed palette color?"""
    return _c.ncchannels_bg_palindex_p(channels)


def ncchannels_set_fg_default(channels: int, /) -> int:
    """Mark the foreground ncchannel as using its default color."""
    return _c.ncchannels_set_fg_default(channels)


def ncchannels_set_bg_default(channels: int, /) -> int:
    """Mark the background ncchannel as using its default color."""
    return _c.ncchannels_set_bg_default(channels)

# endregion ncchannel


# region nckey
NCKEY_INVALID: int
NCKEY_RESIZE: int
NCKEY_UP: int
NCKEY_RIGHT: int
NCKEY_DOWN: int
NCKEY_LEFT: int
NCKEY_INS: int
NCKEY_DEL: int
NCKEY_BACKSPACE: int
NCKEY_PGDOWN: int
NCKEY_PGUP: int
NCKEY_HOME: int
NCKEY_END: int
NCKEY_F00: int
NCKEY_F01: int
NCKEY_F02: int
NCKEY_F03: int
NCKEY_F04: int
NCKEY_F05: int
NCKEY_F06: int
NCKEY_F07: int
NCKEY_F08: int
NCKEY_F09: int
NCKEY_F10: int
NCKEY_F11: int
NCKEY_F12: int
NCKEY_F13: int
NCKEY_F14: int
NCKEY_F15: int
NCKEY_F16: int
NCKEY_F17: int
NCKEY_F18: int
NCKEY_F19: int
NCKEY_F20: int
NCKEY_F21: int
NCKEY_F22: int
NCKEY_F23: int
NCKEY_F24: int
NCKEY_F25: int
NCKEY_F26: int
NCKEY_F27: int
NCKEY_F28: int
NCKEY_F29: int
NCKEY_F30: int
NCKEY_F31: int
NCKEY_F32: int
NCKEY_F33: int
NCKEY_F34: int
NCKEY_F35: int
NCKEY_F36: int
NCKEY_F37: int
NCKEY_F38: int
NCKEY_F39: int
NCKEY_F40: int
NCKEY_F41: int
NCKEY_F42: int
NCKEY_F43: int
NCKEY_F44: int
NCKEY_F45: int
NCKEY_F46: int
NCKEY_F47: int
NCKEY_F48: int
NCKEY_F49: int
NCKEY_F50: int
NCKEY_F51: int
NCKEY_F52: int
NCKEY_F53: int
NCKEY_F54: int
NCKEY_F55: int
NCKEY_F56: int
NCKEY_F57: int
NCKEY_F58: int
NCKEY_F59: int
NCKEY_F60: int
NCKEY_ENTER: int
NCKEY_CLS: int
NCKEY_DLEFT: int
NCKEY_DRIGHT: int
NCKEY_ULEFT: int
NCKEY_URIGHT: int
NCKEY_CENTER: int
NCKEY_BEGIN: int
NCKEY_CANCEL: int
NCKEY_CLOSE: int
NCKEY_COMMAND: int
NCKEY_COPY: int
NCKEY_EXIT: int
NCKEY_PRINT: int
NCKEY_REFRESH: int
NCKEY_SEPARATOR: int
NCKEY_CAPS_LOCK: int
NCKEY_SCROLL_LOCK: int
NCKEY_NUM_LOCK: int
NCKEY_PRINT_SCREEN: int
NCKEY_PAUSE: int
NCKEY_MENU: int
NCKEY_MEDIA_PLAY: int
NCKEY_MEDIA_PAUSE: int
NCKEY_MEDIA_PPAUSE: int
NCKEY_MEDIA_REV: int
NCKEY_MEDIA_STOP: int
NCKEY_MEDIA_FF: int
NCKEY_MEDIA_REWIND: int
NCKEY_MEDIA_NEXT: int
NCKEY_MEDIA_PREV: int
NCKEY_MEDIA_RECORD: int
NCKEY_MEDIA_LVOL: int
NCKEY_MEDIA_RVOL: int
NCKEY_MEDIA_MUTE: int
NCKEY_LSHIFT: int
NCKEY_LCTRL: int
NCKEY_LALT: int
NCKEY_LSUPER: int
NCKEY_LHYPER: int
NCKEY_LMETA: int
NCKEY_RSHIFT: int
NCKEY_RCTRL: int
NCKEY_RALT: int
NCKEY_RSUPER: int
NCKEY_RHYPER: int
NCKEY_RMETA: int
NCKEY_L3SHIFT: int
NCKEY_L5SHIFT: int
NCKEY_MOTION: int
NCKEY_BUTTON1: int
NCKEY_BUTTON2: int
NCKEY_BUTTON3: int
NCKEY_BUTTON4: int
NCKEY_BUTTON5: int
NCKEY_BUTTON6: int
NCKEY_BUTTON7: int
NCKEY_BUTTON8: int
NCKEY_BUTTON9: int
NCKEY_BUTTON10: int
NCKEY_BUTTON11: int
NCKEY_SIGNAL: int
NCKEY_EOF: int
NCKEY_SCROLL_UP: int
NCKEY_SCROLL_DOWN: int
NCKEY_RETURN: int
NCKEY_TAB: int
NCKEY_ESC: int
NCKEY_SPACE: int
NCKEY_MOD_SHIFT: int
NCKEY_MOD_ALT: int
NCKEY_MOD_CTRL: int
NCKEY_MOD_SUPER: int
NCKEY_MOD_HYPER: int
NCKEY_MOD_META: int
NCKEY_MOD_CAPSLOCK: int
NCKEY_MOD_NUMLOCK: int
# endregion nckey


# region ncoption
NCOPTION_INHIBIT_SETLOCALE: int
NCOPTION_NO_CLEAR_BITMAPS: int
NCOPTION_NO_WINCH_SIGHANDLER: int
NCOPTION_NO_QUIT_SIGHANDLERS: int
NCOPTION_PRESERVE_CURSOR: int
NCOPTION_SUPPRESS_BANNERS: int
NCOPTION_NO_ALTERNATE_SCREEN: int
NCOPTION_NO_FONT_CHANGES: int
NCOPTION_DRAIN_INPUT: int
NCOPTION_SCROLLING: int
NCOPTION_CLI_MODE: int
# endregion ncoption


NcInput = _c.NcInput


class NotcursesOptions:
    ...


class NcPlaneOptions:
    ...


class Notcurses:
    """Notcurses context."""

    def __init__(
            self,
            tty_fd: int = 0,
            term_type: str = "",
            renderfd: int = 0,
            loglevel: int = 0,
            margins_str: str = "",
            margin_t: int = 0, margin_r: int = 0,
            margin_b: int = 0, margin_l: int = 0,
            flags: int = 0):
        """Initialize new Notcruses context."""
        self._c = _c.Notcurses(
            tty_fd=tty_fd,
            term_type=term_type,
            renderfd=renderfd,
            loglevel=loglevel,
            margins_str=margins_str,
            margin_t=margin_t, margin_r=margin_r,
            margin_b=margin_b, margin_l=margin_l,
            flags=flags,
        )

    def drop_planes(self) -> None:
        """Destroy all ncplanes other than the stdplane."""
        self._c.drop_planes()

    def render(self) -> None:
        """Renders and rasterizes the standard pile in one shot.

        Blocking call.
        """
        self._c.render()

    def top(self) -> NcPlane:
        """Return the topmost ncplane of the standard pile."""
        return NcPlane(self._c.top())

    def bottom(self) -> NcPlane:
        """Return the bottommost ncplane of the standard pile."""
        return NcPlane(self._c.bottom())

    def inputready_fd(self) -> int:
        """Get a file descriptor suitable for input event poll."""
        return self._c.inputready_fd()

    def get(self, deadline: Optional[float]) -> NcInput:
        """Reads an input event. If no event is ready, returns None."""
        return self._c.get(deadline)

    def get_nblock(self) -> NcInput:
        """Get input event without blocking. If no event is ready,
        returns None."""
        return self._c.get_nblock()

    def get_blocking(self) -> NcInput:
        """Get input event completely blocking until and event or signal
        received."""
        return self._c.get_blocking()

    def mouse_enable(self) -> None:
        """Enable the mouse in \"button-event tracking\" mode with
        focus detection and UTF8-style extended coordinates."""
        self._c.mice_enable()

    def mouse_disable(self) -> None:
        """Disable mouse events.

        Any events in the input queue can still be delivered.
        """
        self._c.mice_disable()

    def linesigs_disable(self) -> None:
        """Disable signals originating from the terminal's line discipline.

        They are enabled by default.
        """
        self._c.linesigs_disable()

    def linesigs_enable(self) -> None:
        """Restore signals originating from the terminal's line discipline."""
        self._c.linesigs_enable()

    def refresh(self) -> Tuple[int, int]:
        """Refresh the physical screen to match what was last rendered.

        Return the new dimensions.
        """
        return self._c.refresh()

    def stdplane(self) -> NcPlane:
        """Get a reference to the standard plane.

        The standard plane always exists, and its origin is always at
        the uppermost, leftmost cell of the terminal.
        """
        return NcPlane(self._c.stdplane())

    def stddim_yx(self) -> Tuple[NcPlane, int, int]:
        """Get standard plane plus dimensions."""
        c_plane, y, x = self._c.stddim_yx()
        return NcPlane(c_plane), y, x

    def term_dim_yx(self) -> Tuple[int, int]:
        """Return our current idea of the terminal dimensions
        in rows and cols."""
        return self._c.term_dim_yx()

    def at_yx(self, yoff: int, xoff: int, /) -> Tuple[int, int]:
        """Retrieve the contents of the specified cells stylemask and channels
        as last rendered"""
        return self._c.at_yx(yoff, xoff)

    def pile_create(self, y_pos: int = 0, x_pos: int = 0,
                    rows: int = 0, cols: int = 0,
                    name: str = "",
                    flags: int = 0,
                    margin_b: int = 0, margin_r: int = 0) -> NcPlane:
        """Same as ncplane_create(), but creates a new pile.

        The returned plane will be the top, bottom, and root of this new pile.
        """
        return NcPlane(self._c.pile_create(
            y_pos=y_pos, x_pos=x_pos,
            rows=rows, cols=cols,
            name=name,
            flags=flags,
            margin_b=margin_b, margin_r=margin_r,
        ))

    def supported_styles(self) -> int:
        """Returns a 16-bit bitmask of supported curses-style attributes."""
        return self._c.supported_styles()

    def palette_size(self) -> int:
        """Returns the number of simultaneous colors claimed
        to be supported."""
        return self._c.palette_size()

    def cantruecolor(self) -> bool:
        """Can we directly specify RGB values per cell,
        or only use palettes?"""
        return self._c.cantruecolor()

    def canfade(self) -> bool:
        """Can we fade?"""
        return self._c.canfade()

    def canchangecolor(self) -> bool:
        """Can we set the \"hardware\" palette? """
        return self._c.canchangecolor()

    def canopen_images(self) -> bool:
        """Can we load images?

        This requires being built against FFmpeg/OIIO.
        """
        return self._c.canopen_images()

    def canopen_videos(self) -> bool:
        """Can we load videos?

        This requires being built against FFmpeg.
        """
        return self._c.canopen_videos()

    def canutf8(self) -> bool:
        """Is our encoding UTF-8?

        Requires LANG being set to a UTF8 locale.
        """
        return self._c.canutf8()

    def cansextant(self) -> bool:
        """Can we reliably use Unicode 13 sextants?"""
        return self._c.cansextant()

    def canbraille(self) -> bool:
        """Can we reliably use Unicode Braille?"""
        return self._c.canbraille()

    def check_pixel_support(self) -> bool:
        """This function must successfully return before NCBLIT_PIXEL
        is available.
        """
        return self._c.check_pixel_support()

    def stats(self) -> None:
        """Acquire an atomic snapshot of the Notcurses stats."""
        return self._c.stats()

    def stats_reset(self) -> None:
        """Reset all cumulative stats (immediate ones, such as fbbytes,
        are not reset) and returning a copy before reset."""
        return self._c.stats_reset()

    def cursor_enable(self) -> None:
        """Enable the terminal's cursor, if supported"""
        self._c.cursor_enable()

    def cursor_disable(self) -> None:
        """Disable the terminal's cursor."""
        self._c.cursor_disable()


class NcPlane:
    """Notcurses Plane"""

    def __init__(self, c_plane: _c.NcPlane):
        self._c = c_plane

    def create(self, rows: int, cols: int,
               y_pos: int = 0, x_pos: int = 0,
               name: str = "",
               flags: int = 0,
               margin_b: int = 0, margin_r: int = 0,) -> NcPlane:
        """Create a new ncplane bound to this plane."""
        return NcPlane(self._c.create(
            rows=rows, cols=cols,
            y_pos=y_pos, x_pos=x_pos,
            name=name,
            flags=flags,
            margin_b=margin_b, margin_r=margin_r,
        ))

    def destroy(self) -> None:
        """Destroy the plane.

        Do NOT try to use the plane after its been
        destoryed.
        """
        self._c.destroy()

    def dim_yx(self) -> Tuple[int, int]:
        """Return the dimensions of this NcPlane."""
        return self._c.dim_yx()

    def dim_x(self) -> int:
        """Return X dimension of this NcPlane."""
        return self._c.dim_x()

    def dim_y(self) -> int:
        """Return Y dimension of this NcPlane."""
        return self._c.dim_y()

    def pixel_geom(self) -> Tuple[int, int, int, int, int, int]:
        """Retrieve pixel geometry for the display region, each cell
        and the maximum displayable bitmap."""
        return self._c.pixel_geom()

    def set_resizecb(self) -> None:
        """Replace the ncplane's existing resize callback

        TODO
        """
        self._c.set_resizecb()

    def reparent(self, new_parent: NcPlane) -> None:
        """Plane will be unbound from its parent plane
        and will be made a bound child of passed plane."""
        self._c.reparent(new_parent._c)

    def reparent_family(self, new_parent: NcPlane) -> None:
        """The same as reparent(), except any planes bound
        to this plane come along with it to its new destination."""
        self._c.reparent_family(new_parent._c)

    def dup(self) -> NcPlane:
        """Duplicate an existing ncplane."""
        return NcPlane(self._c.dup())

    def translate(self,
                  another_plane: NcPlane,
                  /) -> Tuple[int, int]:
        """Return coordinates relative to another plane."""
        return self._c.translate(another_plane._c)

    def translate_abs(self) -> bool:
        """Check if coordinates are in the plane."""
        return self._c.translate_abs()

    def set_scrolling(self, state: bool, /) -> None:
        """All planes are created with scrolling disabled."""
        self._c.set_scrolling(state)

    def resize(self, keepy: int, keepx: int,
               keepleny: int, keeplenx: int,
               yoff: int, xoff: int,
               ylen: int, xlen: int,) -> None:
        """Resize the ncplane."""
        self._c.resize(keepy, keepx, keepleny, keeplenx, yoff, xoff, ylen, xlen)

    def resize_simple(self, ylen: int, xlen: int, /) -> None:
        """Resize the plane, retaining what data we can.

        Keep the origin where it is.
        """
        self._c.resize_simple(ylen, xlen)

    def set_base_cell(self) -> None:
        """Set the plane's base NcCell.

        TODO
        """
        self._c.set_base_cell()

    def set_base(self) -> None:
        """Set the plane's base NcCell.

        TODO
        """
        self._c.set_base()

    def base(self) -> None:
        """Extract the plane's base NcCell.

        TODO
        """
        self._c.base()

    def move_yx(self, y: int, x: int, /) -> None:
        """Move this plane relative to the standard plane,
        or the plane to which it is bound."""
        self._c.move_yx(y, x)

    def yx(self) -> Tuple[int, int]:
        """Get the origin of the plane relative to its
        bound plane, or pile."""
        return self._c.yx()

    def y(self) -> int:
        """Get the Y origin of the plane relative to its
        bound plane, or pile."""
        return self._c.y()

    def x(self) -> int:
        """Get the X origin of the plane relative to its
        bound plane, or pile."""
        return self._c.x()

    def abs_yx(self) -> Tuple[int, int]:
        """Get the origin of plane relative to its pile."""
        return self._c.abs_yx()

    def abs_y(self) -> int:
        """Get the Y origin of plane relative to its pile."""
        return self._c.abs_y()

    def abs_x(self) -> int:
        """Get the X origin of plane relative to its pile."""
        return self._c.abs_x()

    def parent(self) -> Optional[NcPlane]:
        """Get the plane to which the plane is bound or None
        if plane does not have parent.
        """
        p = self._c.parent()
        return NcPlane(p) if p is not None else None

    def descendant_p(self, ancestor: NcPlane, /) -> None:
        """Return True if plane is a proper descendent of passed
        'ancestor' plane.
        """
        return self._c.descendant_p(ancestor._c)

    def move_top(self) -> None:
        """Splice ncplane out of the z-buffer, and reinsert it at the top."""
        self._c.move_top()

    def move_bottom(self) -> None:
        """Splice ncplane out of the z-buffer, and reinsert it at
        the bottom.
        """
        self._c.move_bottom()

    def move_above(self, plane: NcPlane, /) -> None:
        """Splice ncplane out of the z-buffer, and reinsert it above passed
        plane."""
        self._c.move_above(plane._c)

    def move_below(self, plane: NcPlane, /) -> None:
        """Splice ncplane out of the z-buffer, and reinsert it bellow
        passed plane.
        """
        self._c.move_below(plane._c)

    def below(self) -> Optional[NcPlane]:
        """Return the plane below this one, or None if this is
        at the bottom.
        """
        p = self._c.below()
        return NcPlane(p) if p is not None else None

    def above(self) -> Optional[NcPlane]:
        """Return the plane above this one, or None if this is at the top."""
        p = self._c.above()
        return NcPlane(p) if p is not None else None

    def rotate_cw(self) -> None:
        """Rotate the plane π/2 radians clockwise."""
        self._c.rotate_cw()

    def rotate_ccw(self) -> None:
        """Rotate the plane π/2 radians counterclockwise."""
        self._c.rotate_ccw()

    def at_cursor(self) -> Tuple[str, int, int]:
        """Retrieve the current contents of the cell under the cursor."""
        return self._c.at_cursor()

    def at_cursor_cell(self) -> None:
        """Retrieve the current contents of the cell under the cursor.

        TODO
        """
        self._c.at_cursor_cell()

    def at_yx(self, y: int, x: int, /) -> Tuple[str, int, int]:
        """Retrieve the current contents of the specified cell."""
        return self._c.at_yx(y, x)

    def at_yx_cell(self) -> None:
        """"Retrieve the current contents of the specified cell"

        TODO
        """
        self._c.at_yx_cell()

    def contents(self, begy: int, begx: int,
                 leny: int = -1, lenx: int = -1) -> str:
        """Create a flat string from the EGCs of the selected region
        of the ncplane.
        """
        return self._c.contents(begy, begx, leny, lenx)

    def center_abs(self) -> Tuple[int, int]:
        """Return the plane center absolute coordiantes."""
        return self._c.center_abs()

    def halign(self, align: int, collumn: int, /) -> int:
        """Return the column at which cols ought start in
        order to be aligned.
        """
        return self._c.halign(align, collumn)

    def valign(self, align: int, collumn: int, /) -> int:
        """Return the row at which rows ought start in
        order to be aligned.
        """
        return self._c.valign(align, collumn)

    def cursor_move_yx(self, y: int, x: int, /) -> None:
        """Move the cursor to the specified position
        (the cursor needn't be visible).
        """
        self._c.cursor_move_yx(y, x)

    def home(self) -> None:
        """Move the cursor to 0, 0."""
        self._c.home()

    def cursor_yx(self) -> Tuple[int, int]:
        """Get the current position of the cursor within plane."""
        return self._c.cursor_yx()

    def channels(self) -> int:
        """Get the current channels or attribute word."""
        return self._c.channels()

    def styles(self) -> int:
        """Return the current styling for this ncplane."""
        return self._c.styles()

    def putc_yx(self) -> None:
        """Replace the cell at the specified coordinates with
        the provided cell.

        TODO
        """
        self._c.putc_yx()

    def putc(self) -> None:
        """Replace cell at the current cursor location.

        TODO
        """
        self._c.putc()

    def putchar_yx(self, y: int, x: int, char: str, /) -> None:
        """Replace the cell at the specified coordinates
        with the provided 7-bit char."""
        self._c.putchar_yx(y, x, char)

    def putchar(self, char: str) -> None:
        """Replace the cell at the current cursor location."""
        self._c.putchar(char)

    def putchar_stained(self, char: str, /) -> None:
        """Replace the EGC underneath us, but retain the styling."""
        self._c.putchar_stained(char)

    def putegc_yx(self, y: int, x: int, egc: str, /) -> int:
        """Replace the cell at the specified coordinates
        with the provided EGC.

        Returns number of collumns the cursor has advanced.
        """
        return self._c.putegc_yx(y, x, egc)

    def putegc(self, egc: str, /) -> int:
        """Replace the cell at the current cursor location
        with the provided EGC

        Returns number of collumns the cursor has advanced.
        """
        return self._c.putegc(egc)

    def putegc_stained(self, egc: str, /) -> int:
        """Replace the EGC underneath us, but retain the styling.

        Returns number of collumns the cursor has advanced.
        """
        return self._c.putegc_stained(egc)

    def putstr_yx(self, y: int, x: int, egc: str, /) -> None:
        """Write a series of EGCs to the location,
        using the current style.
        """
        self._c.putstr_yx(y, x, egc)

    def putstr(self, egc: str, /) -> None:
        """Write a series of EGCs to the current location,
        using the current style.
        """
        self._c.putstr(egc)

    def putstr_aligned(self, y: int, align: int, egc: str, /) -> None:
        """Write a series of EGCs to the current location,
        using the alignment.
        """
        self._c.putstr_aligned(y, align, egc)

    def putstr_stained(self, egc: str, /) -> None:
        """Replace a string's worth of glyphs at the current
        cursor location, but retain the styling."""
        self._c.putstr_stained(egc)

    def putnstr_yx(self, y: int, x: int, size: int, egc: str, /) -> None:
        """"Write a series of EGCs to the location, using the current
        style.
        """
        self._c.putnstr_yx(y, x, size, egc)

    def putnstr(self, size: int, egc: str, /) -> None:
        """Write a series of EGCs to the current location,
        using the current style.
        """
        self._c.putnstr(size, egc)

    def putnstr_aligned(self, y: int, align: int,
                        size: int, egc: str, /) -> None:
        """Write a series of EGCs to the current location,
        using the alignment.
        """
        self._c.putnstr_aligned(y, align, size, egc)

    def puttext(self, y: int, align: int, /) -> int:
        """Write the specified text to the plane, breaking lines sensibly,
        beginning at the specified line.

        Returns the number of columns written.
        """
        return self._c.puttext(y, align)

    def box(self) -> None:
        """Draw a box with its upper-left corner
        at the current cursor position.

        TODO
        """
        self._c.box()

    def box_sized(self) -> None:
        """Draw a box with its upper-left corner at
        the current cursor position, having dimensions.

        TODO
        """
        self._c.box_sized()

    def perimeter(self) -> None:
        """Draw a perimeter with its upper-left corner
        at the current cursor position

        TODO
        """
        self._c.perimeter()

    def polyfill_yx(self) -> None:
        """Starting at the specified coordinate, if its glyph
        is different from that of is copied into it, and the
        original glyph is considered the fill target.

        TODO
        """
        self._c.polyfill_yx()

    def gradient(self, egc: str, stylemask: int,
                 ul: int, ur: int, ll: int, lr: int,
                 ystop: int, xstop: int,) -> int:
        """Draw a gradient with its upper-left corner
        at the current cursor position.

        Returns cells filled.
        """
        return self._c.gradient(egc, stylemask, ul, ur, ll, lr, ystop, xstop)

    def highgradient(self,
                     ul: int, ur: int, ll: int, lr: int,
                     ystop: int, xstop: int) -> int:
        """Do a high-resolution gradient using upper blocks
        and synced backgrounds.

        Returns cells filled.
        """
        return self._c.highgradient(ul, ur, ll, lr, ystop, xstop)

    def gradient_sized(self, egc: str, stylemask: int,
                       ul: int, ur: int, ll: int, lr: int,
                       ylen: int, xlen: int,) -> int:
        """Draw a gradient with its upper-left corner
        at the current cursor position.

        Returns cells filled.
        """
        return self._c.gradient_sized(egc, stylemask, ul, ur, ll, lr, ylen, xlen)

    def highgradient_sized(self,
                           ul: int, ur: int, ll: int, lr: int,
                           ylen: int, xlen: int,) -> int:
        """NcPlane.gradent_sized() meets NcPlane.highgradient().

        Returns cells filled.
        """
        return self._c.highgradient_sized(ul, ur, ll, lr, ylen, xlen)

    def format(self, ystop: int, xstop: int,
               stylemark: int, /) -> int:
        """Set the given style throughout the specified region,
        keeping content and attributes unchanged.

        Returns the number of cells set.
        """
        return self._c.format(ystop, xstop, stylemark)

    def stain(self, ystop: int, xstop: int,
              ul: int, ur: int, ll: int, lr: int) -> int:
        """Set the given style throughout the specified region,
        keeping content and attributes unchanged.

        Returns the number of cells set.
        """
        return self._c.stain(ystop, xstop, ul, ur, ll, lr)

    def mergedown_simple(self, dst: NcPlane, /) -> None:
        """Merge the ncplane down onto the passed ncplane."""
        self._c.mergedown_simple(dst._c)

    def mergedown(self, dst: NcPlane,
                  begsrcy: int = 0, begsrcx: int = 0,
                  leny: int = 0, lenx: int = 0,
                  dsty: int = 0, dstx: int = 0) -> None:
        """Merge with parameters the ncplane down onto the passed ncplane."""
        self._c.mergedown(dst._c, begsrcy, begsrcx, leny, lenx, dsty, dstx)

    def erase(self) -> None:
        """Erase every cell in the ncplane."""
        self._c.erase()

    def bchannel(self) -> int:
        """Extract the 32-bit working background channel from an ncplane."""
        return self._c.bchannel()

    def fchannel(self) -> int:
        """Extract the 32-bit working foreground channel from an ncplane."""
        return self._c.fchannel()

    def set_channels(self, channels: int, /) -> None:
        """Set both foreground and background channels of the plane."""
        self._c.set_channels(channels)

    def set_styles(self, stylebits: int, /) -> None:
        """Set the specified style bits for the plane,
        whether they're actively supported or not.
        """
        self._c.set_styles(stylebits)

    def on_styles(self, stylebits: int, /) -> None:
        """Add the specified styles to the ncplane's existing spec."""
        self._c.on_styles(stylebits)

    def off_styles(self, stylebits: int, /) -> None:
        """Remove the specified styles from the ncplane's existing spec."""
        self._c.off_styles(stylebits)

    def fg_rgb(self) -> int:
        """Extract 24 bits of working foreground RGB from the plane,
        shifted to LSBs.
        """
        return self._c.fg_rgb()

    def bg_rgb(self) -> int:
        """Extract 24 bits of working background RGB from the plane,
        shifted to LSBs."""
        return self._c.bg_rgb()

    def fg_alpha(self) -> int:
        """Extract 2 bits of foreground alpha from plane,
        shifted to LSBs.
        """
        return self._c.fg_alpha()

    def fg_default_p(self) -> bool:
        """Is the plane's foreground using the \"default foreground color\"?"""
        return self._c.fg_default_p()

    def bg_alpha(self) -> int:
        """Extract 2 bits of background alpha from the plane,
        shifted to LSBs.
        """
        return self._c.bg_alpha()

    def bg_default_p(self) -> bool:
        """Is the plane's background using the \"default background color\"?"""
        return self._c.bg_default_p()

    def fg_rgb8(self) -> Tuple[int, int, int]:
        """Extract 24 bits of foreground RGB from the plane,
        split into components.
        """
        return self._c.fg_rgb8()

    def bg_rgb8(self) -> Tuple[int, int, int]:
        """Is the plane's background using the \"default background color\"?"""
        return self._c.bg_rgb8()

    def set_fchannel(self, channel: int, /) -> int:
        """Set an entire foreground channel of the plane,
        return new channels.
        """
        return self._c.set_fchannel(channel)

    def set_bchannel(self, channel: int, /) -> int:
        """Set an entire background channel of the plane,
        return new channels.
        """
        return self._c.set_bchannel(channel)

    def set_fg_rgb8(self, red: int, green: int, blue: int, /) -> None:
        """Set the current foreground color using RGB specifications."""
        self._c.set_fg_rgb8(red, green, blue)

    def set_bg_rgb8(self, red: int, green: int, blue: int, /) -> None:
        """Set the current background color using RGB specifications."""
        self._c.set_bg_rgb8(red, green, blue)

    def set_bg_rgb8_clipped(self, red: int, green: int, blue: int, /) -> None:
        """Set the current foreground color using RGB specifications
        but clipped to [0..255]."""
        self._c.set_bg_rgb8_clipped(red, green, blue)

    def set_fg_rgb8_clipped(self, red: int, green: int, blue: int, /) -> None:
        """Set the current background color using RGB specifications
        but clipped to [0..255]."""
        self._c.set_fg_rgb8_clipped(red, green, blue)

    def set_fg_rgb(self, channel: int, /) -> None:
        """Set the current foreground color using channel."""
        self._c.set_fg_rgb(channel)

    def set_bg_rgb(self, channel: int, /) -> None:
        """Set the current background color using channel."""
        self._c.set_bg_rgb(channel)

    def set_fg_default(self) -> None:
        """Use the default color for the foreground."""
        self._c.set_fg_default()

    def set_bg_default(self) -> None:
        """Use the default color for the background."""
        self._c.set_bg_default()

    def set_fg_palindex(self, idx: int, /) -> None:
        """Set the ncplane's foreground palette index."""
        self._c.set_fg_palindex(idx)

    def set_bg_palindex(self, idx: int, /) -> None:
        """Set the ncplane's background palette index."""
        self._c.set_bg_palindex(idx)

    def set_fg_alpha(self, aplha: int, /) -> None:
        """Set the foreground alpha parameters for the plane."""
        self._c.set_fg_alpha(aplha)

    def set_bg_alpha(self, aplha: int, /) -> None:
        """Set the current background color using channel."""
        self._c.set_bg_alpha(aplha)

    def fadeout(self) -> None:
        """Fade the ncplane out over the provided time,
        calling 'fader' at each iteration.

        TODO
        """
        self._c.fadeout()

    def fadein(self) -> None:
        """Fade the ncplane in over the specified time.

        TODO
        """
        self._c.fadein()

    def fade_setup(self) -> None:
        """Create NcFadeCtx.

        TODO
        """
        self._c.fade_setup()

    def fadeout_iteration(self) -> None:
        """TODO"""
        self._c.fadeout_iteration()

    def fadein_iteration(self) -> None:
        """TODO"""
        self._c.fadein_iteration()

    def pulse(self) -> None:
        """Pulse the plane in and out until the callback returns non-zero.

        TODO
        """
        self._c.pulse()

    def cells_load_box(self) -> None:
        """Load up six cells with the EGCs necessary to draw a box.

        TODO
        """
        self._c.cells_load_box()

    def cells_rounded_box(self) -> None:
        """Load up six cells with the EGCs necessary to draw a round box.

        TODO
        """
        self._c.cells_rounded_box()

    def perimeter_rounded(
            self,
            stylemask: int, channels: int,
            ctlword: int,) -> None:
        """Draw a perimeter around plane."""
        self._c.perimeter_rounded(stylemask, channels, ctlword)

    def rounded_box_sized(self,
                          styles: int, channels: int,
                          ylen: int, xlen: int,
                          ctlword: int) -> None:
        """Draw a round box around plane."""
        self._c.rounded_box_sized(styles, channels, ylen, xlen, ctlword)

    def cells_double_box(self) -> None:
        """Draw a double box with cells.

        TODO
        """
        self._c.cells_double_box()

    def double_box(self,
                   styles: int, channels: int,
                   ylen: int, xlen: int,
                   ctlword: int) -> None:
        """Draw a double box."""
        self._c.double_box(styles, channels, ylen, xlen, ctlword)

    def perimeter_double(self,
                         styles: int, channels: int,
                         ctlword: int) -> None:
        """Draw a double perimeter."""
        self._c.perimeter_double(styles, channels, ctlword)

    def double_box_sized(self,
                         styles: int, channels: int,
                         ylen: int, xlen: int,
                         ctlword: int) -> None:
        """Draw a double box sized."""
        self._c.double_box_sized(styles, channels, ylen, xlen, ctlword)

    def ncvisual_from_plane(self) -> None:
        """Promote an plane to an NcVisual.

        TODO
        """
        self._c.ncvisual_from_plane()

    def as_rgba(self) -> None:
        """Create an RGBA flat array from the selected
        region of the plane.

        TODO
        """
        self._c.as_rgba()

    def reel_create(self) -> None:
        """Take over the plane and use it to draw a reel.

        TODO
        """
        self._c.reel_create()

    def greyscale(self) -> None:
        """Convert the plane's content to greyscale."""
        self._c.greyscale()

    def selector_create(self) -> None:
        """Create NcSelector.

        TODO
        """
        self._c.selector_create()

    def multiselector_create(self) -> None:
        """Create MultiSelector.

        TODO
        """
        self._c.multiselector_create()

    def tree_create(self) -> None:
        """Create NcTree.

        TODO
        """
        self._c.tree_create()

    def menu_create(self) -> None:
        """Create NcMenu.

        TODO
        """
        self._c.menu_create()

    def progbar_create(self) -> None:
        """Create NcProgbar.

        TODO
        """
        self._c.progbar_create()

    def tabbed_create(self) -> None:
        """Create NcTabbed.

        TODO
        """
        self._c.tabbed_create()

    def uplot_create(self) -> None:
        """Create NcUplot.

        TODO
        """
        self._c.uplot_create()

    def dplot_create(self) -> None:
        """Create NcDplot.

        TODO
        """
        self._c.dplot_create()

    def fdplane_create(self) -> None:
        """Create NcFdPlane.

        TODO
        """
        self._c.fdplane_create()

    def subproc_createv(self) -> None:
        """Create subprocess plane.

        TODO
        """
        self._c.subproc_createv()

    def subproc_createvp(self) -> None:
        """Create subprocess plane.

        TODO
        """
        self._c.subproc_createvp()

    def subproc_createvpe(self) -> None:
        """Create subprocess plane.

        TODO
        """
        self._c.subproc_createvpe()

    def qrcode(self, data: bytes, /) -> Tuple[int, int]:
        """Create QR code, return y and x size."""
        return self._c.qrcode(data)

    def reader_create(self) -> None:
        """Create NcReader.

        TODO
        """
        self._c.reader_create()

    def pile_top(self) -> NcPlane:
        """Return the topmost plane of the pile."""
        return NcPlane(self._c.pile_top())

    def pile_bottom(self) -> NcPlane:
        """Return the bottommost plane of the pile."""
        return NcPlane(self._c.pile_bottom())

    def pile_render(self) -> None:
        """Renders the pile of which plane is a part."""
        self._c.pile_render()

    def pile_rasterize(self) -> None:
        """Make the physical screen match the last
        rendered frame from the pile."""
        self._c.pile_rasterize()

    def pile_render_to_buffer(self) -> bytes:
        """Perform the rendering and rasterization portion of render()
        and write it to bytes object instead of terminal."""
        return self._c.pile_render_to_buffer()

    def pile_render_to_file(self, fd: int, /) -> None:
        """Write the last rendered frame, in its entirety, to file descriptor.

        If render() has not yet been called, nothing will be written.
        """
        self._c.pile_render_to_file(fd)

    def scrollup(self, r: int, /) -> None:
        """Effect scroll events on the plane."""
        self._c.scrollup(r)


NCBOXASCII: str
NCBOXDOUBLE: str
NCBOXHEAVY: str
NCBOXLIGHT: str
NCBOXOUTER: str
NCBOXROUND: str

# region functions from functions.c
def box(
    plane: NcPlane, ystop: int, xstop: int,
    box_chars: str, styles: int, fg: int, bg: int,
    ctlword: int,
) -> None:
    """Draw a box."""
    _c.box(
        plane._c, ystop, xstop, box_chars, styles, fg, bg, ctlword
    )


def rgb(r: int, g: int, b: int) -> int:
    """Create an RGB channel."""
    return _c.rgb(r, g, b)
# endregion
