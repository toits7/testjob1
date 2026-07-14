клонируем репозиторий 
git clone https://github.com/toits7/testjob1.git
создаем в корне файл .env если не хотим использовать дефолтные значеия переменных
записываем в файл переменные окружения
echo "HTTP_SERVER_PORT='8080'" > .env
запускаем
docker compose up -d
проверяем на хосте докера
curl http://localhost

можно проверить на бекенде(там при сборке образа уставлена утилита curl, если используется файл .env то порт 8080 нужно поменять на порт из файла с переменными окружения)
docker compose exec backend sh -c "curl http://localhost:8080"

можно проверить на проксе(там утилита curl идет в составе образа)
docker compose exec proxy sh -c "curl http://localhost"