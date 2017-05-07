## Spell-check

Install hunspell. On macOS with Homebrew: `brew install hunspell`.

```bash
$ mdspell --en-us -n -x **/*.md
```

## Find hard-coded dates

Install [ripgrep](https://github.com/BurntSushi/ripgrep).

```bash
$ rg '(Jan(unary)?|Feb(uary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Oct(ober)?|Sep(t(ember)?)?|Nov(ember)?|Dec(ember)?)\b'
$ rg '(Mon(day)|Tu(e(sday)?)?|Wed(nesday)?|Th(ur(sday)?)?|Fri(day)?)\b'
```

This can show false positives.
