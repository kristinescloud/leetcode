#!/bin/bash

echo -e "Enter the path to the directory you would like to clean:"
read target_dir

cd $target_dir

rm -rf *.html
rm -rf *_files

echo "Exit code $?"
