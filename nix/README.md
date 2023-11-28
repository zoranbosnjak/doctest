# Update procedure

## niv and nix update

```bash
# update niv itself
nix-shell -p niv --run "niv init"

# update niv sources
# check actual nix release here: https://nixos.org/download.html
# at the time of writing, the actual release is 23.05
nix-shell -p niv --run "niv update nixpkgs -b release-23.05"
```

## sphinx update

Check actual version and sha256 hash here <https://pypi.org/project/Sphinx/#files>

Edit `nix/sphinx/default.nix`, adjust `version` and `sha256`.

