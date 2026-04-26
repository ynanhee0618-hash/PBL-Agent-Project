import pymupdf4llm
import pathlib

# Convert the PDF
md_text = pymupdf4llm.to_markdown("sample paper.pdf")

# Write to file
pathlib.Path("sample paper.md").write_bytes(md_text.encode('utf-8'))
