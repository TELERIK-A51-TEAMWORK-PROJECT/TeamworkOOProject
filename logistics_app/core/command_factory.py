from commands.create_scania import CreateScaniaCommand

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createscania":
            return CreateScaniaCommand(params, self._app_data)
        
        raise ValueError(f'Invalid command name: {cmd}!')