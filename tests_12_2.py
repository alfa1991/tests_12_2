import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2  # Увеличиваем дистанцию в два раза за "шаг"

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name  # Возвращаем имя бегуна

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Используем копию списка
                participant.run()
                if participant.distance >= self.full_distance:
                    if place not in finishers:  # Проверяем, если место еще не занято
                        finishers[place] = participant
                        place += 1
                        self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для хранения всех результатов

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {{", ", ".join(f"{place}: {runner}" for place, runner in result.items()), "}}")

    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results['Usain_vs_Nick'] = result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_andrei_vs_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results['Andrei_vs_Nick'] = result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_usain_andrei_vs_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        result = tournament.start()
        self.__class__.all_results['Usain_Andrei_vs_Nick'] = result
        self.assertTrue(result[max(result.keys())].name == "Ник")


if __name__ == '__main__':
    unittest.main()
