
#!/bin/bash
# define function
get_files () {
  # ls returns filenames that match its argument
  # * matches anything, including nothing
  # set result to global variable
  file_names="`ls *.html`"
}
# another function for counting lines
count_lines () {
  # local means variable cannot be accessed outside function
  # $1 is special and refers to first argument
  local file_name=$1
  # wc -l prints newline counts
  # | pipes left-side output as right-side input
  # sed edits text; s refers to substitute, rest is regex
  line_count=`wc -l $file_name | sed 's/^\([0-9]*\).*$/\1/'`
}
# conditions go inside [ ]
# $# -ge 1 means number of script arguments greater or equal to 1
# so if arguments given...
if [ $# -ge 1 ]
then
  echo "Error: Use without arguments."
  exit 1
fi
# set internal field separator as newline character, excludes space and tab
IFS=$'\012'
# initialize counters
line_count=0
file_count=0
line_count_sum=0
# run get_files; populates file_names list data structure
get_files
# loop over file_names
for file_name in $file_names
do
  count_lines $file_name
  # print result to terminal
  echo "$file_name: $line_count"
  # math operations within [ ]
  # need $ to make return value a variable
  file_count=$[ $file_count + 1 ]
  # increase sum of all lines
  line_count_sum=$[ $line_count_sum + $line_count ]
done
# print result to terminal
echo "$file_count files in total, with $line_count_sum lines in total"