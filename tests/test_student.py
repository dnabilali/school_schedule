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

def test_add_class_method_with_valid_input():
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )

    claire.add_class("python")

    assert "python" in claire.classes
    assert claire.get_num_classes() == 6
    

def test_add_class_method_duplicate_class():
    claire = Student( 
            "Claire", 
            "freshman", 
            [ 
                "Algebra", 
                "Writing", 
                "Contemporary World Issues", 
                "Gym", 
                "Earth Science" 
            ]
        )

    result = claire.add_class("Algebra")

    assert claire.get_num_classes() == 5
    assert not result

