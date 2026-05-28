# MathJax Rendering Fix

## Problem

Mathematical symbols (`$...$` and `$$...$$` LaTeX) were not rendered on blog pages despite `mathjax.enable: true` in `_config.yml`.

## Root Cause

The MathJax 3 configuration in `_includes/scripts.html` overrode the `find` render action to only look for `<script type="math/tex">` blocks (inserted by kramdown). However, kramdown leaves `$...$` and `$$...$$` delimiters as raw text in the HTML — it does not generate `<script>` tags. Since the custom `find` action replaced MathJax 3's built-in delimiter scanning, `$...$` and `$$...$$` were never discovered and rendered.

## Fix

Removed the custom `find` render action from the MathJax configuration in `_includes/scripts.html`, allowing MathJax 3 to use its default `find` action which handles `$...$`, `$$...$$`, `\(...\)`, `\[...\]`, and `<script>` blocks all at once.

Added explicit `inlineMath` and `displayMath` delimiter configuration for clarity:

```js
MathJax = {
  tex: {
    tags: "ams",
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
}
```

## Scope

This change applies universally to all blog pages via `_includes/scripts.html`, which is included in the default layout.

---

# Rules for writing math in blog posts

Follow these when adding new `_posts/*.md` files. The MathJax 3 config in `_includes/scripts.html` accepts both delimiter styles, but only `$$`/`$` survives Markdown processing reliably.

## Delimiter choice

| Context | Use | Never use |
|---------|-----|-----------|
| Display math (block) | `$$...$$` | `\[...\]` |
| Inline math | `$...$` | `\(...\)` |

**Why:** In Markdown, `\[` is parsed as an escaped literal bracket → renders as `[` in HTML. MathJax never sees a delimiter. Double-escaping `\\[` is fragile and inconsistent. `$$` has no such issue and matches what the existing Riemann zeta post uses.

## No markdown inside math blocks

Do NOT put any of these between `$$...$$` or `$...$`:

- `====` or `---` — markdown headings / horizontal rules
- `*` or `-` at line-start — list markers
- `[text](url)` — markdown links

Everything between math delimiters must be valid LaTeX only.

## HTML-sensitive characters in math

| Character | Fix |
|-----------|-----|
| `<` | Use `\lt` or wrap in `$...$`. E.g. `$\lvert z \rvert < 1$` not `|z|<1` |
| `>` | Use `\gt` |

Raw `<` in HTML is an unescaped tag opener and will break rendering for the rest of the page.

## Curly braces in LaTeX

`{}_2F_1`, `\frac{a}{b}`, `\boxed{x}` etc. work fine inside `$$`/`$`. Jekyll's Liquid only treats `{%` and `{{` as special — bare `{` and `}` are safe.

## Long / multi-line equations

Keep display math on a single line, or use a LaTeX alignment environment:

```
$$
\begin{aligned}
x &= a + b \\
y &= c + d
\end{aligned}
$$
```

## Pre-publish checklist

```bash
# Should print nothing
grep -n '\\\\\[\|\\\\\]\|\\(' _posts/new-post.md

# Check for markdown inside math
grep -n '^=\|^--' _posts/new-post.md
```

No `====` or `---` lines between `$$` delimiters, and no raw `<` or `>` in math mode.
