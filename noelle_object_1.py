#class_name
#minutes_teaching
#avg_rating
#class_hours
#class_type -dictionary
#class_date
#lesson_title
#pay_amount
#students_enrolled


def take_input():
    print("Enter your selection here")
    selection = input()
    selection = selection.upper()
    selection = selection[0]
    return selection

class_types = ['social studies', 'maths' , 'sciences']


class Course():
    def __init__(self, lesson_title):
        self.lesson_title = lesson_title
        
        
    def set_class_type(self):
        print("What is the class_type?")

        count = 0
        for i in class_types:
            print(str(count) + ' ' + i)
            count += 1

        my_type = input()
        my_type = my_type[0]
        my_type = int(my_type)
        
        self.class_type = class_types[my_type]
        return self.class_type
        
    


#main
print("What is the class name?")
my_lesson_title = input()

my_class = Course(my_lesson_title)

my_local_display = my_class.set_class_type()

print("local display: " + my_local_display)
print(my_class.lesson_title)
print(my_class.class_type)
