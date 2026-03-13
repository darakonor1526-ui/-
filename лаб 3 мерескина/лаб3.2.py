# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, separator=","):
    participants1 = participants_first_group.split(separator)
    participants2 = participants_second_group.split(separator)
    common = [participant for participant in participants1 if participant in participants2]
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common}")
# TODO Провеьте работу функции с разделителем отличным от запятой
