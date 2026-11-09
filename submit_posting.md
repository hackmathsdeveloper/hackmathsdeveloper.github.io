
# Pre-blog-posting checklist

Apply this checklist before publishing a blog post.

## Writing rule: use direct English

Apply this rule when writing, editing, or combining content. It takes priority over any instruction that encourages exaggeration, promotional language, or unnecessary length.

Preserve the technical content. Remove unnecessary language, not necessary explanations.

### Preserve technical content

- Keep technical details, definitions, derivations, proofs, examples, code, assumptions, limitations, references, and relevant connections.
- Do not shorten an explanation if doing so removes a step needed to understand it.
- When combining sources, remove duplicate explanations without losing distinct information.
- Keep qualifications that affect correctness. Do not turn a conditional result into an absolute claim.
- Do not replace precise technical terms with vague wording merely to simplify the prose. Explain unfamiliar terms when needed.

### Use plain, precise wording

- State the idea directly.
- Use ordinary words unless a technical term is more accurate.
- Prefer concrete descriptions of mechanisms, results, and limitations.
- Use sentences and paragraphs that are easy to follow. Split long sentences when useful, but do not fragment a connected explanation.
- Explain why something matters by describing its actual consequence or use.
- Use descriptive titles and headings.
- Let the technical content establish its significance. Do not add special phrasing to make it sound impressive.

### Remove unnecessary language

Remove:

- Exaggeration and unsupported superlatives.
- Promotional wording and clickbait.
- Dramatic framing, artificial suspense, and rhetorical questions used only as teasers.
- Stock introductions such as “Let us embark on a journey” or “Dive into the fascinating world of.”
- Empty transitions such as “This is where the magic happens.”
- Phrases such as “It is important to note that” when the sentence can state the point directly.
- Repeated claims that a result is interesting, powerful, elegant, remarkable, or profound.
- Conclusions that only repeat earlier summaries without adding useful synthesis.

Do not use words such as “groundbreaking,” “revolutionary,” “game-changing,” or “mind-blowing” as substitutes for explanation.

These are editing guidelines, not a mechanical word blacklist. Keep a word when it has a precise technical meaning or is needed in a quotation.

### Examples

| Avoid | Use |
|-------|-----|
| “Let us dive into the fascinating world of elliptic curves.” | “An elliptic curve is…” |
| “This elegant identity reveals a profound connection between X and Y.” | “This identity relates X to Y.” |
| “The real magic happens when we substitute this expression.” | “Substituting this expression gives…” |
| “It is important to note that this holds only for positive integers.” | “This holds only for positive integers.” |
| “This powerful technique unlocks arbitrary memory access.” | “Under these conditions, this technique allows arbitrary memory access.” |
| “As we have seen throughout this fascinating journey…” | State the conclusion directly, or omit the sentence. |

### Diagrams

Generate SVG diagrams when they help explain memory corruption or another complex concept.

- Place each diagram beside the explanation it supports.
- Label relevant objects, addresses, offsets, variables, states, and transitions.
- Ensure the diagram agrees with the text, equations, and code.
- Explain the relationship the reader should notice.
- Do not add decorative diagrams.

---

## 1. Source material preparation

Read the source material and identify:

- The central theorem, identity, concept, or finding.
- Definitions, assumptions, derivations, proofs, examples, code, and limitations that must be preserved.
- Relevant connections to other topics and opportunities for cross-linking.
- Repetition that can be removed without losing information.
- Exaggerated or unnecessary wording that should be replaced with direct English.
- Concepts that would benefit from an SVG diagram.
- Any companion illustration files whose diagrams should be integrated into the post.
- Markdown formatting that must be removed from math blocks.
- Raw `<` or `>` characters in math that need review or replacement with LaTeX commands.

When combining material, preserve the distinct technical content from every source.

---

## 2. Frontmatter

Every post must have this YAML block at the top:

```yaml
***
title: "..."
date: YYYY-MM-DD
categories:
  - CategoryName
  - Mathematics
tags:
  - tag-one
  - tag-two
share: true
read_time: true
excerpt: "..."
***
```

