# ElegantFin for Jellyfin 12

[![jsDelivr hits](https://img.shields.io/jsdelivr/gh/hm/mihaif7/elegantfin-jf12?style=flat&logo=jsdelivr&label=jsDelivr%20hits)](https://www.jsdelivr.com/package/gh/mihaif7/elegantfin-jf12)
[![Release](https://img.shields.io/github/v/release/mihaif7/elegantfin-jf12?style=flat&logo=github&label=Release)](https://github.com/mihaif7/elegantfin-jf12/releases/latest)
[![Released](https://img.shields.io/github/release-date/mihaif7/elegantfin-jf12?style=flat&label=Released)](https://github.com/mihaif7/elegantfin-jf12/releases/latest)

A companion stylesheet that makes [ElegantFin](https://github.com/lscambo13/ElegantFin)
work on Jellyfin 12's **Modern** layout, so you don't have to switch Display
Mode back to Legacy to keep your theme.

It layers on top of upstream ElegantFin rather than forking it, so everything
that still works keeps flowing from upstream.

## Why this exists

I made this for myself because switching Display Mode back to Legacy on every device
got annoying enough to fix.

**It's meant to be temporary.** ElegantFin's maintainer has
[declined to support the Modern UI for now](https://github.com/lscambo13/ElegantFin/issues/309),
which is fair: the Jellyfin team is still actively developing it, and it's a
moving target. This fills the gap until either the UI settles down or upstream
takes it on. When that happens, this repo has done its job.

It is **not a fork and not a replacement**. It bundles none of ElegantFin's
code; it only layers on top. The design work is all
[lscambo13](https://github.com/lscambo13)'s, and every update to the theme
itself still comes from them.

## Screenshots

ElegantFin on Jellyfin 12's Modern layout, without this sheet and with it. The
untreated side pushes the poster grid down the page and paints the active tab
and Play All in MUI's indigo instead of the theme's own colours.

<details open>
<summary><strong>Desktop</strong> — home, library, sort menu, item details, player</summary>

<table>
<thead><tr><th width="10%"></th><th width="45%">Before</th><th width="45%">After</th></tr></thead>
<tbody>
<tr><td><strong>Home</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/home-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/home-before.webp" width="100%" alt="Home without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/home-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/home-after.webp" width="100%" alt="Home with the sheet"></a></td></tr>
<tr><td><strong>Library</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movies-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movies-before.webp" width="100%" alt="Movies library without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movies-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movies-after.webp" width="100%" alt="Movies library with the sheet"></a></td></tr>
<tr><td><strong>Sort menu</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/dropdown-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/dropdown-before.webp" width="100%" alt="Library sort menu without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/dropdown-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/dropdown-after.webp" width="100%" alt="Library sort menu with the sheet"></a></td></tr>
<tr><td><strong>Item details</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movie-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movie-before.webp" width="100%" alt="Item details without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movie-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/movie-after.webp" width="100%" alt="Item details with the sheet"></a></td></tr>
<tr><td><strong>Player</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/player-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/player-before.webp" width="100%" alt="Video player without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/player-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/desktop/player-after.webp" width="100%" alt="Video player with the sheet"></a></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>Mobile</strong> — home, library, sort menu, item details, drawer, player</summary>

<table>
<thead><tr><th width="10%"></th><th width="45%">Before</th><th width="45%">After</th></tr></thead>
<tbody>
<tr><td><strong>Home</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/home-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/home-before.webp" width="100%" alt="Home on mobile without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/home-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/home-after.webp" width="100%" alt="Home on mobile with the sheet"></a></td></tr>
<tr><td><strong>Library</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movies-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movies-before.webp" width="100%" alt="Movies library on mobile without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movies-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movies-after.webp" width="100%" alt="Movies library on mobile with the sheet"></a></td></tr>
<tr><td><strong>Sort menu</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/dropdown-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/dropdown-before.webp" width="100%" alt="Library sort menu on mobile without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/dropdown-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/dropdown-after.webp" width="100%" alt="Library sort menu on mobile with the sheet"></a></td></tr>
<tr><td><strong>Item details</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movie-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movie-before.webp" width="100%" alt="Item details on mobile without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movie-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/movie-after.webp" width="100%" alt="Item details on mobile with the sheet"></a></td></tr>
<tr><td><strong>Drawer</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/menu-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/menu-before.webp" width="100%" alt="Navigation drawer without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/menu-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/menu-after.webp" width="100%" alt="Navigation drawer with the sheet"></a></td></tr>
<tr><td><strong>Player</strong></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/player-before.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/player-before.webp" width="100%" alt="Video player on mobile without the sheet"></a></td><td><a href="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/player-after.webp"><img src="https://raw.githubusercontent.com/mihaif7/elegantfin-jf12/main/Previews/previews-v26.09.10/mobile/player-after.webp" width="100%" alt="Video player on mobile with the sheet"></a></td></tr>
</tbody>
</table>

</details>

## Install

Paste into **Dashboard → General → Custom CSS** (server-wide) or
**Settings → Display → Custom CSS** (just you):

```css
/* Main ElegantFin CSS */
@import url("https://cdn.jsdelivr.net/gh/lscambo13/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");

/* ElegantFin Media Bar CSS */
@import url("https://cdn.jsdelivr.net/gh/lscambo13/ElegantFin@main/Theme/assets/add-ons/media-bar-plugin-support-latest-min.css");

/* ElegantFin 12 Companion CSS */
@import url("https://cdn.jsdelivr.net/gh/mihaif7/elegantfin-jf12@main/Theme/ElegantFin-jf12-modern-latest.css");
```

Line 1 is ElegantFin itself. Line 2 is its Media Bar add-on, it's harmless without
the [Media Bar](https://github.com/CodeDevMLH/jellyfin-plugin-media-bar-enhanced)
plugin, needed with it. Line 3 is this sheet, and it has to come **last**.

If you'd rather not import from a URL, paste the contents of
[`ElegantFin-jf12-modern-latest.css`](Theme/ElegantFin-jf12-modern-latest.css)
in place of that third line.

## Updating

The URL above tracks the newest release, so updates arrive on their own, but
your browser caches the file for up to a week, so **hard-refresh** to pull one
in sooner. What changed in each version is on the
[releases page](https://github.com/mihaif7/elegantfin-jf12/releases).

To pin a version instead, name it in the URL. It will then never change:

```css
@import url("https://cdn.jsdelivr.net/gh/mihaif7/elegantfin-jf12@v26.09.10/Theme/ElegantFin-jf12-modern-v26.09.10.css");
```

## Tuning

Override any of these in your own Custom CSS, after the imports:

```css
:root {
    --ef12-appBarHeight: 3.5rem;
    --ef12-navPillBackground: none;
}
```

| Variable | Default | What it does |
|---|---|---|
| `--ef12-appBarHeight` | `4rem` | App bar height |
| `--ef12-appBarHeightDesktop` | `4.5rem` | App bar height, desktop layout only |
| `--ef12-libraryToolbarHeight` | `3.75rem` | Secondary toolbar on library pages |
| `--ef12-libraryToolbarGap` | `0.75rem` | Space under the wrapped toolbar row on mobile |
| `--ef12-appBarFade` | `2.5rem` | How far the bar's fill carries below itself when scrolled; `0` for a hard edge |
| `--ef12-navRadius` | `1rem` | Library nav button corners |
| `--ef12-navPaddingInline` | `1.1rem` | Horizontal room inside the nav pills |
| `--ef12-navGap` | `0.6rem` | Gap between adjacent nav pills |
| `--ef12-navPillBackground` | `--darkerGradientPointAlpha` | `none` for flat nav buttons |
| `--ef12-iconButtonGap` | `0.58rem` | Gap between header icon buttons |
| `--ef12-appBarIconSize` | `1.25rem` | App bar icon glyph size |
| `--ef12-surfaceRadius` | `1rem` | Menu / popover / dialog corners |
| `--ef12-surfaceBlur` | `--blurDefault` | Blur behind menus and dialogs; `none` to disable |
| `--ef12-menuGap` | `0.5rem` | Space between a dropdown and the control that opened it |
| `--ef12-osdToolbarHeight` | `5rem` | Toolbar height inside the video OSD header |
| `--ef12-episodePreviewIcon` | `"video_library"` | Glyph for the in-player episode picker |
| `--ef12-linkMarkHeight` | `1.4cap` | Logo mark height in the external-links row |
| `--ef12-mediaBarHeight` | `62vh` | Media Bar only: bar height, and what the home sections clear |
| `--ef12-mediaBarGap` | `1.25rem` | Media Bar only: the gap above and below the bar |

Upstream ElegantFin's own knobs still work too, including the solid and fully
transparent app bar presets from its README.

## Compatibility

- Jellyfin **12.0**, Modern layout, desktop and mobile.
- ElegantFin **v26.09.05** or later.
- Safe to leave installed on Legacy, everything structural is scoped with
  `:has(.MuiAppBar-root)`, which only matches the Modern layout.
- Non-dark colour schemes fall back to ElegantFin's dark tokens, as they do
  upstream.

If content sits far down the page under a large gap, or buttons come out
indigo, this sheet isn't loading last. Check the import order.

## Credits

[ElegantFin](https://github.com/lscambo13/ElegantFin) by
[lscambo13](https://github.com/lscambo13) - If you like the design go and thank them for the effort :)

[GPL-2.0](LICENSE), matching upstream.
