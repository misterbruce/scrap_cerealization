# Path Serialization Experiment

An early Python experiment in packing a text file's original path and contents into a single string and recovering the original path from its length-prefixed metadata.

This prototype was developed while exploring file serialization for the separate [EDP](https://github.com/misterbruce/EDP) experiment.

## Format

The conceptual payload is `<path character count>^<path><file text>`. During unpacking, the leading count determines how many characters belong to the path.

## Current implementation

The script `path_bundle_file_creation.py` demonstrates file creation, packing and unpacking. **Importing or running it creates a local test file in the user's Documents folder.** Its unpacker writes to a path specified in serialized data; do not use untrusted inputs or execute it against valuable files.

## Limitations

- Not a standardized, secure, or authenticated serialization format.
- Text-file only; no support for arbitrary binary files or encoding metadata.
- Does not validate recovered output paths against an allowed directory.
- Existing-file behavior and malformed-input handling are not robustly tested.
- The script has side effects at import time.

## Next steps

Convert it into a pure, side-effect-free `pack(path, content)` / `unpack(payload)` library, validate lengths and paths, and add unit tests using temporary directories. Until then, treat it solely as a historical educational prototype.
