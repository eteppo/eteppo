// we can use classes and constructors
// constructors run when class is instantiated
var Student = /** @class */ (function () {
    // set access control too
    function Student(first, middle, last) {
        this.first = first;
        this.middle = middle;
        this.last = last;
        // this keyword points to instantiated object (example below)
        this.name = first + " " + middle + " " + last;
    }
    return Student;
}());
// function that only accepts input of type Person defined above
function greeter(person) {
    return "Hello, " + person.first + " " + person.last;
}
// create new object of class Student; input values to constructor
var user = new Student("User", "U.", "Userson");
// object has properties first and last of type string; hence type Person
// add function output to html DOM body
document.body.textContent = greeter(user);
