import json
import re
import sys

def fix_json_file(input_file, output_file):
    """Fix JSON file with unescaped control characters in strings."""
    
    with open(input_file, 'r') as f:
        content = f.read()
    
    print(f"Original file length: {len(content)} chars")
    
    # First, try to parse to see if it's valid
    try:
        data = json.loads(content)
        print("File is already valid JSON!")
        return True
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
    
    # Fix approach: We need to properly escape control characters within strings
    # but not outside strings. This is complex with regex alone.
    # Better approach: parse character by character with a simple state machine
    
    output = []
    in_string = False
    escape_next = False
    line_num = 1
    col_num = 1
    
    for i, ch in enumerate(content):
        if not in_string:
            output.append(ch)
            if ch == '"' and (i == 0 or content[i-1] != '\\'):
                in_string = True
        else:
            # Inside a string
            if escape_next:
                output.append(ch)
                escape_next = False
            elif ch == '\\':
                output.append(ch)
                escape_next = True
            elif ch == '"':
                output.append(ch)
                in_string = False
            elif ch == '\n':
                # Replace newline with escaped newline
                output.append('\\n')
                print(f"Fixed newline at line {line_num}, col {col_num}, position {i}")
            elif ch == '\t':
                # Replace tab with escaped tab
                output.append('\\t')
                print(f"Fixed tab at line {line_num}, col {col_num}, position {i}")
            elif ch == '\r':
                # Replace carriage return with escaped
                output.append('\\r')
                print(f"Fixed carriage return at line {line_num}, col {col_num}, position {i}")
            elif ord(ch) < 32:  # Other control characters
                # Replace with Unicode escape
                output.append(f'\\u{ord(ch):04x}')
                print(f"Fixed control char {ord(ch)} at line {line_num}, col {col_num}, position {i}")
            else:
                output.append(ch)
        
        # Track line/col for error reporting
        if ch == '\n':
            line_num += 1
            col_num = 1
        else:
            col_num += 1
    
    fixed_content = ''.join(output)
    
    # Try to parse the fixed content
    try:
        data = json.loads(fixed_content)
        print(f"Successfully parsed fixed JSON! Found {len(data)} lessons.")
        
        # Write fixed file
        with open(output_file, 'w') as f:
            # Write with proper formatting
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"Fixed JSON written to {output_file}")
        return True
    except json.JSONDecodeError as e:
        print(f"Still invalid JSON after fixing: {e}")
        # Write the fixed content anyway for debugging
        with open(output_file + '.debug', 'w') as f:
            f.write(fixed_content)
        print(f"Debug output written to {output_file}.debug")
        return False

if __name__ == '__main__':
    input_file = 'static/lessons_en.json'
    output_file = 'static/lessons_en_fixed.json'
    
    if fix_json_file(input_file, output_file):
        print("\nSuccess! Now replace the original file:")
        print(f"  mv {output_file} {input_file}")
        
        # Test the fixed file
        print("\nTesting fixed file...")
        with open(input_file, 'r') as f:
            try:
                data = json.load(f)
                print(f"✓ File is valid JSON with {len(data)} lessons")
                print(f"✓ First lesson: {data[0]['title'][:50]}...")
            except Exception as e:
                print(f"✗ Still has error: {e}")
    else:
        print("\nFailed to fix JSON file.")