<!-- <template>
    <div>
      <h1>Авторизация через Google</h1>
      <p>Обработка кода авторизации...</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        code: null
      };
    },
    created() {
      // Получаем параметр 'code' из URL
      const urlParams = new URLSearchParams(window.location.search);
      this.code = urlParams.get('code'); // Сохраняем значение 'code'
  
      if (this.code) {
        // Здесь вы можете отправить код на сервер для получения токена доступа
        this.exchangeCodeForToken();
      } else {
        // Если кода нет в URL, показываем ошибку или другую логику
        console.error('Нет кода авторизации в URL');
      }
    },
    methods: {
      exchangeCodeForToken() {
        // Пример отправки кода на сервер для получения токена
        fetch('http://localhost:8000/auth/google', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ code: this.code })
        })
          .then(response => response.json())
          .then(data => {
            console.log('Токен доступа:', data.access_token);
          })
          .catch(error => {
            console.error('Ошибка при получении токена:', error);
          });
      }
    }
  };
  </script>
   -->