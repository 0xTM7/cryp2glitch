# cryp2glitch

Python script obfuscation tools for transforming and securing Python code through sophisticated obfuscation techniques.

## Overview

cryp2glitch provides a comprehensive toolkit for obfuscating Python scripts, making it difficult to reverse-engineer or understand the original code structure. This tool is useful for protecting intellectual property and securing sensitive logic in Python applications.

## Features

- **Script Obfuscation**: Transform readable Python code into obfuscated versions
- **Variable Renaming**: Systematically rename variables to meaningless identifiers
- **Code Transformation**: Apply various transformation techniques to obscure code flow
- **String Encryption**: Encrypt string literals in your code
- **Control Flow Obfuscation**: Modify program structure while maintaining functionality

## Installation

```bash
git clone https://github.com/tom7voldemort/cryp2glitch.git
cd cryp2glitch
```

# example of use:
```
python3 cryp2glitch -f test.py -o output.py -e # encrypt or -d for decrypt.
```
