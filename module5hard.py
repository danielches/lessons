from typing import List, Optional, NoReturn
from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int) -> NoReturn:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self) -> str:
        return f"{self.nickname}"


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False) -> NoReturn:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users: List[User] = None, videos: List[Video] = None,
                 current_user: Optional[User] = None) -> NoReturn:
        self.users = [] if users is None else users
        self.videos = [] if videos is None else videos
        self.current_user = current_user

    def log_in(self, nickname: str, password: str) -> NoReturn:
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int) -> NoReturn:
        if nickname in [user.nickname for user in self.users]:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_out(self) -> NoReturn:
        self.current_user = None

    def add(self, *videos: Video) -> NoReturn:
        titles_video = [v.title for v in self.videos]
        for video in videos:
            if video.title not in titles_video:
                self.videos.append(video)

    def get_videos(self, search_query: str) -> List[str]:
        found_videos = []
        for video in self.videos:
            if search_query.upper() in video.title.upper():
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, title: str) -> NoReturn:
        if self.current_user is not None:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while video.time_now < video.duration:
                            sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=" ")
                        print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
