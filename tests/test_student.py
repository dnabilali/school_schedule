from school_schedule.student import Student
import pytest

def test_student_instance_with_valid_input():
    new_student = Student("Claire", "5th", [])

    assert new_student.name == "Claire"
    assert new_student.grade == "5th"
    assert new_student.classes == []

def test_student_instance_with_invalid_input():
    with pytest.raises(TypeError):
        Student("","", [])


