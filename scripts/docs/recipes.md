## Find hard-coded dates

Install [ripgrep](https://github.com/BurntSushi/ripgrep).

```bash
$ rg '(Jan(unary)?|Feb(uary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Oct(ober)?|Sep(t(ember)?)?|Nov(ember)?|Dec(ember)?)\b'
$ rg '(Mon(day)|Tu(e(sday)?)?|Wed(nesday)?|Th(ur(sday)?)?|Fri(day)?)\b'
```

This shows false positives.

## Lint and style-check embedded code blocks

```bash
$ jekyll build
$ ./scripts/extract_code_blocks > blocks.py
$ flake8 blocks.py --ignore=E402,H101,W391 --max-line-length=100
```

This shows false positives. In particular, the equations that
generate the computational art are marked up as Python but are
long and are split across lines.