Rules:

- `date` must be the current date.
- `categories` must include at least one topic category plus `Mathematics`.
- `tags` should be kebab-case, narrowly topical, and contain 4–8 entries.
- `excerpt` must be 2–3 sentences and no more than approximately 300 characters.
- The excerpt must describe the content directly. Do not use promotional claims, teasers, or exaggerated promises.

---

## 3. Title requirements

Use a clear, specific title that identifies the subject and what the post explains.

Rules:

- Name the relevant theorem, concept, technology, or mechanism.
- State the result or relationship when that makes the title more useful.
- Keep the title as short as accuracy allows.
- Do not require a viral-style title.
- Do not promise a revelation or imply secrecy, novelty, or importance without evidence.
- Straightforward titles such as “An Introduction to X” are acceptable when they accurately describe the post.

Examples:

- “Deriving the Hexagon Spiral Formula”
- “How the Gamma Function Extends the Factorial”
- “The Relationship Between Elliptic Curves and Modular Forms”
- “How Type Confusion Causes an Out-of-Bounds Read”

Avoid titles built around phrases such as:

- “The Secret Behind…”
- “The Formula That Changes Everything”
- “The Most Beautiful…”
- “You Won’t Believe…”
- “The Hidden Power of…”

---

## 4. Opening challenge

Immediately after the frontmatter, place a reader challenge in bold:

```markdown
**Challenge to the reader:** [concrete, verifiable task using the post's content]
```

Rules:

- Make the task specific: for example, “Compute X for Y,” not “Explore X.”
- Make it solvable after reading the post.
- Place it before any body text.
- Use direct wording without dramatic framing.
- State any assumptions needed to make the task well-defined.

Include 2–3 additional challenges after relevant explanations or derivations, and one final challenge at the end.

Each challenge should test a distinct idea rather than repeat the same task.

---

## 5. Math rendering rules

Use these conventions wherever the post contains mathematical notation.

| Item | Required format | Avoid |
|------|-----------------|-------|
| Display math | `$$...$$` | `\[...\]`, `\\[...\\]` |
| Inline math | `$...$` | `\(...\)` |
| Content inside math | Valid LaTeX | Markdown headings, separators, emphasis, or links |
| Absolute values | `$\lvert z \rvert < 1$` | Raw `|z|<1` outside math |
| Grouping braces | `{}_2F_1`, `\frac{a}{b}` | Unbalanced braces |

Use alignment environments for multiline equations:

```latex
$$
\begin{aligned}
x &= a + b \\
y &= c + d
\end{aligned}
$$
```

Keep explanations outside math blocks.

For posts without mathematical notation, skip the math-specific checks.

---

## 6. Content structure

Use this structure:

1. Opening challenge.
2. Central identity, theorem, concept, or finding stated upfront.
3. A short explanation of its use, consequence, or relevance.
4. Numbered sections, each covering one main idea.
5. Challenges after relevant derivations or explanations.
6. A reference or comparison table where it helps.
7. An explanation of the mechanism, root cause, connections, or implications.
8. A final challenge that combines ideas from the post.
9. Source code and references, where applicable.

Section headings use:

```markdown
## N. Descriptive Name
```

Writing requirements:

- State the main point before providing background unless the background is necessary to understand it.
- Present reasoning in an order the reader can follow.
- Explain intermediate steps when they are needed.
- Use specific headings such as “Deriving the Recurrence” rather than “The Hidden Connection.”
- Do not add a generic “deeper significance” section merely to make the post sound important.
- Discuss significance through concrete relationships, applications, consequences, or limitations.
- Use tables for structured comparisons, not as substitutes for explanations that require connected reasoning.
- Integrate useful SVG diagrams into the relevant sections.

---

## 7. Visual separators

Use `---` between major sections.

Place each separator on its own line, outside math blocks.

---

## 8. Pre-publish verification

### 8a. Technical completeness

Compare the draft with the source material.

