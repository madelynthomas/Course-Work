/**
 * Student
 */

public class Student implements Comparable<Student> { // constructor
    public Student leftChild;
    public Student rightChild;
    public Double gpa = 0.0;

    public Student(Double gradePointAverage) {
        gpa = gradePointAverage;
    } // end constructor

    public int compareTo(Student student) {
        if(this.gpa == student.gpa)
            return 0; // return equal
        else if (this.gpa < student.gpa)
            return 1; // return greater than
        else
            return -1; // return less than
    } // end compareTo
} // end Student class
