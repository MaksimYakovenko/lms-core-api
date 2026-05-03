from cachetools import TTLCache
from enum import Enum

CAPTCHA_CACHE = TTLCache(maxsize=1000, ttl=300)
captcha_cache = CAPTCHA_CACHE
BASE_URL = "https://mechmat.knu.ua/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Cache-Control': 'max-age=0'
}


class LessonType(str, Enum):
    LECTURE = "LECTURE"
    PRACTICE = "PRACTICE"
    LAB = "LAB"
    SEMINAR = "SEMINAR"
    MODULE = "MODULE"
    EXAM = "EXAM"
    CREDIT = "CREDIT"
    COLLOQUIUM = "COLLOQUIUM"
    CONSULTATION = "CONSULTATION"
    FACULTATIVE = "FACULTATIVE"


LESSON_TYPE_LABELS = {
    LessonType.LECTURE: "Лекція",
    LessonType.PRACTICE: "Практична",
    LessonType.LAB: "Лабораторна",
    LessonType.SEMINAR: "Семінар",
    LessonType.MODULE: "Модуль",
    LessonType.EXAM: "Екзамен",
    LessonType.CREDIT: "Залік",
    LessonType.COLLOQUIUM: "Колоквіум",
    LessonType.CONSULTATION: "Консультація",
    LessonType.FACULTATIVE: "Факультатив",
}