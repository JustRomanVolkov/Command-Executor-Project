import os
import importlib.util
import subprocess
from typing import List, Set


class CommandExecutor:
    """
    Class for executing commands
    """
    def __init__(self):
        self.executed_commands: Set[str] = set()

    def execute(self, cmd: str):
        if cmd in self.executed_commands:
            print(f'команда "{cmd}" уже выполнялась')
        else:
            try:
                # subprocess.run(cmd, shell=True, check=True)
                # Исполняем команду и захватываем результат для возможности тестирования
                result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
                print(result.stdout.strip())  # Вывод результата команды
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при выполнении команды '{cmd}': {e}")
            self.executed_commands.add(cmd)


class CommandLoader:
    """
    Class for loading commands from files
    """
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def find_command_files(self) -> List[str]:
        command_files = []
        for dirpath, _, filenames in os.walk(self.root_dir):
            for file in filenames:
                if file.endswith('.py'):
                    command_files.append(os.path.join(dirpath, file))
        return sorted(command_files)

    def load_commands_from_file(self, file_path: str) -> List[str]:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, 'CMDS', [])


class CommandRunner:
    """
    Class for running commands
    """
    def __init__(self, root_dir: str):
        self.loader = CommandLoader(root_dir)
        self.executor = CommandExecutor()

    def run(self):
        command_files = self.loader.find_command_files()
        for file_path in command_files:
            commands = self.loader.load_commands_from_file(file_path)
            for command in commands:
                self.executor.execute(command)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    runner = CommandRunner(root_directory)
    runner.run()
