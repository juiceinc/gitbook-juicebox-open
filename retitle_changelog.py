#!/usr/bin/env python3
"""
Retitle changelog entries from date-based headings to release numbers.

For each {% update %} block in changelog.md:
- If it contains a (release X.XXX) line, replace the ## <date> heading
  with ## Release X.XXX and remove the (release X.XXX) line
- If no release line exists, leave the block unchanged
"""

import re
import subprocess
import sys
from pathlib import Path


def retitle_changelog(filepath: Path) -> tuple[int, int, int, str]:
    """
    Process the changelog file and retitle entries with release numbers.

    Returns:
        tuple of (total_blocks, retitled_count, skipped_count, first_updated_entry)
    """
    content = filepath.read_text()

    # Pattern to match {% update %} blocks
    update_block_pattern = re.compile(
        r'(\{% update date="[^"]+?" %\})(.*?)(\{% endupdate %\})',
        re.DOTALL
    )

    # Pattern to match release line like (release 4.128)
    release_pattern = re.compile(r'^\(release (\d+\.\d+)\)\s*$', re.MULTILINE)

    # Pattern to match date heading like ## May 8, 2026 or ## Apr 24, 2025
    date_heading_pattern = re.compile(r'^## .+?, \d{4}\s*$', re.MULTILINE)

    total_blocks = 0
    retitled_count = 0
    skipped_count = 0
    first_updated_entry = None

    def process_block(match):
        nonlocal total_blocks, retitled_count, skipped_count, first_updated_entry

        total_blocks += 1
        open_tag = match.group(1)
        block_content = match.group(2)
        close_tag = match.group(3)

        # Check for release line
        release_match = release_pattern.search(block_content)

        if not release_match:
            skipped_count += 1
            return match.group(0)  # Return unchanged

        # Extract release version
        release_version = release_match.group(1)

        # Replace the date heading with release heading
        new_content = date_heading_pattern.sub(f'## Release {release_version}', block_content, count=1)

        # Remove the (release X.XXX) line and blank line after it
        new_content = re.sub(r'\n\(release \d+\.\d+\)\n', '\n', new_content)

        retitled_count += 1

        # Capture first updated entry
        if first_updated_entry is None:
            first_updated_entry = f"{open_tag}{new_content}{close_tag}"

        return f"{open_tag}{new_content}{close_tag}"

    new_content = update_block_pattern.sub(process_block, content)

    # Write the transformed content
    filepath.write_text(new_content)

    return total_blocks, retitled_count, skipped_count, first_updated_entry


def get_untouched_entry_from_2022(filepath: Path) -> str:
    """Find and return one untouched entry from 2022."""
    content = filepath.read_text()

    # Pattern to find a 2022 entry (these should not have release lines)
    pattern = re.compile(
        r'(\{% update date="2022[^"]+?" %\}.*?\{% endupdate %\})',
        re.DOTALL
    )

    match = pattern.search(content)
    return match.group(1) if match else "No 2022 entries found"


def main():
    changelog_path = Path(__file__).parent / 'changelog.md'

    if not changelog_path.exists():
        print(f"Error: {changelog_path} not found")
        sys.exit(1)

    print("Processing changelog.md...")
    print()

    total, retitled, skipped, first_updated = retitle_changelog(changelog_path)

    # Print statistics
    print(f"Total {{% update %}} blocks found: {total}")
    print(f"Number retitled (had a release line): {retitled}")
    print(f"Number skipped (no release line): {skipped}")
    print()

    # Run git diff --stat
    print("git diff --stat changelog.md:")
    print("-" * 40)
    result = subprocess.run(
        ['git', 'diff', '--stat', 'changelog.md'],
        capture_output=True,
        text=True,
        cwd=changelog_path.parent
    )
    print(result.stdout or "(no changes)" if result.returncode == 0 else result.stderr)
    print()

    # Show first updated entry
    print("First updated entry (May 8, 2026 -> Release 4.128):")
    print("=" * 50)
    if first_updated:
        # Truncate for readability
        lines = first_updated.split('\n')
        preview_lines = lines[:15]
        print('\n'.join(preview_lines))
        if len(lines) > 15:
            print(f"... ({len(lines) - 15} more lines)")
    print()

    # Show one untouched 2022 entry
    print("One untouched entry from 2022 (confirming older entries are unchanged):")
    print("=" * 50)
    untouched = get_untouched_entry_from_2022(changelog_path)
    lines = untouched.split('\n')
    preview_lines = lines[:20]
    print('\n'.join(preview_lines))
    if len(lines) > 20:
        print(f"... ({len(lines) - 20} more lines)")


if __name__ == '__main__':
    main()
