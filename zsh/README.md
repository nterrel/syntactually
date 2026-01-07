# Zsh syntax and features

## Files

- `basics.zsh` — Zsh-specific features: 1-indexed arrays, associative arrays, parameter expansion flags, extended globbing, glob qualifiers, floating-point arithmetic, aliases, modules, and more.

## Run

Using Makefile targets (recommended):

```bash
make zsh        # Syntax check + run all scripts
make zsh-check  # Syntax check only (from zsh directory)
```

Or run scripts directly:

```bash
chmod +x basics.zsh

zsh basics.zsh
# or if executable:
./basics.zsh
```

## Key Zsh Features

### Differences from Bash

- **Arrays are 1-indexed** (not 0-indexed like bash)
- Native associative array support (no version check needed)
- More powerful parameter expansion with flags
- Extended globbing with qualifiers
- Floating-point arithmetic support

### Extended Globbing

Zsh globbing is incredibly powerful:

- `**/*.txt` - recursive search
- `*(.)` - only regular files
- `*(/)` - only directories
- `*(Om)` - sort by modification time (newest first)
- `*(L0)` - empty files

### Parameter Expansion Flags

- `${(U)var}` - uppercase
- `${(L)var}` - lowercase
- `${(j:,:)array}` - join array with commas
- `${(@s: :)string}` - split string into array

### Additional Features

- Global aliases (expand anywhere)
- Suffix aliases (auto-open by extension)
- Named directories
- Loadable modules for extra functionality
- Powerful completion system

## Testing

Scripts are automatically tested via `make test` and in CI to ensure they run without errors and produce expected outputs.
