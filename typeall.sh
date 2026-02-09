#!/usr/bin/env nix-shell
#! nix-shell -i bash --pure
#! nix-shell -p bash

IFS=:

for dir in $PATH; do
	for fil in "$dir"/*; do
		if [ "$(basename "$fil")" = "$1" ] && [ -x "$fil" ]; then
			echo "$fil"
		fi
	done
done


for dir in $PATH; do
	[ -d "$dir" ] || continue
	[ -x "$dir/$1" ] && echo "$dir/$1"
done
