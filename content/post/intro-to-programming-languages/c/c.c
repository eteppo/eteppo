// include header file stdio.h here
// contains standard input output programs
#include <stdio.h>
 // main is run when program is run 
// must define type of return data
int main() {
    // declare 3 variables, define 1
    int number, reversed = 0, remainder, original;
    // output to terminal (stdin)
    printf("Enter an integer: ");
    // input from terminal
    // %d means integer, &number means address of variable number
    scanf("%d", &number);
    // value in address &number is original input
    original = number;
    // reverse number with modulo math
    // != means "is not equal to"
    while (number != 0) {
        // % means modulo; returns last digit in input
        remainder = number % 10;
        // set last number first
        reversed = reversed * 10 + remainder;
        // "x /= y" is short for "x = x / y"
        number /= 10;
    }
    // palindromes are same in either direction
    if (original == reversed)
        printf("%d is a palindrome.\n", original);
    else
        printf("%d is not a palindrome.\n", original);
    // must return something; 0 used for nothing
    return 0;
}
//compile with gcc filename.c
//run executable compiled program with ./filename