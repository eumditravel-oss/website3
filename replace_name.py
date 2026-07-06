import os
import glob

def replace_text_in_files(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.py')) and file != 'replace_name.py':
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if old_text in content:
                        new_content = content.replace(old_text, new_text)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    replace_text_in_files('f:/website3', '신영에스씨엠', '한강엔지니어링')
    print("Done replacing company name.")
