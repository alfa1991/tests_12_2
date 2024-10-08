import unittest

# Класс, представляющий бегуна
class Runner:
    def __init__(self, name, speed=5):
        self.name = name  # Имя бегуна
        self.distance = 0  # Начальная дистанция
        self.speed = speed  # Скорость бегуна

    # Метод для имитации бега
    def run(self):
        self.distance += self.speed * 2  # Увеличиваем дистанцию в два раза за "шаг"

    # Метод для имитации ходьбы (не используется в тестах)
    def walk(self):
        self.distance += self.speed

    # Метод для строкового представления объекта
    def __str__(self):
        return self.name  # Возвращаем имя бегуна

    # Метод для сравнения бегунов по имени
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other  # Сравниваем с именем
        elif isinstance(other, Runner):
            return self.name == other.name  # Сравниваем с другим бегуном


# Класс, представляющий турнир
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance  # Полная дистанция турнира
        self.participants = list(participants)  # Список участников

    # Метод для запуска турнира
    def start(self):
        finishers = {}  # Словарь для хранения финишировавших
        place = 1  # Начальное место
        while self.participants:  # Пока есть участники
            for participant in self.participants[:]:  # Используем копию списка участников
                participant.run()  # Каждый участник пробегает "шаг"
                if participant.distance >= self.full_distance:  # Проверяем, достиг ли участник финиша
                    if place not in finishers:  # Если место еще не занято
                        finishers[place] = participant  # Сохраняем участника
                        place += 1  # Увеличиваем место
                        self.participants.remove(participant)  # Убираем финишировавшего участника

        return finishers  # Возвращаем словарь с результатами


# Класс для тестирования турниров
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для хранения всех результатов тестов

    def setUp(self):
        # Создаем бегунов с заданными именами и скоростями
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов по окончании
        for key, result in cls.all_results.items():
            print(f"{key}: {{", ", ".join(f"{place}: {runner}" for place, runner in result.items()), "}}")

    def test_usain_vs_nick(self):
        # Турнир между Усэйном и Ником
        tournament = Tournament(90, self.usain, self.nick)  # Создаем турнир на 90 единиц дистанции
        result = tournament.start()  # Запускаем турнир
        self.__class__.all_results['Usain_vs_Nick'] = result  # Сохраняем результаты
        # Проверяем, что последний финишировавший - Ник
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_andrei_vs_nick(self):
        # Турнир между Андреем и Ником
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results['Andrei_vs_Nick'] = result
        # Проверяем, что последний финишировавший - Ник
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_usain_andrei_vs_nick(self):
        # Турнир между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results['Usain_Andrei_vs_Nick'] = result
        # Проверяем, что последний финишировавший - Ник
        self.assertTrue(result[max(result.keys())].name == "Ник")


# Запускаем тесты, если файл выполняется напрямую
if __name__ == '__main__':
    unittest.main()
