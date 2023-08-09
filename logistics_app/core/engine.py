from core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output: list[str] = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                command = self._command_factory.create(input_line) 
                output.append(command.execute())
            except ValueError as err:
                print(err.args[0])

        with open(file='data_output.txt', mode='w') as file:
            file.writelines('\n'.join(output))

        print('\n'.join(output))