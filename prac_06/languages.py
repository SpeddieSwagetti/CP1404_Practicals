from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage instances"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    """List Dynamic ProgrammingLanguages"""
    pl_list = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for item in pl_list:
        if item.is_dynamic():
            print(item.name)


main()