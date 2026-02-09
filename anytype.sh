#!/usr/bin/env nix-shell
#! nix-shell -i bash --pure
#! nix-shell -p bash

IFS=:

for dir in $PATH; do
	[ -d "$dir" ] || continue
	for fil in "$dir"/*; do
		if [ -x "$fil" ] && basename "$fil" | grep -iq "$1"; then
			echo $fil
		fi
	done
done

shopt -s nocasematch  # make regex matches case-insensitive
search="$1"

IFS=:
for dir in $PATH; do
    [ -d "$dir" ] || continue
    for file in "$dir"/*; do
        [ -x "$file" ] || continue
        name="$(basename "$file")"
        if [[ "$name" == *"$search"* ]]; then
            echo "$file"
        fi
    done
done
