# Obsidian WikiLinks Converter Skill

Convert Obsidian WikiLinks (`[[...]]`) to standard Markdown links (`[...](...)`) for GitHub compatibility.

## Quick Start

```bash
# Change to Obsidian Vault root
cd /Users/10069683/Documents/ObsidianVault

# Preview changes (recommended first step)
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --dry-run

# Apply conversions
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py

# Convert specific file
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py \
  --file Level-6-Best-Practices/README.md
```

## Common Use Cases

### 1. Convert All README Files

```bash
# Preview
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py --dry-run

# Apply
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py
```

### 2. Convert Files in Specific Directory

```bash
# Only convert README files under 06-AI/
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py \
  --root 06-AI/04-AIAgentic/Claude-Code
```

### 3. Verbose Output

```bash
# See detailed conversion information
python3 .claude/skills/obsidian-wikilinks-converter/scripts/convert.py \
  --verbose --dry-run
```

## Conversion Examples

| WikiLink | Standard Markdown |
|----------|-------------------|
| `[[file]]` | `[file](file.md)` |
| `[[path/file]]` | `[file](path/file.md)` |
| `[[file\|Display]]` | `[Display](file.md)` |
| `[[../path/file]]` | `[file](../path/file.md)` |
| `[[My File]]` | `[My File](My%20File.md)` |

## Features

- ✅ Converts WikiLinks to standard Markdown
- ✅ Preserves relative paths
- ✅ Handles custom display text (`|` separator)
- ✅ URL-encodes spaces for GitHub
- ✅ Skips WikiLinks in code blocks
- ✅ Dry-run mode for safe preview
- ✅ Batch processing support
- ✅ Verbose logging

## Options

```
--dry-run          Preview changes without modifying files
--file FILE        Convert specific file
--root DIR         Root directory to search (default: .)
--pattern PATTERN  Filename pattern (default: README.md)
--verbose, -v      Show detailed conversion info
```

## Best Practices

1. **Always preview first**: Use `--dry-run` before applying changes
2. **Commit before converting**: Save your work in Git first
3. **Test on sample file**: Try converting a single file first
4. **Review changes**: Use `git diff` to verify conversions

## Skill Activation

To use this skill with Claude Code, simply mention:

```
"Use the obsidian-wikilinks-converter skill to convert WikiLinks in README files"
```

Or invoke directly:

```
Use obsidian-wikilinks-converter skill
```

## Documentation

Full documentation available in: `skill.md`

## License

MIT
