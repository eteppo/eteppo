#!/usr/bin/ruby -w
# def to define function like in Python but without colon
def longest_repetition(string)
  # method chaining in ruby
  max = string
          .chars
          .chunk(&:itself)
          .map(&:last)
          .max_by(&:size)
  # short-hand syntax for if-else
  max ? [max[0], max.size] : ["", 0]
end
# run program with "ruby" command line tool