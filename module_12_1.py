from unittest import TestCase, main


class Runner:
    runner_id = 0

    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.runner_id += 1

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner(f"Runner {Runner.runner_id}")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner(f"Runner {Runner.runner_id}")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_test_challenge(self):
        runner1 = Runner(f"Runner {Runner.runner_id}")
        runner2 = Runner(f"Runner {Runner.runner_id}")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    main()
