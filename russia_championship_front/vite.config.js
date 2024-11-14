import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import dotenv from 'dotenv';

dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host : true,
    proxy: {
      '/api': {
        target: "http://172.20.10.3:8000" || process.env.URL, // Добавлен http://
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, ''),
      },
    },
  },
});
