# Text Tokenizer

A simple Python library for encoding text to ASCII tokens and decoding tokens back to text.

## Overview

This project provides functions to:
1. Convert characters to their ASCII token values
2. Decode ASCII token values back to human-readable text

## Files

- **tokenizer.py**: Contains the core tokenization and detokenization functions
- **all_characters.py**: Includes a comprehensive mapping of characters to different numerical representations

## Usage

### Basic Tokenization

```python
from tokenizer import convert_chars_to_token, decode_token

# Encode text to tokens
sample_text = "Hello, World!"
encoded_tokens = convert_chars_to_token(sample_text)
print(f"Encoded: {encoded_tokens}")

# Decode tokens back to text
decoded_text = decode_token(encoded_tokens)
print(f"Decoded: {decoded_text}")
```

### Output

