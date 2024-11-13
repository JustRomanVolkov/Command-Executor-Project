import os
import tempfile
import unittest
import io
from unittest.mock import patch
from main import CommandRunner


class TestCommandRunner(unittest.TestCase):
    def setUp(self):
        # Создаем временную директорию
        self.test_dir = tempfile.TemporaryDirectory()

        # Создаем тестовые файлы с переменными CMDS
        self.file_paths = [
            os.path.join(self.test_dir.name, 'tests/a.py'),
            os.path.join(self.test_dir.name, 'tests/1/c.py'),
            os.path.join(self.test_dir.name, 'tests/2/b.py'),
        ]

        # Создаем структуру директорий и файлы
        os.makedirs(os.path.join(self.test_dir.name, 'tests/1'), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir.name, 'tests/2'), exist_ok=True)

        with open(self.file_paths[0], 'w') as f:
            f.write("z='1'\nCMDS=['echo ' + z, 'echo 2']\n")

        with open(self.file_paths[1], 'w') as f:
            f.write("CMDS=['echo 4', 'echo 5']\n")

        with open(self.file_paths[2], 'w') as f:
            f.write("CMDS=['echo 2', 'echo 3']\n")

    def tearDown(self):
        # Удаляем временную директорию после теста
        self.test_dir.cleanup()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_command_execution(self, mock_stdout):
        runner = CommandRunner(self.test_dir.name)
        runner.run()

        # Проверка последовательности выполнения команд и вывода сообщений
        expected_output = """4
5
2
3
1
команда "echo 2" уже выполнялась
"""

        # Сравниваем результат с захваченным выводом
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
