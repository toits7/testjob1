клонируем репозиторий 
git clone https://github.com/toits7/testjob1.git
создаем в корне файл .env
записываем в файл переменные окружения
HTTP_SERVER_PORT='8080'
запускаем
docker compose up -d
проверяем 
curl http://localhost