import csv
from .algorithm import Course, Teacher, Classroom, Section, TimeSlot

def load_data_from_csv(path):
    courses, teachers, classrooms, sections = [], [], [], []
    section_courses = {}

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Example expected CSV columns:
            # course_id,course_name,teacher_id,teacher_name,section_id,...

            courses.append(Course(
                id=row['course_id'],
                name=row['course_name'],
                code=row['course_code'],
                sessions_per_week=int(row['sessions']),
                department=row['department']
            ))

            teachers.append(Teacher(
                id=row['teacher_id'],
                name=row['teacher_name'],
                courses=[row['course_id']]
            ))

            sections.append(Section(
                id=row['section_id'],
                name=row['section_name'],
                department=row['department'],
                semester=int(row['semester']),
                strength=int(row['strength'])
            ))

            section_courses.setdefault(row['section_id'], []).append(row['course_id'])

    # Static classrooms + timeslots (can also move to CSV later)
    classrooms = [
    # Original Rooms
    Classroom("R1", "Room A", 50),
    Classroom("R2", "Room B", 40),
    
    # Multi-Purpose Lecture Halls
    Classroom("MLH1", "Multi-Lecture Hall 1", 120),
    Classroom("MLH2", "Multi-Lecture Hall 2", 120),
    
    # Specialized Labs
    Classroom("SELAB", "Software Engineering Lab", 35),
    Classroom("DSLAB", "Data Science Lab", 30),
    Classroom("AILAB", "AI & Robotics Lab", 30),
    Classroom("CYBERLAB", "Cyber Security Lab", 25), # Added "More"
    
    # Other Facilities
    Classroom("SEM01", "Seminar Hall", 80),
    Classroom("AUD01", "Main Auditorium", 250),
]

    timeslots = []
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    for d in days:
        for i in range(1,6):
            timeslots.append(TimeSlot(f"{d}_{i}", d, f"{8+i}:00", f"{9+i}:00", i))

    return courses, teachers, classrooms, sections, timeslots, section_courses