Confirm that:

- Definitions and assumptions are preserved.
- Derivations and proofs retain the steps needed to follow them.
- Code, examples, limitations, and references are preserved.
- Combining sources has not removed distinct technical information.
- Diagrams agree with the text, equations, and code.
- Challenges are well-defined and solvable from the material presented.

### 8b. Language review

Review the title, excerpt, headings, body, challenges, diagram labels, and conclusion.

Confirm that:

- Simple ideas are expressed simply.
- Technical terms are used accurately and explained where needed.
- Exaggeration, filler, and decorative phrasing have been removed.
- Claims of importance are supported by a specific explanation.
- Transitions explain the relationship between ideas rather than add empty commentary.
- Repeated summaries have been removed unless they serve a clear purpose.
- Necessary qualifications remain intact.
- The edit reduces unnecessary wording without reducing technical content.

### 8c. Rendering checks

Run these commands from the repository root, replacing the filename:

```bash
# 1. Find old-style math delimiters.
# Review any matches in mathematical content.
grep -n '\\\\\[\|\\\\\]\|\\(' _posts/NEW-FILE.md

# 2. Find possible headings or separators that need review.
grep -n '^=\|^--' _posts/NEW-FILE.md

# 3. Find angle brackets that need review.
grep -n '<\|>' _posts/NEW-FILE.md
```

Treat these commands as screening checks. Review matches in context.

Legitimate matches may include:

- Frontmatter `---` delimiters.
- Section separators outside math blocks.
- HTML tags such as `</script>`.
- Code syntax.
- Mathematical comparisons written correctly inside math delimiters.

Confirm that no Markdown headings or separators appear inside `$$...$$` blocks.

Check for pipes inside inline math:

```bash
grep -n '\$.*|.*\$' _posts/NEW-FILE.md
```

Replace absolute-value pipes inside inline math with `\lvert` and `\rvert`.

Also run the escaping checks in section 12c.

---

## 9. Git workflow

```bash
# Stage the new post.
git add _posts/NEW-FILE.md

# Commit with a message that summarizes the content.
git commit -m "Add [topic] blog post

[One line describing the core content]

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"

# Push to deploy.
git push
```

Never amend commits. Create a new commit for each correction. Never skip hooks.

---

## 10. Post-publish verification

After pushing, allow approximately two minutes for the build, then check its status and the live site.

1. Visit the live URL:
   `https://hackmathsdeveloper.github.io/category/mathematics/post-slug/`
2. Confirm that display equations render as math rather than raw LaTeX.
3. Confirm that inline math renders correctly.
4. Confirm that SVG diagrams appear and their labels are readable.
5. Check the title, excerpt, tags, and read time on the listing page.
6. Confirm that the homepage lists the new post:
   `https://hackmathsdeveloper.github.io/`
7. Read the rendered introduction and at least one technical section to catch wording or formatting problems missed in the source.

If math appears as raw LaTeX:

- Check for incorrect delimiters.
- Re-run the checks in sections 8 and 12.
- Inspect the generated HTML and math-rendering configuration if the source checks do not explain the problem.
- Correct the issue, create a new commit, and push again.

---

## 11. Homepage and build verification

### 11a. Confirm that new posts appear

Visit:

```text
[https://hackmathsdeveloper.github.io/](https://hackmathsdeveloper.github.io/)
```

If posts are missing or the homepage is incorrect, check:

| Symptom | Item to check | Action |
|---------|---------------|--------|
| New posts are missing | Post dates relative to build time | If future-dated posts should be published immediately, enable `future: true` |
| Homepage uses the wrong layout | Root index files and their frontmatter | Confirm that the intended `index.html` is tracked |
| Pagination is missing or incomplete | `index.html`, pagination configuration, and conflicting index files | Confirm the required pagination settings and remove unintended conflicts |
| Content is stale | Build and deployment workflow results | Confirm that a deployment completed and inspect the live site |

### 11b. Verify index files

This site's expected homepage file is `index.html`.

Run:

