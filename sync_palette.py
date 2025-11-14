#!/usr/bin/env python3
"""Sync shared palette data into the theme configs."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

BASE_DIR = Path(__file__).resolve().parent
PALETTE_FILE = BASE_DIR / "palette.json"


def load_palette() -> dict[str, object]:
    with PALETTE_FILE.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def ensure_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"


def write_file(path: Path, content: str) -> None:
    path.write_text(ensure_newline(content), encoding="utf-8")


def format_alacritty(palette: dict[str, object]) -> str:
    normal = palette["normal"]
    bright = palette["bright"]
    return dedent(
        f"""\
        [colors.primary]
        background = "{palette['background']}"
        foreground = "{palette['foreground']}"

        [colors.cursor]
        text = "{palette['background']}"
        cursor = "{palette['foreground']}"

        [colors.vi_mode_cursor]
        text = "{palette['background']}"
        cursor = "{palette['foreground']}"

        [colors.search.matches]
        foreground = "{palette['background']}"
        background = "{palette['foreground']}"

        [colors.search.focused_match]
        foreground = "CellBackground"
        background = "CellForeground"

        [colors.line_indicator]
        foreground = "None"
        background = "None"

        [colors.footer_bar]
        foreground = "{palette['bright']['black']}"
        background = "{palette['foreground']}"

        [colors.selection]
        text = "CellBackground"
        background = "CellForeground"

        [colors.normal]
        black = "{normal['black']}"
        red = "{normal['red']}"
        green = "{normal['green']}"
        yellow = "{normal['yellow']}"
        blue = "{normal['blue']}"
        magenta = "{normal['magenta']}"
        cyan = "{normal['cyan']}"
        white = "{normal['white']}"

        [colors.bright]
        black = "{bright['black']}"
        red = "{bright['red']}"
        green = "{bright['green']}"
        yellow = "{bright['yellow']}"
        blue = "{bright['blue']}"
        magenta = "{bright['magenta']}"
        cyan = "{bright['cyan']}"
        white = "{bright['white']}"

        [colors.dim]
        black = "{palette['foreground']}"
        red = "{bright['red']}"
        green = "{bright['green']}"
        yellow = "{bright['yellow']}"
        blue = "{bright['blue']}"
        magenta = "{bright['magenta']}"
        cyan = "{bright['cyan']}"
        white = "{bright['black']}"
        """
    ).strip()


def format_kitty(palette: dict[str, object]) -> str:
    normal = palette["normal"]
    bright = palette["bright"]
    return dedent(
        f"""\
        background            {palette['background']}
        foreground            {palette['foreground']}

        # black
        color0  {normal['black']}
        color8  {bright['black']}

        # red
        color1  {normal['red']}
        color9  {bright['red']}

        # green
        color2  {normal['green']}
        color10 {bright['green']}

        # yellow
        color3  {normal['yellow']}
        color11 {bright['yellow']}

        # blue
        color4  {normal['blue']}
        color12 {bright['blue']}

        # magenta
        color5  {normal['magenta']}
        color13 {bright['magenta']}

        #cyan
        color6  {normal['cyan']}
        color14 {bright['cyan']}

        #white
        color7  {normal['white']}
        color15 {bright['white']}
        """
    ).strip() + "\n\n"


def format_ghostty(palette: dict[str, object]) -> str:
    normal = palette["normal"]
    bright = palette["bright"]
    lines = [
        "# Background and foreground colors",
        f"background = {palette['background']}",
        f"foreground = {palette['foreground']}",
        "",
        "# Standard colors",
    ]
    lines.extend(
        f"palette = {idx}={color}"
        for idx, color in enumerate(
            [
                normal["black"],
                normal["red"],
                normal["green"],
                normal["yellow"],
                normal["blue"],
                normal["magenta"],
                normal["cyan"],
                normal["white"],
            ]
        )
    )
    lines.extend(["", "# Bright colors"])
    lines.extend(
        f"palette = {idx}={color}"
        for idx, color in enumerate(
            [
                bright["black"],
                bright["red"],
                bright["green"],
                bright["yellow"],
                bright["blue"],
                bright["magenta"],
                bright["cyan"],
                bright["white"],
            ],
            start=8,
        )
    )
    return "\n".join(lines)


def format_warp(palette: dict[str, object]) -> str:
    normal = palette["normal"]
    bright = palette["bright"]
    return dedent(
        f"""\
        name: Aether
        accent: "{palette['accent']}"
        cursor: "{palette['cursor']}"
        background: "{palette['background']}"
        foreground: "{palette['foreground']}"
        details: {palette['details']}

        terminal_colors:
          normal:
            black:   "{normal['black']}"
            red:     "{normal['red']}"
            green:   "{normal['green']}"
            yellow:  "{normal['yellow']}"
            blue:    "{normal['blue']}"
            magenta: "{normal['magenta']}"
            cyan:    "{normal['cyan']}"
            white:   "{normal['white']}"
          bright:
            black:   "{bright['black']}"
            red:     "{bright['red']}"
            green:   "{bright['green']}"
            yellow:  "{bright['yellow']}"
            blue:    "{bright['blue']}"
            magenta: "{bright['magenta']}"
            cyan:    "{bright['cyan']}"
            white:   "{bright['white']}"
        """
    ).strip()


def format_btop(palette: dict[str, object]) -> str:
    normal = palette["normal"]
    bright = palette["bright"]
    return dedent(
        f"""\
        # Main background, empty for terminal default, need to be empty if you want transparent background
        theme[main_bg]="{palette['background']}"

        # Main text color
        theme[main_fg]="{palette['foreground']}"

        # Title color for boxes
        theme[title]="{normal['magenta']}"

        # Highlight color for keyboard shortcuts
        theme[hi_fg]="{normal['cyan']}"

        # Background color of selected item in processes box
        theme[selected_bg]="{bright['black']}"

        # Foreground color of selected item in processes box
        theme[selected_fg]="{palette['foreground']}"

        # Color of inactive/disabled text
        theme[inactive_fg]="{bright['black']}"

        # Misc colors for processes box including mini cpu graphs, details memory graph and details status text
        theme[proc_misc]="{normal['magenta']}"

        # Box outline and divider line color
        theme[cpu_box]="{normal['green']}"
        theme[mem_box]="{normal['green']}"
        theme[net_box]="{normal['green']}"
        theme[proc_box]="{normal['green']}"
        theme[div_line]="{bright['black']}"

        # Gradient for all meters and graphs
        theme[temp_start]="{normal['cyan']}"
        theme[temp_mid]="{normal['blue']}"
        theme[temp_end]="{normal['green']}"


        theme[cpu_start]="{normal['cyan']}"
        theme[cpu_mid]="{normal['blue']}"
        theme[cpu_end]="{normal['green']}"


        theme[free_start]="{normal['blue']}"
        theme[free_mid]="{normal['yellow']}"
        theme[free_end]="{normal['yellow']}"


        theme[cached_start]="{normal['yellow']}"
        theme[cached_mid]="{normal['yellow']}"
        theme[cached_end]="{normal['yellow']}"


        theme[available_start]="{normal['cyan']}"
        theme[available_mid]="{normal['cyan']}"
        theme[available_end]="{normal['cyan']}"


        theme[used_start]="{normal['green']}"
        theme[used_mid]="{normal['green']}"
        theme[used_end]="{normal['green']}"


        theme[download_start]="{normal['yellow']}"
        theme[download_mid]="{normal['cyan']}"
        theme[download_end]="{normal['blue']}"


        theme[upload_start]="{normal['yellow']}"
        theme[upload_mid]="{normal['cyan']}"
        theme[upload_end]="{normal['blue']}"
        """
    ).strip()


def hex_to_rgb_tuple(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[idx : idx + 2], 16) for idx in (0, 2, 4))


def format_chromium(palette: dict[str, object]) -> str:
    return ",".join(str(component) for component in hex_to_rgb_tuple(palette["background"]))


def main() -> None:
    palette = load_palette()
    write_file(BASE_DIR / "alacritty.toml", format_alacritty(palette))
    write_file(BASE_DIR / "kitty.conf", format_kitty(palette))
    write_file(BASE_DIR / "ghostty.conf", format_ghostty(palette))
    write_file(BASE_DIR / "warp.yaml", format_warp(palette))
    write_file(BASE_DIR / "btop.theme", format_btop(palette))
    write_file(BASE_DIR / "chromium.theme", format_chromium(palette))


if __name__ == "__main__":
    main()
