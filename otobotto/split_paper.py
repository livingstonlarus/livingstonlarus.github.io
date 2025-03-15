import re
import os

def split_markdown(input_file, output_dir):
    """
    Splits a Markdown file into multiple files based on sections.

    Args:
        input_file: Path to the input Markdown file.
        output_dir: Directory to save the split files.
    """

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define sections (including Abstract and References)
    sections = [
        "Abstract",
        "1. Introduction",
        "2. Background and Motivation",
        "3. Evolving AI Capabilities and Global Competition",
        "4. Architecture Overview",
        "5. Technical Implementation Considerations",
        "6. Human-in-the-Loop and Progressive Autonomy",
        "7. Preliminary Evaluation and Future Considerations",
        "8. Discussion",
        "9. Future Work",
        "10. Conclusion",
        "References"
    ]

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    start = 0

    for i, section_title in enumerate(sections):
      # Find Section Start
      if section_title == "Abstract":
        section_start_pattern = r"^## Abstract$"
      elif section_title == "References":
        section_start_pattern = r"^## References$"
      else:
        section_start_pattern = r"^## " + re.escape(section_title) + r"$"
      
      match_start = re.search(section_start_pattern, content, re.MULTILINE)
      
      if match_start:
        start = match_start.start()
      else:
        print(f"Not found: {section_title}")
        continue # Or raise exception

      # Find Section End
      if i < len(sections) - 1:
          next_section_title = sections[i+1]
          if next_section_title == "Abstract":
            section_end_pattern = r"^## Abstract$"
          elif next_section_title == "References":
            section_end_pattern = r"^## References$"
          else:
            section_end_pattern = r"^## " + re.escape(next_section_title) + r"$"
          match_end = re.search(section_end_pattern, content[start:], re.MULTILINE)

          if match_end:
              end = start + match_end.start()
          else:
              print("Error: Could not find the end of section: " + section_title)
              end = -1
      else:
          end = len(content)

      if end != -1:
        section_content = content[start:end]

        # Construct output filename
        if section_title == "Abstract":
          output_filename = "abstract.md"
        elif section_title == "References":
          output_filename = "references.md"
        else:
          output_filename = section_title.lower().replace(' ', '-') + ".md"
          output_filename = output_filename.replace('.', '')

        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(section_content)
        print(f"Section '{section_title}' written to '{output_path}'")

if __name__ == "__main__":
    input_file = "otobotto/otobotto-paper-draft.md"
    output_dir = "otobotto/paper"
    split_markdown(input_file, output_dir)