```bash
git ls-files index.html index.md
git status -- index.html index.md
```

Expected state:

- `index.html` is tracked.
- `index.md` is not tracked.

Review any conflicting or untracked index file before changing it.

### 11c. Check future-post configuration

Run:

```bash
grep 'future:' _config.yml
```

If the site should include future-dated posts, the configuration must contain:

```yaml
future: true
```

Add it under the site settings if required.

Do not confuse publishing a future-dated post immediately with scheduling it to appear later.

### 11d. Check deployment workflows

Check both workflows:

- `.github/workflows/jekyll.yml`
- `.github/workflows/jekyll-gh-pages.yml`

Workflow page:

```text
[https://github.com/hackmathsdeveloper/hackmathsdeveloper.github.io/actions](https://github.com/hackmathsdeveloper/hackmathsdeveloper.github.io/actions)
```

The checklist assumes both workflows trigger on pushes to `main`. Verify their current configuration when diagnosing a deployment problem.

At least one relevant deployment must complete successfully, and the live site must show the expected content.

If one workflow is cancelled but the other succeeds, verify the live site before taking further action.

If both fail or are cancelled:

1. Inspect the workflow logs.
2. Correct any identified problem.
3. Re-run the appropriate workflow.

If a new push is needed to trigger the build:

```bash
git commit --allow-empty -m "Re-trigger build"
git push
```

### 11e. Verify individual post pages

Check 2–3 new post URLs, or all of them if fewer than three were published:

```bash
curl -sI [https://hackmathsdeveloper.github.io/category/mathematics/post-slug/](https://hackmathsdeveloper.github.io/category/mathematics/post-slug/) | head -3
```

Confirm HTTP 200.

For a 404, check:

- Whether the post was included in the build.
- Whether its date caused it to be excluded.
- Whether the URL matches the site's permalink configuration.
- Whether the deployment completed.

### 11f. Homepage layout

The expected `index.html` frontmatter is:

```yaml
***
layout: home
show_excerpts: true
paginate: true
entries_layout: grid
***
```

The intended grid has three columns. Use `entries_layout: list` for a single-column layout.

The grid configuration is in `_includes/head-custom.html`.

If the grid layout is incorrect, inspect:

- The `.entries-grid` CSS override.
- The `.layout--home.page--wide .page-wrapper` width setting.
- The expected width of 1400px.

---

## 12. kramdown escaping in math

Apply this section to posts containing mathematical notation.

The inline-math precautions below address Markdown processing before the LaTeX reaches MathJax. Check the rendered output as well as the source.

### 12a. Hash signs and visible braces

The existing rendering setup can strip backslashes from Markdown escape sequences inside inline `$...$` math.

Use letter-based LaTeX commands where possible:

| Intended notation | Avoid in inline math | Use |
|-------------------|----------------------|-----|
| Left set brace | `\{` | `\lbrace` |
| Right set brace | `\}` | `\rbrace` |
| Cardinality | `\#` | `\lvert ... \rvert` or an equivalent explicit notation |

Example:

```markdown
$\lvert\lbrace i : b_i = 1\rbrace\rvert$
```

If `\#` reaches MathJax as a bare `#`, it can produce a “macro parameter character # in math mode” error.

If `\{` or `\}` loses its backslash, the brace becomes a grouping character rather than a visible set delimiter.

Ordinary grouping braces remain valid:

```latex
\frac{a}{b}
{}_2F_1
```

### 12b. Row breaks in inline matrices

In the existing setup, Markdown processing can reduce `\\` inside inline math to a single backslash. MathJax then receives a control space rather than a matrix row break.

For an inline matrix, double the row-break backslashes:

```markdown
<!-- Avoid: the row break may be lost. -->
$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$

<!-- Inline form with doubled backslashes. -->
$\begin{pmatrix} a & b \\\\ c & d \end{pmatrix}$
```

Do not apply this doubling to display math.

Prefer display math for matrices with multiple rows.

### 12c. Additional source checks

Run:

