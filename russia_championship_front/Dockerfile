FROM node:18-alpine

RUN mkdir /frontend
# Устанавливаем рабочую директорию
WORKDIR /frontend

# Установка Vue CLI и зависимостей приложения
COPY package*.json ./

RUN npm install -g @vue/cli && npm install && npm cache clean --force

# Копирование остального кода приложения
COPY . .

RUN chmod a+x /frontend/docker/*.sh

# Команда для запуска приложения
CMD ["npm", "run", "dev"]