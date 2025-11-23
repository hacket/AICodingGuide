---
name: obsidian-wikilinks-converter
description: Convert Obsidian WikiLinks ([[...]]) to standard Markdown links ([...](...)) for GitHub compatibility. This skill should be used when users need to make README files or other Markdown documents GitHub-compatible while maintaining Obsidian functionality, or when batch converting WikiLinks across multiple files.
license: MIT
---

# Obsidian WikiLinks Converter

This skill provides tools and workflows for converting Obsidian WikiLinks (`[[...]]`) to standard Markdown links (`[...](...)`) to ensure GitHub compatibility.

## When to Use This Skill

Use this skill when you need to:
- 📄 Make README.md files GitHub-compatible
- 🔗 Convert WikiLinks to standard Markdown in batch
- 🔄 Maintain dual compatibility (Obsidian + GitHub)
- 📝 Prepare Obsidian notes for publishing to platforms that don't support WikiLinks

## Core Concepts

### WikiLink Formats

Obsidian supports several WikiLink patterns:

| WikiLink Format | Standard Markdown | Notes |
|----------------|-------------------|-------|
| `[[file]]` | `[file](file.md)` | Simple file reference |
| `[[path/file]]` | `[file](path/file.md)` | With path |
| `[[file\|Display]]` | `[Display](file.md)` | Custom display text |
| `[[../path/file]]` | `[file](../path/file.md)` | Relative path |

### Conversion Rules

1. **Display Text Priority**:
   - If `|` separator exists: use specified display text
   - Otherwise: use filename (without path and extension)

2. **Path Handling**:
   - Preserve relative paths (`../`, `./`)
   - Add `.md` extension if missing
   - URL-encode spaces: `My File.md` → `My%20File.md`

3. **Special Cases**:
   - `[[README]]` → `[README](README.md)`
   - `[[folder/README]]` → `[README](folder/README.md)`

## Usage

### Quick Start

```bash
# Preview changes without modifying files
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --dry-run

# Convert all README.md files in current directory
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py

# Convert a specific file
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --file path/to/file.md

# Convert all README files in a specific directory
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --root ./06-AI
```

### Common Workflows

#### Workflow 1: Convert All README Files

For maintaining GitHub-compatible documentation:

```bash
# 1. Review what will be changed
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --dry-run

# 2. Apply changes
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py

# 3. Verify in Git
git diff
```

#### Workflow 2: Convert Single File

For preparing a specific document:

```bash
# Convert and review
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py \
  --file Level-6-Best-Practices/README.md
```

#### Workflow 3: Batch Convert by Pattern

For converting all files matching a pattern:

```bash
# Find and convert all README files
find . -name "README.md" -type f | while read file; do
  python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --file "$file"
done
```

## Implementation Details

### Conversion Logic

The converter uses regex pattern matching with the following logic:

```python
# Pattern: [[content]]
pattern = r'\[\[([^\]]+)\]\]'

# Conversion function
def convert(match):
    content = match.group(1)

    # Split by | for display text
    if '|' in content:
        path, display = content.split('|', 1)
    else:
        path = content
        display = path.split('/')[-1]  # Use filename

    # Add .md extension if needed
    if not path.endswith('.md'):
        path = path + '.md'

    # URL encode spaces
    path = path.replace(' ', '%20')

    return f'[{display}]({path})'
```

### Edge Cases Handled

1. **Code Blocks**: WikiLinks inside code blocks are NOT converted
2. **Front Matter**: YAML front matter is preserved
3. **Empty Links**: `[[]]` is skipped
4. **Special Characters**: Properly escaped in URLs
5. **Nested Paths**: Relative and absolute paths preserved

## Best Practices

### 1. Always Use Dry-Run First

```bash
# GOOD: Preview before applying
python3 convert.py --dry-run
python3 convert.py

# BAD: Direct conversion without review
python3 convert.py
```

### 2. Commit Before Conversion

```bash
# Save current state
git add .
git commit -m "Before WikiLinks conversion"

# Apply conversion
python3 convert.py

# Review and commit
git diff
git add .
git commit -m "Convert WikiLinks to standard Markdown"
```

### 3. Test on Sample Files First

```bash
# Test on a single file
cp README.md README.md.backup
python3 convert.py --file README.md
diff README.md README.md.backup
```

### 4. Use Obsidian-Compatible Markdown

Both Obsidian and GitHub support standard Markdown links:

```markdown
# ✅ RECOMMENDED: Works everywhere
[Display Text](path/to/file.md)

# ❌ Obsidian-only: Breaks on GitHub
[[path/to/file|Display Text]]
```

## Limitations

1. **Code Block Detection**: Basic implementation may convert WikiLinks in code blocks
2. **Image Links**: Assumes all WikiLinks are document links (not images)
3. **Section Links**: `[[file#section]]` not fully supported yet
4. **Block References**: `[[file^block]]` not supported

## Future Enhancements

- [ ] Preserve WikiLinks in code blocks/inline code
- [ ] Support image WikiLinks `![[image.png]]`
- [ ] Handle section links `[[file#section]]`
- [ ] Support block references `[[file^block]]`
- [ ] Interactive mode with confirmation prompts
- [ ] Git integration for auto-commit

## Troubleshooting

### Issue: Script Not Found

```bash
# Solution: Run from repository root
cd /path/to/ObsidianVault
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py
```

### Issue: Permission Denied

```bash
# Solution: Make script executable
chmod +x .claude/skills/obsidian-wikilinks-converter/scripts/convert.py
```

### Issue: Unexpected Conversions

```bash
# Solution: Use --dry-run to preview
python3 convert.py --dry-run --file problematic-file.md
```

## References

- [Obsidian Help: Internal Links](https://help.obsidian.md/Linking+notes+and+files/Internal+links)
- [GitHub Markdown Spec](https://github.github.com/gfm/)
- [Markdown Links Best Practices](https://www.markdownguide.org/basic-syntax/#links)

## Script Location

The conversion script is located at:
```
.claude/skills/obsidian-wikilinks-converter/scripts/convert.py
```

Invoke with: `python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --help`