```bash
# 4. Find possible inline pmatrix row-break issues.
grep -n '\$.*\\\\begin{pmatrix}.*[^\\]\\\\[^\\].*\\\\end{pmatrix}' _posts/NEW-FILE.md

# 5. Find escaped Markdown special characters in possible inline math.
grep -n '\$.*\\[#{}]' _posts/NEW-FILE.md
```

Review matches manually:

- Distinguish inline `$...$` from display `$$...$$`.
- Inspect other matrix environments, including `bmatrix`; the first command checks only the displayed `pmatrix` pattern.
- Replace problematic inline `\#`, `\{`, and `\}` notation with suitable letter-based commands.
- Do not change valid display-math syntax merely because a screening command matched it.

These commands help locate possible issues; they do not replace checking the rendered equations.

### 12d. Decision guide

For display math, `$$...$$`:

- Write LaTeX normally.
- Use `\\` for matrix row breaks.
- Keep Markdown formatting outside the block.

For inline math, `$...$`:

- Prefer display math for matrices.
- If an inline matrix is necessary, use the escaping convention in section 12b.
- Replace visible `\{` and `\}` with `\lbrace` and `\rbrace`.
- Rewrite cardinality notation that uses `\#`.
- Replace absolute-value pipes with `\lvert` and `\rvert`.
- Check the rendered result.

### 12e. Pipes in inline math

Pipe characters can interfere with Markdown table parsing.

Avoid:

```markdown
The set $\lbrace z : |z| \ge 1\rbrace$ is a fundamental domain.
```

Use:

```markdown
The set $\lbrace z : \lvert z\rvert \ge 1\rbrace$ is a fundamental domain.
```

This is especially important when the line also contains table separators.

If an equation is split across HTML table cells, inspect the source for pipes inside inline math.

### 12f. Prefer display math for matrices

Use display math when a matrix has multiple rows or is difficult to read inline:

```markdown
The matrix

$$
M = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

has ...
```

Display math avoids the inline row-break escaping problem and gives the matrix enough space.

---

## Quick reference

### Content and language

- [ ] Technical content preserved.
- [ ] Definitions, assumptions, derivations, proofs, examples, code, limitations, and references retained.
- [ ] Direct English used throughout.
- [ ] Exaggeration, filler, promotional wording, and decorative phrasing removed.
- [ ] Title and headings describe the actual content.
- [ ] Excerpt summarizes the post without teasers.
- [ ] Claims of significance explained through specific consequences or uses.
- [ ] No unnecessary repetition.
- [ ] SVG diagrams included where they clarify complex concepts.
- [ ] Diagrams agree with the text, equations, and code.

### Structure

- [ ] Frontmatter complete.
- [ ] Opening challenge is concrete and well-defined.
- [ ] Central result or concept stated near the beginning.
- [ ] Sections follow a clear reasoning order.
- [ ] 2–3 additional challenges test distinct ideas.
- [ ] Final challenge combines ideas from the post.
- [ ] References and source-code links included where applicable.

### Math and rendering

- [ ] Display math uses `$$...$$`.
- [ ] Inline math uses `$...$`.
- [ ] No Markdown headings or separators inside math blocks.
- [ ] Angle brackets reviewed in context.
- [ ] Inline visible braces use `\lbrace` and `\rbrace`.
- [ ] Inline cardinality notation avoids problematic `\#`.
- [ ] Inline absolute values use `\lvert` and `\rvert`.
- [ ] Inline matrix row breaks checked.
- [ ] Display math preferred for multiline matrices.
- [ ] Screening commands run and matches reviewed.
- [ ] Equations and SVG diagrams checked on the rendered page.

### Publication

- [ ] Changes committed and pushed.
- [ ] Deployment workflow completed successfully.
- [ ] Live post URLs return HTTP 200.
- [ ] Homepage lists the new posts.
- [ ] Future-date behavior matches the intended publication behavior.
- [ ] `index.html` is tracked and unintended index-file conflicts are absent.
- [ ] Listing metadata and homepage layout checked.
