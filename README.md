клонируем репозиторий 
git clone https://github.com/toits7/testjob1.git
создаем в корне файл .env
записываем в файл переменные окружения
echo "HTTP_SERVER_PORT='8080'" > .env
запускаем
docker compose up -d
проверяем 
curl http://localhost