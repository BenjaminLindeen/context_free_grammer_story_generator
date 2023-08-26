# Context Free Grammer Story Generator

## Introduction

A **Context-Free Grammar (CFG)** is a set of replacement rules utilized to produce strings. Despite seeming simplistic, a CFG can generate intricate textual representations when equipped with a comprehensive set of rules.

**Example Output:**
the cat bit the dog.
the girl chased the boy.
the cat chased the boy and the boy kissed the cat.
the cat bit the dog and the dog kissed the girl and the dog chased the girl.


Python modules:
- `my_rng.py`: A random number generating system.
- `cfg.py`: A CFG-based text-generation system.

These modules collaborate; the CFG text-generator will harness the RNG tool for random numbers.

## Theory

### 1. Context-Free Grammars

CFGs consist of substitution rules. Here's a rudimentary grammar:

Start ⇒ Story ’.’
Story ⇒ Phrase
Story ⇒ Phrase ’and’ Story

Each rule embodies a left-hand-side variable and a right-hand-side substitution. A variable can possess multiple rules, enabling diversity in generated text. Text generation commences with the `Start` variable, and sequentially, rules are applied to create textual content.

### 2. Random Number Generation

For random rule selection, we need random numbers. True random generation is elusive without dedicated hardware. The project will employ the **Park-Miller algorithm** for pseudo-random number generation, offering both educational value and debugging advantages.

## Project Structure

You'll produce two Python files:

- **my_rng.py**
- **cfg.py**

Both files will contain:
- A module: A series of reusable Python functions.
- A program: Direct user-interaction instructions.

**Template:**
```python
import this
import that

def function():
    code

if __name__ == "__main__":
    program code

⚠️ Note: Avoid using Python's built-in random module. Rely solely on the my_rng module for random number generation.
