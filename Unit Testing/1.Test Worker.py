class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker("Worker", 250, 20)
        self.assertEqual("Worker", worker.name)
        self.assertEqual(250, worker.salary)
        self.assertEqual(20, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_incrementation_after_rest(self):
        worker = Worker("Test", 200, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_work_wit_zero_energy_raises(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_work_wit_negative_energy_raises(self):
        worker = Worker("Test", 100, -5)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_rises_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)

    def test_worker_energy_decreased_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(9, worker.energy)

    def test_get_info_returns_the_right_value_without_working(self):
        worker = Worker("Test", 100, 10)
        result = worker.get_info()
        self.assertEqual("Test has saved 0 money.", result)

    def test_get_info_returns_the_right_value_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        result = worker.get_info()
        self.assertEqual("Test has saved 100 money.", result)


if __name__ == "__main__":
    main()
