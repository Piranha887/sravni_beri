# Определение функции rate_limit с параметрами limit и key (key имеет значение по умолчанию None)
def rate_limit(limit: int, key=None):
    # Определение внутреннего декоратора decorator, который принимает функцию func
    def decorator(func):
        # Установка атрибута 'throttling_rate_limit' для функции func со значением limit
        setattr(func, 'throttling_rate_limit', limit)

        # Проверка, если key не является None
        if key:
            # Установка атрибута 'throttling_key' для функции func со значением key
            setattr(func, 'throttling_key', key)

        # Возвращение функции func
        return func

    # Возвращение декоратора decorator
    return decorator
