
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output: list[str] = []
        while True:
            input_line = input()
            if input_line.lower() == 'end':
                break

            command = self._command_factory.create(input_line) #addtest
            output.append(command.execute())

            #veche ot komandite trqq napraim execute

        print('\n'.join(output))