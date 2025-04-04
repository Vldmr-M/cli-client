# Клиент для сервиса отправки SMS

## установка и запуск

```bash
# 1 Клонировать репозиторий и установить uv
git clone https://github.com/Vldmr-M/cli-client
cd cli-client
pip install uv

# 2 Установить зависимости
uv sync
source .venv/bin/activate.fish

# 3 Запустить клиент
uv run ./src/main.py -s 111 -r 222 -m "Hello World"

# 6. Запустить тесты
pytest
```
