// public allows use of class outside package
// everything must be absracted to classes in Java
public class Java {
 	// static means a method of class, not of object made from it
 	// void means doesn't return data
 	// String is data type, [] means array
 	// main method is called if class is called
	public static void main(String[] args) {
		// make new array of numbers
		int numbers[] = new int[]{32,43,53,54,32,65,63,98,43,23};
		// initialize variables; [0] means first item in array
		int smallest = numbers[0];
		int largest = numbers[0];
		// from index 1 until index of last number, one-by-one
		for (int i = 1; i < numbers.length; i++) {
			// if larger, set as largest
			if (numbers[i] > largest) {
				largest = numbers[i];
			// if smaller, set as smallest
			} else if (numbers[i] < smallest) {
				smallest = numbers[i];
			}	
		}
		// built-in System.out has println to print to terminal
		System.out.println("Largest Number is : " + largest);
		System.out.println("Smallest Number is : " + smallest);
	}
}
// compile program with "javac" command line program
// run compiled program with "java" command line program