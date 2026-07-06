import os
import re

def replace_text_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.py')) and file not in ['replace_name.py', 'update_info.py']:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    
                    # Fix the mobile number missing from the footer
                    # The pattern looks like: <strong>TEL :</strong> 02-6959-0729  |  <strong>FAX :</strong> 02-6959-0730  |  <strong>E-mail :</strong> hangang0730@daum.net
                    # And also: TEL : 02-6959-0729 &nbsp;|&nbsp; FAX : 02-6959-0730 &nbsp;|&nbsp; E-mail : hangang0730@daum.net
                    
                    new_content = re.sub(
                        r'(<strong>FAX\s*:\s*</strong>\s*02-6959-0730\s*(?:&nbsp;| |\||\s)+)(<strong>E-mail)', 
                        r'\1<strong>Mobile :</strong> 010-9700-2926 &nbsp;|&nbsp; \2', 
                        new_content
                    )
                    
                    new_content = re.sub(
                        r'(FAX\s*:\s*02-6959-0730\s*(?:&nbsp;| |\||\s)+)(E-mail)', 
                        r'\1Mobile : 010-9700-2926 &nbsp;|&nbsp; \2', 
                        new_content
                    )
                    
                    # Fix mobile missing in part3_footer.html (sometimes it's a <br>)
                    new_content = re.sub(
                        r'FAX\s*:\s*02-6959-0730\s*<br>',
                        r'FAX : 02-6959-0730 | Mobile : 010-9700-2926<br>',
                        new_content
                    )
                        
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {filepath}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    replace_text_in_files('f:/website3')
    print("Done adding mobile number.")
