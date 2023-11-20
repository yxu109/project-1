Yizheng Xu yxu109@stevens.edu

1. https://github.com/yxu109/project-1.git

2. 50h

3. For my project, which consists of implementing wc.py, gron.py, and ungron.py, I employed a combination of manual testing and automated testing using a custom test harness (test.py).

4. Errors that occur when the program runs differently than expected due to incorrect logic or algorithms. 

While working on wc.py, a script designed to mimic the Unix wc command by counting lines, words, and characters in a file, I encountered a significant issue. After implementing exception handling, I discovered the script was running out of memory. This led me to believe the issue was related to how the file content was being read and processed. I conducted research on memory-efficient file reading in Python and learned that reading large files line-by-line, instead of reading the whole file into memory at once, is more memory-efficient.

5. List of Implemented Extensions

Extension: More Advanced wc - Flags to Control Output
Enhanced the wc.py program to support flags (-l, -w, -c) that control the output to show only lines, words, or characters, respectively.

Added argument parsing using Python’s argparse module.
Based on the flags provided by the user, the program selectively counts and displays lines, words, or characters.
Testing:

Test without flags to ensure default behavior (counting lines, words, and characters).
Test with each flag individually and in combination (-lw, -lc, -wc, -lwc) to ensure correct output.
Include test cases for empty input and large files.


Extension: More Advanced gron - Control the Base-Object Name
Modified gron.py to allow a user-defined base object name in the flattened JSON output, using the --obj flag.

Implemented additional command-line argument --obj to specify the base object name.
The JSON flattening function was adjusted to use this user-provided base object name instead of the default json.

Test with the --obj flag to ensure the custom object name is used in the output.
Compare against expected output where the base name is replaced with the specified name.
Test without the --obj flag to ensure default behavior remains unchanged.

