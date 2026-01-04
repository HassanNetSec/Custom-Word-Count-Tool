# ccwc - Custom Word Count Tool

A Python implementation of the Unix `wc` (word count) command-line tool built as part of [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc).

## 🎯 Overview

`ccwc` (Coding Challenges Word Count) is a lightweight command-line utility that mimics the functionality of the classic Unix `wc` tool. It provides accurate counting of bytes, lines, and words in text files, with full support for standard input (stdin) through pipes.
## 📸 Screenshots

### Basic Usage
<img width="692" height="52" alt="image" src="https://github.com/user-attachments/assets/40f55ddf-15c6-4598-9be7-94a22ec0f000" />

### Standard Input (Pipe) Usage
<img width="700" height="28" alt="image" src="https://github.com/user-attachments/assets/1b608542-11e8-4f95-8896-6402fbdf1aae" />
*Processing input from pipes with different options*

### Error Handling
<img width="695" height="29" alt="image" src="https://github.com/user-attachments/assets/43ea6b51-33ef-4fd5-b0ce-24d40d7d4090" />
*Graceful handling of missing files and invalid inputs*
## ✨ Features

- **Byte Counting (`-c`)**: Count the number of bytes in a file
- **Line Counting (`-l`)**: Count the number of lines in a file
- **Word Counting (`-w`)**: Count the number of words in a file
- **Standard Input Support**: Process input from pipes and redirects
- **Default Behavior**: Display all statistics when no option is specified
- **Error Handling**: Graceful handling of missing files and encoding issues

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher

### Clone the Repository
```bash
git clone https://github.com/HassanNetSec/ccwc-tool.git
cd ccwc-tool
```

## 📖 Usage

### Basic Commands

#### Count Bytes in a File
```bash
python tool.py -c test.txt
```
**Output:**
```
  342190 test.txt
```

#### Count Lines in a File
```bash
python tool.py -l test.txt
```
**Output:**
```
  7145 test.txt
```

#### Count Words in a File
```bash
python tool.py -w test.txt
```
**Output:**
```
  58164 test.txt
```

#### Display All Statistics
```bash
python tool.py test.txt
```
**Output:**
```
  7145  58164 342190 test.txt
```

### Advanced Usage with Pipes

#### Using with `cat` (Unix/Linux/Mac)
```bash
cat test.txt | python tool.py -l
```
**Output:**
```
  7145
```

#### Using with `type` (Windows)
```bash
type test.txt | python tool.py -w
```

#### Chaining Multiple Commands
```bash
echo "Hello World" | python tool.py -w
```
**Output:**
```
  2
```

## 🛠️ Technical Details

### Command-Line Options

| Option | Description | Example Output |
|--------|-------------|----------------|
| `-c` | Count bytes | `  342190 test.txt` |
| `-l` | Count lines | `  7145 test.txt` |
| `-w` | Count words | `  58164 test.txt` |
| (none) | All statistics | `  7145  58164 342190 test.txt` |

### How It Works

- **Byte Counting**: Opens files in binary mode (`rb`) for accurate byte counting, preventing encoding-related discrepancies
- **Line Counting**: Uses `readlines()` to count newline characters
- **Word Counting**: Splits content on whitespace (spaces, tabs, newlines)
- **Stdin Processing**: Reads from `sys.stdin` when input is piped from another command

## 📂 Project Structure
```
ccwc-tool/
├── tool.py          # Main implementation
├── README.md        # Project documentation
├── test.txt         # Sample test file
└── .gitignore       # Git ignore rules
```

## 🧪 Testing

The tool has been tested against the original Unix `wc` command to ensure accuracy:
```bash
# Test with the provided test file
python tool.py -c test.txt
wc -c test.txt

python tool.py -l test.txt
wc -l test.txt

python tool.py -w test.txt
wc -w test.txt
```

Expected results should match the Unix `wc` output exactly.

## 🐛 Error Handling

The tool handles common errors gracefully:

- **File Not Found**: Displays appropriate error message
- **Encoding Issues**: Uses UTF-8 encoding with fallback handling
- **Invalid Options**: Falls back to default behavior (display all stats)

Example error output:
```bash
python tool.py -c nonexistent.txt
# Output: ccwc: nonexistent.txt: No such file or directory
```

## 💡 Implementation Highlights

- **Binary Mode for Byte Count**: Ensures accurate byte counting by reading files in binary mode
- **Efficient String Processing**: Uses Python's built-in methods for optimal performance
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- **Clean Code Structure**: Well-documented functions with type hints
- **Professional Error Messages**: Outputs errors to `stderr` following Unix conventions

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- Python file I/O operations
- Command-line argument parsing with `sys.argv`
- Standard input/output handling
- Error handling and edge case management
- Text processing and string manipulation
- Adherence to Unix tool conventions

## 🗓️ Development Timeline

- **Day 1** of 21-Day Coding Challenge
- **Duration**: 1 day
- **Challenge Source**: [Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)

## 🔗 Connect With Me

- **Portfolio**: [portfolio-website-nu-seven-13.vercel.app](https://portfolio-website-nu-seven-13.vercel.app)
- **GitHub**: [@HassanNetSec](https://github.com/HassanNetSec)
- **LinkedIn**: [Hassan Khan](https://linkedin.com/in/hassan-khan-641a32371)
- **Email**: hassankhancyber647@gmail.com

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Challenge inspired by [Coding Challenges](https://codingchallenges.fyi/)
- Part of my journey to master secure software development and DevSecOps

---

**⭐ If you found this project helpful, please consider giving it a star!**

*Built with 💻 and ☕ by Hassan Khan*
```

---

## 🎁 **Bonus: LICENSE File** (MIT License)

Create a file named `LICENSE`:
```
MIT License

Copyright (c) 2026 Hassan Khan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
