"""
This script's purpose is to assemble the files in the `src/` directory
into a json file that can be used in KETSU

- Requires Jsmin@3.0.1

P.S.

Yeah I know it's a javascript project but I don't like JS
"""

import os
import json
import re
import jsmin
from typing import Dict, Any


OUTPUT_FILE_NAME = "soaper-test"
SOURCE_DIRECTORY = "src"
OUTPUT_INDENT_LEVEL = 4


if __name__ == "__main__":
    # this print statement just makes everything look nice
    print("\n\n--- STARTING ASSEMBLE ---\n")

    output_file_path = f"{OUTPUT_FILE_NAME}.json"
    assert os.path.exists(output_file_path)
    print(f"File path exists -> {output_file_path}")

    with open(output_file_path, "r") as output_file_read_mode:
        json_data: Dict[str, Any] = json.load(output_file_read_mode)
        print(f"Got JSON Data from -> {output_file_path}")
    
    print("")

    main_page_path: str = os.path.join(SOURCE_DIRECTORY, "MainPage", "mainPage1.html")
    assert os.path.exists(main_page_path)
    print(f"File path exists -> {main_page_path}")

    with open(main_page_path, "r") as main_page_file:
        main_page_contents: str = main_page_file.read()
        print(f"Read Main Page contents from -> {main_page_path}")

    print("")

    no_script_tag_pattern = r'<script\s+type="text/javascript">\s*|</script>'
    no_script_tag_main_page: str = re.sub(no_script_tag_pattern, '', main_page_contents)
    print("Removed Script Tags from Main Page")

    minified_javscript_code: str = jsmin.jsmin(no_script_tag_main_page) 
    print("Minified Javscript source code")

    print("")

    json_data["mainPage"][0]["javascriptConfig"]["javaScript"] = minified_javscript_code

    with open(output_file_path, "w") as output_file_write_mode:
        json.dump(json_data, output_file_write_mode, indent=OUTPUT_INDENT_LEVEL)
        print(f"Wrote Json Data to -> {output_file_path}")
