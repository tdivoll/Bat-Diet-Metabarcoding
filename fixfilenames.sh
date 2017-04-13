#!/bin/bash
cd $1;
for file in *L001*; do
  fp = "${file%L001*}";
  lp = "${file#*L001}";
  new = "${fp//_/.}L001$lp";
  mv "$file" "$new";
done
