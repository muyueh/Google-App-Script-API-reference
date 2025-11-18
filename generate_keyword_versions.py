import re
import shutil
from pathlib import Path


def remove_links(text: str) -> str:
    """Strip markdown links and inline code markers."""
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = text.replace("`", "")
    return text.strip()


def process_table_row(row: str) -> str | None:
    """Return the first cell as a keyword bullet if appropriate."""
    # Ignore separator rows (|---|)
    if set(row.replace("|", "").strip()) <= {"-", ":", " "}:
        return None

    cells = [remove_links(cell.strip()) for cell in row.strip().strip("|").split("|")]
    if not cells:
        return None

    first = cells[0].strip()
    if not first or " " in first or first.lower() in {
        "name",
        "brief description",
        "property",
        "type",
        "method",
        "return type",
    }:
        return None

    # Skip rows that are clearly notes.
    if first.lower().startswith("**note"):
        return None

    open_count = first.count("(")
    close_count = first.count(")")
    while close_count > open_count and first.endswith(")"):
        first = first[:-1]
        close_count -= 1

    return f"- {first}"


def collapse_blank_lines(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    last_blank = False
    for line in lines:
        if line:
            cleaned.append(line)
            last_blank = False
        elif not last_blank:
            cleaned.append("")
            last_blank = True
    return cleaned


def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z_-]+", "_", name).strip("_")
    return cleaned or "section"


def split_sections(lines: list[str]) -> tuple[list[str], dict[str, list[str]]]:
    preamble: list[str] = []
    sections: dict[str, list[str]] = {}
    current_name: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("## "):
            if current_name is not None:
                sections[current_name] = current_lines
            current_name = line[3:].strip()
            current_lines = [line]
        else:
            if current_name is None:
                preamble.append(line)
            else:
                current_lines.append(line)

    if current_name is not None:
        sections[current_name] = current_lines

    return preamble, sections


def extract_class_names(section: list[str]) -> list[str]:
    names: list[str] = []
    for line in section:
        if line.startswith("- "):
            names.append(line[2:].strip())
    return names


def convert_file(path: Path, output_root: Path) -> list[Path]:
    lines = path.read_text().splitlines()
    output: list[str] = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            output.append("")
            continue

        if stripped.startswith("#"):
            output.append(remove_links(stripped))
            continue

        if stripped.startswith("|"):
            bullet = process_table_row(stripped)
            if bullet:
                output.append(bullet)
            continue

    cleaned = collapse_blank_lines(output)
    preamble, sections = split_sections(cleaned)

    service_dir = output_root / path.stem
    service_dir.mkdir(parents=True, exist_ok=True)
    written_paths: list[Path] = []

    classes_section = sections.pop("Classes", None)
    class_names: list[str] = extract_class_names(classes_section) if classes_section else []

    readme_lines = collapse_blank_lines(preamble)
    if classes_section:
        if readme_lines and readme_lines[-1] != "":
            readme_lines.append("")
        readme_lines.extend(collapse_blank_lines(classes_section))

    readme_path = service_dir / "README.md"
    readme_path.write_text("\n".join(readme_lines).strip() + "\n")
    written_paths.append(readme_path)

    desired_sections = class_names or list(sections.keys())
    seen = set()
    for name in desired_sections:
        section = sections.get(name)
        if not section:
            continue
        seen.add(name)
        file_path = service_dir / f"{sanitize_filename(name)}.md"
        file_path.write_text("\n".join(collapse_blank_lines(section)).strip() + "\n")
        written_paths.append(file_path)

    # Include any sections that were not in the classes list.
    for name, section in sections.items():
        if name in seen:
            continue
        file_path = service_dir / f"{sanitize_filename(name)}.md"
        file_path.write_text("\n".join(collapse_blank_lines(section)).strip() + "\n")
        written_paths.append(file_path)

    return written_paths


def main() -> None:
    output_root = Path("keywords")
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    for path in sorted(Path.cwd().glob("*.md")):
        if path.name == "README.md" or path.name.endswith("-keywords.md"):
            continue
        convert_file(path, output_root)


if __name__ == "__main__":
    main()
