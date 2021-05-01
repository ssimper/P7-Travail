from .sentences import welcome
from ..parser.program.parser01 import Parser

class InvocateGp:

    def the_answer(self):
        answer = input("Bonjour ! Quelle question voulez-vous poser à GranPy ?")
        return answer


def main():
    
    test = InvocateGp()
    to_parse = test.the_answer()
    print(to_parse)


if __name__ == "__main__":
    main()

