from visit_check import VisitCheck


def main():
    visit_check = VisitCheck()
    visit_check.load_dataset("apalula.json")

    question_cases = [
        ("Aco", "Armory"),
        ("Aro", "City Wall"),
        ("Baco", "Storage"),
        ("Aco", "Aco Home"),
        ("Baco", "Storage")
    ]

    for citizen_name, place in question_cases:
        print(f"Can {citizen_name} visit {place}? {visit_check.can_visit(citizen_name, place)}")




if __name__ == "__main__":
    main()