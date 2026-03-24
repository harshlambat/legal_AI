import json
import os

def extract_text(data):
    texts = []

    act_title = data.get("Act Title", "")

    chapters = data.get("Chapters", {})

    for ch in chapters.values():
        chapter_name = ch.get("Name", "")

        sections = ch.get("Sections", {})

        for sec_key, sec_val in sections.items():
            heading = sec_val.get("heading", "")

            paragraphs = sec_val.get("paragraphs", {})

            full_text = ""

            for p in paragraphs.values():
                if isinstance(p, str):
                    full_text += p + " "

                elif isinstance(p, dict):
                    full_text += p.get("text", "") + " "

                    if "contains" in p:
                        for sub in p["contains"].values():
                            if isinstance(sub, str):
                                full_text += sub + " "
                            elif isinstance(sub, dict):
                                full_text += sub.get("text", "") + " "

            chunk = f"""
Act: {act_title}
Chapter: {chapter_name}
Section: {heading}
Content: {full_text}
"""
            texts.append(chunk.strip())

    return texts


def process_all_json(folder="json_files"):
    all_chunks = []

    files = os.listdir(folder)

    print(f"Processing {len(files)} files...")

    for file in files:
        if file.endswith(".json"):
            try:
                with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    chunks = extract_text(data)
                    all_chunks.extend(chunks)
            except Exception as e:
                print(f"Error in {file}: {e}")

    return all_chunks


if __name__ == "__main__":
    chunks = process_all_json()

    with open("processed_data.txt", "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(c + "\n\n")

    print(f"\n✅ Done. Total chunks: {len(chunks)}")