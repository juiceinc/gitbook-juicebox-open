#!/usr/bin/env python3
"""
Migrate changelog.md to use GitBook update blocks for RSS feed generation.

This script:
1. Reads changelog.md
2. Identifies the prefix (everything before the first dated entry)
3. Wraps each dated entry in {% update date="YYYY-MM-DD" %} blocks
4. Wraps all entries in a single {% updates format="full" %} block
5. Preserves all content exactly as-is
"""

import re
import sys
from pathlib import Path
from dateutil import parser as date_parser


def parse_date_heading(heading_text: str) -> tuple[str, str | None]:
    """
    Parse a date from a heading like "May 8, 2026" or "Mar 27, 2025".

    Returns:
        (original_heading, iso_date) where iso_date is YYYY-MM-DD or None if parsing fails
    """
    try:
        parsed = date_parser.parse(heading_text)
        return heading_text, parsed.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return heading_text, None


def is_date_heading(line: str) -> tuple[bool, str]:
    """
    Check if a line is a dated H2 heading (## Month Day, Year).

    Returns:
        (is_dated, heading_text) where heading_text is the text after ##
    """
    match = re.match(r'^## (.+)$', line)
    if not match:
        return False, ""

    heading_text = match.group(1).strip()

    # Try to parse as a date - this is more reliable than regex for various formats
    _, iso_date = parse_date_heading(heading_text)
    return iso_date is not None, heading_text


def find_first_dated_entry(lines: list[str]) -> int:
    """Find the line index of the first dated H2 heading."""
    for i, line in enumerate(lines):
        is_dated, _ = is_date_heading(line)
        if is_dated:
            return i
    return -1


def extract_entries(lines: list[str], start_idx: int) -> list[dict]:
    """
    Extract all dated entries starting from start_idx.

    Returns list of dicts with:
        - heading: original heading text
        - iso_date: YYYY-MM-DD date string (or None if parsing failed)
        - content: list of lines (including the heading line)
    """
    entries = []
    current_entry = None

    for i in range(start_idx, len(lines)):
        line = lines[i]
        is_dated, heading_text = is_date_heading(line)

        if is_dated:
            # Save previous entry if exists
            if current_entry is not None:
                entries.append(current_entry)

            # Start new entry
            _, iso_date = parse_date_heading(heading_text)
            current_entry = {
                'heading': heading_text,
                'iso_date': iso_date,
                'content': [line]
            }
        elif line.startswith('## '):
            # Non-dated H2 heading - this is a warning case
            if current_entry is not None:
                entries.append(current_entry)

            # Treat as entry with failed date parsing
            current_entry = {
                'heading': line[3:].strip(),
                'iso_date': None,
                'content': [line]
            }
        else:
            # Regular content line
            if current_entry is not None:
                current_entry['content'].append(line)

    # Don't forget the last entry
    if current_entry is not None:
        entries.append(current_entry)

    return entries


def migrate_changelog(input_path: str, output_path: str | None = None) -> dict:
    """
    Migrate changelog to use GitBook update blocks.

    Args:
        input_path: Path to input changelog.md
        output_path: Path for output (defaults to overwriting input)

    Returns:
        Summary dict with stats about the migration
    """
    if output_path is None:
        output_path = input_path

    # Read the file
    content = Path(input_path).read_text(encoding='utf-8')
    lines = content.split('\n')

    # Find where dated entries begin
    first_dated_idx = find_first_dated_entry(lines)

    if first_dated_idx == -1:
        raise ValueError("No dated entries found in changelog")

    # Split into prefix and entries
    prefix_lines = lines[:first_dated_idx]
    entries = extract_entries(lines, first_dated_idx)

    # Track stats
    total_entries = len(entries)
    failed_parses = []
    dates = []

    # Build the output
    output_lines = []

    # Add prefix (unchanged)
    output_lines.extend(prefix_lines)

    # Start the updates block
    output_lines.append('{% updates format="full" %}')
    output_lines.append('')

    # Add each entry wrapped in update blocks
    for entry in entries:
        if entry['iso_date'] is None:
            failed_parses.append(entry['heading'])
            # Still wrap it, but with a placeholder date
            output_lines.append('{% update date="PARSE-FAILED" %}')
        else:
            dates.append(entry['iso_date'])
            output_lines.append('{' + '% update date="' + entry['iso_date'] + '" %' + '}')

        # Add the content (heading + body)
        output_lines.extend(entry['content'])

        # Ensure there's a blank line before endupdate if content doesn't end with one
        if entry['content'] and entry['content'][-1].strip() != '':
            output_lines.append('')

        output_lines.append('{% endupdate %}')
        output_lines.append('')

    # Close the updates block
    output_lines.append('{% endupdates %}')

    # Write output
    Path(output_path).write_text('\n'.join(output_lines), encoding='utf-8')

    # Compute stats
    if dates:
        dates_sorted = sorted(dates)
        oldest = dates_sorted[0]
        newest = dates_sorted[-1]
    else:
        oldest = newest = None

    return {
        'total_entries': total_entries,
        'successful_parses': total_entries - len(failed_parses),
        'failed_parses': failed_parses,
        'oldest_date': oldest,
        'newest_date': newest,
    }


def main():
    input_file = 'changelog.md'

    if not Path(input_file).exists():
        print(f"ERROR: {input_file} not found in current directory")
        sys.exit(1)

    print(f"Migrating {input_file} to GitBook update blocks...")
    print()

    try:
        stats = migrate_changelog(input_file)
    except Exception as e:
        print(f"ERROR: Migration failed: {e}")
        sys.exit(1)

    # Print summary
    print("=" * 60)
    print("MIGRATION SUMMARY")
    print("=" * 60)
    print(f"Total entries processed: {stats['total_entries']}")
    print(f"Successfully parsed:     {stats['successful_parses']}")
    print(f"Oldest date:             {stats['oldest_date']}")
    print(f"Newest date:             {stats['newest_date']}")
    print()

    if stats['failed_parses']:
        print("!" * 60)
        print("WARNING: The following headings FAILED date parsing:")
        print("!" * 60)
        for heading in stats['failed_parses']:
            print(f"  - ## {heading}")
        print()
        print("These entries were wrapped with date=\"PARSE-FAILED\"")
        print("Please fix these manually!")
        print("!" * 60)
    else:
        print("All date headings parsed successfully.")

    print()
    print(f"Migration complete. {input_file} has been updated.")


if __name__ == '__main__':
    main()
