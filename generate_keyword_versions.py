import re
import shutil
from pathlib import Path


def remove_links(text: str) -> str:
    """Strip markdown links and inline code markers."""
    text = re.sub(r"\[(.*?)\]\([^\)]+\)", r"\1", text)
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
    if "(" in first:
        name_portion = first.split("(", 1)[0].strip()
    else:
        name_portion = first

    if not name_portion or " " in name_portion or name_portion.lower() in {
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

    return_type = ""
    if len(cells) > 1:
        candidate = cells[1].strip()
        if candidate and candidate.lower() not in {
            "type",
            "return type",
            "description",
            "brief description",
        }:
            return_type = candidate

    if return_type:
        return f"- {first} — {return_type}"
    return f"- {first}"


def build_keyword_lines(lines: list[str]) -> list[str]:
    """Create the stripped-down keyword representation of a doc file."""

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

    return collapse_blank_lines(output)


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


def prepare_content(lines: list[str]) -> tuple[list[str], dict[str, list[str]], list[str] | None]:
    preamble, sections = split_sections(lines)
    normalized_sections: dict[str, list[str]] = {}
    for name, content in sections.items():
        normalized_sections[remove_links(name)] = content
    classes_section = normalized_sections.pop("Classes", None)
    return preamble, normalized_sections, classes_section


def write_service_files(
    service_dir: Path,
    preamble: list[str],
    sections: dict[str, list[str]],
    classes_section: list[str] | None,
    desired_sections: list[str],
    collapse: bool,
) -> list[Path]:
    service_dir.mkdir(parents=True, exist_ok=True)
    written_paths: list[Path] = []

    readme_lines = list(preamble)
    if classes_section:
        if readme_lines and readme_lines[-1].strip():
            readme_lines.append("")
        readme_lines.extend(classes_section)

    readme_content = collapse_blank_lines(readme_lines) if collapse else readme_lines
    readme_text = "\n".join(readme_content).strip() if collapse else "\n".join(readme_content).rstrip("\n")
    if readme_text:
        readme_path = service_dir / "README.md"
        readme_path.write_text(readme_text + "\n")
        written_paths.append(readme_path)

    seen = set()
    for name in desired_sections:
        section = sections.get(name)
        if not section:
            continue
        seen.add(name)
        section_lines = collapse_blank_lines(section) if collapse else section
        section_text = "\n".join(section_lines).strip() if collapse else "\n".join(section_lines).rstrip("\n")
        if not section_text:
            continue
        file_path = service_dir / f"{sanitize_filename(name)}.md"
        file_path.write_text(section_text + "\n")
        written_paths.append(file_path)

    for name, section in sections.items():
        if name in seen:
            continue
        section_lines = collapse_blank_lines(section) if collapse else section
        section_text = "\n".join(section_lines).strip() if collapse else "\n".join(section_lines).rstrip("\n")
        if not section_text:
            continue
        file_path = service_dir / f"{sanitize_filename(name)}.md"
        file_path.write_text(section_text + "\n")
        written_paths.append(file_path)

    return written_paths


def convert_file(path: Path, keyword_root: Path, complete_root: Path) -> None:
    lines = path.read_text().splitlines()

    keyword_lines = build_keyword_lines(lines)
    keyword_preamble, keyword_sections, keyword_classes = prepare_content(keyword_lines)

    complete_preamble, complete_sections, complete_classes = prepare_content(lines)

    class_names = extract_class_names(complete_classes) if complete_classes else []
    desired_sections = class_names or list(complete_sections.keys())

    write_service_files(
        keyword_root / path.stem,
        keyword_preamble,
        keyword_sections,
        keyword_classes,
        desired_sections,
        collapse=True,
    )

    write_service_files(
        complete_root / path.stem,
        complete_preamble,
        complete_sections,
        complete_classes,
        desired_sections,
        collapse=False,
    )


def main() -> None:
    keyword_root = Path("keyword-index")
    complete_root = Path("full-reference")

    for root in (keyword_root, complete_root):
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True)

    source_root = Path("source")
    if not source_root.exists():
        raise SystemExit("source directory not found; ensure service docs live in 'source/'")

    for path in sorted(source_root.glob("*.md")):
        if path.name.endswith("-keywords.md"):
            continue
        convert_file(path, keyword_root, complete_root)


if __name__ == "__main__":
    main()
