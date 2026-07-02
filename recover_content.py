import subprocess
import glob
import os

def recover_all():
    files = glob.glob('sub_*.html')
    files = [f for f in files if 'part' not in f and 'old' not in f]
    
    count = 0
    for file in files:
        page_id = file.split('_')[1].split('.')[0]
        
        # Get old content from git
        try:
            result = subprocess.run(['git', 'show', f'fa6fb1a:{file}'], capture_output=True)
            old_html = result.stdout.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Failed to get {file} from git: {e}")
            continue
            
        # Extract the content part from old_html
        start_idx = old_html.find('<h2 id="container_title">')
        if start_idx == -1:
            print(f"Could not find container_title in old {file}")
            continue
        start_idx = old_html.find('</h2>', start_idx) + 5
        
        # Find the end of the content area. Usually before <footer or <!-- }
        end_idx = old_html.find('<!-- Footer -->')
        if end_idx == -1:
            end_idx = old_html.find('<footer')
        
        # Need to trim some closing divs before footer
        # In old layout it was </div> </div> </div> before footer
        # Let's search for "</div>\n\n</div>\n<!-- }" or similar
        search_end = old_html.rfind('</div>\n\n</div>\n</div>\n<!-- }', start_idx, end_idx)
        if search_end == -1:
            search_end = old_html.rfind('</div>\n\n</div>\n<!-- }', start_idx, end_idx)
            
        if search_end == -1:
            # Just take everything up to the first </div>\n<!-- }
            search_end = old_html.find('<!-- }', start_idx)
            if search_end != -1:
                search_end = old_html.rfind('</div>', start_idx, search_end)
        
        if search_end == -1:
            search_end = end_idx # Fallback
            
        old_content = old_html[start_idx:search_end].strip()
        
        # Clean up old_content slightly (remove remaining closing divs that don't match)
        # It's better to just inject it directly, as they are mostly <div class="sub_wrap">...</div>
        
        # Now read current file
        with open(file, 'r', encoding='utf-8') as f:
            curr_html = f.read()
            
        curr_start = curr_html.find('<main class="sub-content content-body">')
        if curr_start == -1:
            print(f"Could not find <main> in {file}")
            continue
        curr_start = curr_html.find('>', curr_start) + 1
        
        curr_end = curr_html.find('</main>', curr_start)
        
        # Rebuild
        page_title = curr_html[curr_start:curr_end].strip()
        # Keep the h2 title from the new template if we want?
        # Actually old_content usually didn't have the H2 title (it was container_title).
        # We can add an H2 title if old_content doesn't have it.
        # Let's extract the h2 page-title from the generic template
        h2_title = ""
        import re
        m = re.search(r'<h2 class="page-title">(.*?)</h2>', curr_html[curr_start:curr_end])
        if m:
            h2_title = f'\n    <h2 class="page-title">{m.group(1)}</h2>\n'
            
        new_main_content = h2_title + "\n    " + old_content + "\n"
        
        final_html = curr_html[:curr_start] + new_main_content + curr_html[curr_end:]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        count += 1
        print(f"Recovered {file}")
        
    print(f"Successfully recovered {count} files.")

if __name__ == "__main__":
    recover_all()
