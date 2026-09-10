# ElegantFin for Jellyfin 12

A companion stylesheet that makes [ElegantFin](https://github.com/lscambo13/ElegantFin)
work on Jellyfin 12's **Modern** layout, so you don't have to switch Display
Mode back to Legacy to keep your theme.

It layers on top of upstream ElegantFin rather than forking it, so everything
that still works keeps flowing from upstream.

## Why this exists

I made this for myself — switching Display Mode back to Legacy on every device
got annoying enough to fix — and I'm sharing it in case it saves someone else
the same trouble.

**It's meant to be temporary.** ElegantFin's maintainer has
[declined to support the Modern UI for now](https://github.com/lscambo13/ElegantFin/issues/309),
which is fair: the Jellyfin team is still actively developing it, and it's a
moving target. This fills the gap until either the UI settles down or upstream
takes it on. When that happens, this repo has done its job — use ElegantFin on
its own.

It is **not a fork and not a replacement**. It bundles none of ElegantFin's
code; it only layers on top. The design work is all
[lscambo13](https://github.com/lscambo13)'s, and every update to the theme
itself still comes from them.

## Screenshots

_Coming soon._

## Install

Paste into **Dashboard → General → Custom CSS** (server-wide) or
**Settings → Display → Custom CSS** (just you):

```css
@import url("https://cdn.jsdelivr.net/gh/lscambo13/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
@import url("https://cdn.jsdelivr.net/gh/lscambo13/ElegantFin@main/Theme/assets/add-ons/media-bar-plugin-support-latest-min.css");
@import url("https://cdn.jsdelivr.net/gh/mihaif7/elegantfin-jf12@main/Theme/ElegantFin-jf12-modern-latest.css");
```

Line 1 is ElegantFin itself. Line 2 is its Media Bar add-on — harmless without
the [Media Bar](https://github.com/IAmParadox27/jellyfin-plugin-media-bar)
plugin, needed with it. Line 3 is this sheet, and it has to come **last**.

Then set **Settings → Display → Display Mode** to `Desktop` or `Mobile` — the
Modern layout, not `(Legacy)` — and hard-refresh. Jellyfin caches custom CSS
aggressively; on the mobile and TV apps, sign out and back in.

If you'd rather not import from a URL, paste the contents of
[`ElegantFin-jf12-modern-latest.css`](Theme/ElegantFin-jf12-modern-latest.css)
in place of that third line. Both shapes were measured on a live 12.0 server and
produce identical computed styles.

## Updating

The URL above tracks the newest release, so updates arrive on their own — but
your browser caches the file for up to a week, so **hard-refresh** to pull one
in sooner. What changed in each version is on the
[releases page](https://github.com/mihaif7/elegantfin-jf12/releases).

To pin a version instead, name it in the URL. It will then never change:

```css
@import url("https://cdn.jsdelivr.net/gh/mihaif7/elegantfin-jf12@v26.09.10/Theme/ElegantFin-jf12-modern-v26.09.10.css");
```

## What it does

Jellyfin 12 didn't rewrite the whole web UI — cards, the home page, item
details and the video OSD are still the legacy DOM, so most of ElegantFin
already applies unchanged. What changed is the chrome: the app bar, library
toolbar, drawer, menus and dialogs are now MUI components that ElegantFin has
no rules for. So this sheet:

- **bridges ElegantFin's tokens onto Jellyfin 12's `--jf-palette-*` variables**,
  so every MUI surface picks up the theme;
- **fixes the layout maths**, where ElegantFin's legacy header reservations now
  stack on top of the Modern layout's own spacing and push content down the page;
- **restyles the MUI chrome in ElegantFin's language** — its gradient header,
  its nav pills, its blurred translucent panels.

Everything is matched element-by-element against ElegantFin on a stock 10.11
server, comparing computed styles rather than eyeballing screenshots.

Three plugins get accommodations, all inert if the plugin isn't installed:
**Media Bar** (bar and home sections re-anchored so they stop overlapping below
`75em`, and its overlay laid out as a column on portrait phones),
**[Jellyfin Enhanced](https://github.com/n00bcodr/Jellyfin-Enhanced)** (drawer
entries and Seerr link matched to their neighbours), and
**InPlayerEpisodePreview** (its hairline SVG replaced with a Material glyph).

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
- **The TV layout is untested** — I have no TV client to check it on. It should
  degrade to plain ElegantFin rather than break, since the layout-specific rules
  are scoped to `.layout-desktop` and `.layout-mobile`, but nobody has looked.
  Reports welcome ([#1](https://github.com/mihaif7/elegantfin-jf12/issues/1)).
- ElegantFin **v26.09.05** or later.
- Safe to leave installed on Legacy — everything structural is scoped with
  `:has(.MuiAppBar-root)`, which only matches the Modern layout.
- Non-dark colour schemes fall back to ElegantFin's dark tokens, as they do
  upstream.

If content sits far down the page under a large gap, or buttons come out
indigo, this sheet isn't loading last. Check the import order.

## Credits

[ElegantFin](https://github.com/lscambo13/ElegantFin) by
[lscambo13](https://github.com/lscambo13) — the theme this extends; if you like
how your server looks, that's their work. Its maintainer has
[declined to support the Modern UI for now](https://github.com/lscambo13/ElegantFin/issues/309#issuecomment-5600787192),
which is why this is a companion sheet rather than a fork.

[GPL-2.0](LICENSE), matching upstream.
