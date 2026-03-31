from datetime import datetime

syll = []

def add_topic(sub_name, topic_name, exam_date, prep_lvl):
    target_date = datetime.strptime(exam_date, "%Y-%m-%d")
    time_diff = target_date - datetime.now()
    days_remain = time_diff.days

    # if the exam already passed or is today, set 0 to avoid -ve nos
    if days_remain < 0:
        days_remain = 0

    new_topic = {
        'subject': sub_name,
        'topic': topic_name,
        'days_left': days_remain,
        'prep': prep_lvl  # 1 means totally unprepared and 5 means fully ready
    }
    syll.append(new_topic)

def get_urgency(item):
    return item['score']

def create_plan(hrs_available):
    print(f"\n Study Plan for Today ({hrs_available} Hours) ")

    for item in syll:
        # formula: low prep + less days = higher score
        # adding 1 to days_left so as to not divide by 0
        calc_score = (5 - item['prep']) / (item['days_left'] + 1)
        item['score'] = calc_score

    # sort the list (highest score first)
    syll.sort(key=get_urgency, reverse=True)

    hrs_done = 0

    for item in syll:
        if hrs_done < hrs_available:
            print(f"Hour {hrs_done + 1}: {item['subject']} ({item['topic']})")
            hrs_done += 1
        else:
            break

while True:
    sub = input("Subject (or 'done'): ")
    
    if sub.lower() == 'done':
        break
        
    topic = input("Topic: ")
    date = input("Exam Date (YYYY-MM-DD): ")
    p_lvl = int(input("Prep level (1-5): "))
    
    add_topic(sub, topic, date, p_lvl)
    print("added to list\n")

print("\n Syllabus saved ")

if len(syll) > 0:
    hrs = int(input("How many hours can you study? "))
    create_plan(hrs)
else:
    print("Nothing added!")
