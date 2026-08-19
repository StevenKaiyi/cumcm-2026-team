"""Convert locally downloaded problem PDFs to untracked Markdown text.

This helper is intentionally local-only. The generated text lives under
documents/_local/, which is excluded from Git because the official website
does not grant redistribution rights for the full problem statements.
"""

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
LOCAL_ROOT = ROOT / "_local"
MARKDOWN_ROOT = LOCAL_ROOT / "markdown"


def convert_pdf(pdf_path: Path, output_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    pages = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append(f"## 第 {index} 页\n\n{text.strip()}\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"# {pdf_path.stem}\n\n"
        "> 本文件由官方 PDF 自动抽取，仅供本地检索；公式、图片和排版请以原 PDF 为准。\n\n"
        + "\n".join(pages),
        encoding="utf-8",
    )


def main() -> None:
    pdfs = [
        path
        for letter in "ABCDE"
        for path in (LOCAL_ROOT / letter).rglob("*.pdf")
    ]
    if not pdfs:
        raise SystemExit(
            "未找到 PDF。请先运行 documents/download-official.ps1。"
        )

    for pdf_path in sorted(pdfs):
        relative = pdf_path.relative_to(LOCAL_ROOT)
        output_path = (MARKDOWN_ROOT / relative).with_suffix(".md")
        convert_pdf(pdf_path, output_path)
        print(f"Converted: {relative}")


if __name__ == "__main__":
    main()
