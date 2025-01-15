FROM node:18

RUN mkdir /frontend
# Устанавливаем рабочую директорию
WORKDIR /frontend

# Установка Vue CLI и зависимостей приложения
COPY package*.json ./

RUN npm install
# -g @vue/cli && npm install && npm cache clean --force

# Копирование остального кода приложения
COPY . .

RUN chmod a+x /frontend/docker/*.sh

RUN npm run build

EXPOSE 5173

# Команда для запуска приложения
CMD ["npx", "serve", "-s", "dist"]