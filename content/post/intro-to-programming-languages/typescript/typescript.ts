// we can use classes and constructors
// constructors run when class is instantiated
class Student {
	// define property and its data type
    name: string;
    // can use access control keywords too; public allows access outside class block
    constructor(public first: string, public middle: string, public last: string) {
        // this keyword points to instantiated object (example below)
        this.name = first + " " + middle + " " + last;
    }
}
// interfaces allow defining a type of object; much like string or boolean
interface Person {
    first: string;
    last: string;
}
// function that only accepts input of type Person defined above
function greeter(person: Person) {

    return "Hello, " + person.first + " " + person.last;
}
// create new object of class Student; input values go to constructor
let user = new Student("User", "U.", "Userson");
// object has properties first and last of type string; hence type Person
// add function output to html DOM body
document.body.textContent = greeter(user);