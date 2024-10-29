class ResourceNotClosedException(Exception):
    pass

class Счетчик:
    def __init__(self):
        self.value = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise ResourceNotClosedException("Ресурс закрыт.")
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True
        if exc_type is not None:
            raise exc_type(exc_val)

# Пример использования:
try:
    with Счетчик() as counter:
        counter.add()
        print("Значение счетчика:", counter.value)
except ResourceNotClosedException as e:
    print("Ошибка:", e)
