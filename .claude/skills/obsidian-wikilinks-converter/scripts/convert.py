#!/usr/bin/env python3
"""
Obsidian WikiLinks to Standard Markdown Converter

Converts Obsidian WikiLinks [[...]] to standard Markdown links [...](...)
for GitHub compatibility while maintaining Obsidian functionality.

Author: Claude Code Skill
License: MIT
"""

import re
import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple


class WikiLinkConverter:
    """Handles conversion of Obsidian WikiLinks to standard Markdown."""

    # Pattern to match WikiLinks: [[content]]
    WIKILINK_PATTERN = re.compile(r'\[\[([^\]]+)\]\]')

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.stats = {'files': 0, 'conversions': 0, 'skipped': 0}

    def convert_wikilink(self, match: re.Match) -> str:
        """
        Convert a single WikiLink to Markdown link.

        Args:
            match: Regex match object containing the WikiLink content

        Returns:
            Converted Markdown link string
        """
        content = match.group(1)

        # Handle display text: [[path/file|Display Text]]
        if '|' in content:
            path, display = content.split('|', 1)
            display = display.strip()
        else:
            path = content
            # Extract filename for display (remove path and extension)
            display = path.split('/')[-1].replace('.md', '')

        # Normalize path
        path = path.strip()

        # Add .md extension if not present
        if not path.endswith('.md'):
            # Special handling for README
            if path.endswith('README'):
                path = path + '.md'
            else:
                path = path + '.md'

        # URL encode spaces for GitHub compatibility
        path = path.replace(' ', '%20')

        return f'[{display}]({path})'

    def is_in_code_block(self, text: str, position: int) -> bool:
        """
        Check if a position in text is inside a code block.

        Args:
            text: Full text content
            position: Character position to check

        Returns:
            True if position is inside a code block
        """
        # Count code fence markers before position
        text_before = text[:position]

        # Check for inline code
        inline_code_count = text_before.count('`')
        if inline_code_count % 2 == 1:  # Odd count means inside inline code
            return True

        # Check for code blocks (```)
        code_blocks = text_before.count('```')
        if code_blocks % 2 == 1:  # Odd count means inside code block
            return True

        # Check for indented code blocks (4 spaces at line start)
        lines = text_before.split('\n')
        if lines and lines[-1].startswith('    '):
            return True

        return False

    def convert_content(self, content: str) -> Tuple[str, int]:
        """
        Convert all WikiLinks in content to Markdown links.

        Args:
            content: Markdown content to convert

        Returns:
            Tuple of (converted_content, conversion_count)
        """
        conversions = 0
        result = []
        last_end = 0

        for match in self.WIKILINK_PATTERN.finditer(content):
            start, end = match.span()

            # Check if WikiLink is in code block
            if self.is_in_code_block(content, start):
                if self.verbose:
                    print(f"    ⊘ Skipping WikiLink in code block: {match.group(0)}")
                self.stats['skipped'] += 1
                continue

            # Add text before match
            result.append(content[last_end:start])

            # Convert WikiLink
            converted = self.convert_wikilink(match)
            result.append(converted)

            if self.verbose:
                print(f"    ✓ {match.group(0)} → {converted}")

            conversions += 1
            last_end = end

        # Add remaining text
        result.append(content[last_end:])

        return ''.join(result), conversions

    def convert_file(self, file_path: str, dry_run: bool = False) -> int:
        """
        Convert WikiLinks in a single file.

        Args:
            file_path: Path to file to convert
            dry_run: If True, only show what would change

        Returns:
            Number of conversions made
        """
        print(f"\n{'[DRY RUN] ' if dry_run else ''}📄 Processing: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception as e:
            print(f"  ❌ Error reading file: {e}")
            return 0

        converted_content, conversions = self.convert_content(original_content)

        if conversions == 0:
            print("  ✓ No WikiLinks found")
            return 0

        print(f"  ✓ Found {conversions} WikiLink(s) to convert")

        if self.stats['skipped'] > 0:
            print(f"  ⊘ Skipped {self.stats['skipped']} WikiLink(s) in code blocks")

        if not dry_run:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
                print(f"  ✅ Converted successfully")
            except Exception as e:
                print(f"  ❌ Error writing file: {e}")
                return 0

        self.stats['files'] += 1
        self.stats['conversions'] += conversions

        return conversions

    def find_readme_files(self, root_dir: str, pattern: str = "README.md") -> List[str]:
        """
        Find all README.md files recursively.

        Args:
            root_dir: Root directory to search
            pattern: Filename pattern to match

        Returns:
            List of file paths
        """
        readme_files = []

        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip hidden directories
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]

            for filename in filenames:
                if filename == pattern:
                    readme_files.append(os.path.join(dirpath, filename))

        return sorted(readme_files)

    def print_summary(self, dry_run: bool = False):
        """Print conversion summary statistics."""
        print(f"\n{'=' * 70}")
        print(f"{'[DRY RUN] ' if dry_run else ''}Summary:")
        print(f"  📁 Files processed: {self.stats['files']}")
        print(f"  🔗 WikiLinks converted: {self.stats['conversions']}")
        if self.stats['skipped'] > 0:
            print(f"  ⊘ WikiLinks skipped (in code): {self.stats['skipped']}")

        if dry_run:
            print(f"\n💡 Run without --dry-run to apply changes")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Obsidian WikiLinks to standard Markdown links.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview changes without modifying files
  python3 convert.py --dry-run

  # Convert all README.md files
  python3 convert.py

  # Convert a specific file
  python3 convert.py --file path/to/file.md

  # Convert all README files in a directory
  python3 convert.py --root ./06-AI

  # Verbose output
  python3 convert.py --verbose --dry-run
        """
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Convert a specific file instead of all README.md files'
    )
    parser.add_argument(
        '--root',
        type=str,
        default='.',
        help='Root directory to search for README files (default: current directory)'
    )
    parser.add_argument(
        '--pattern',
        type=str,
        default='README.md',
        help='Filename pattern to match (default: README.md)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed conversion information'
    )

    args = parser.parse_args()

    # Initialize converter
    converter = WikiLinkConverter(verbose=args.verbose)

    if args.file:
        # Convert single file
        if not os.path.exists(args.file):
            print(f"❌ Error: File not found: {args.file}")
            return 1

        converter.convert_file(args.file, args.dry_run)
    else:
        # Convert all README files
        readme_files = converter.find_readme_files(args.root, args.pattern)

        if not readme_files:
            print(f"❌ No {args.pattern} files found in {args.root}")
            return 1

        print(f"🔍 Found {len(readme_files)} {args.pattern} file(s):")
        for f in readme_files:
            print(f"  • {f}")

        for readme in readme_files:
            converter.convert_file(readme, args.dry_run)

    # Print summary
    converter.print_summary(args.dry_run)

    return 0


if __name__ == '__main__':
    sys.exit(main())
