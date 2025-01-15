import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import dotenv from 'dotenv';

dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({
  assetsInclude: ['**/*.JPG'],
  plugins: [vue()],
  base: './',
  build: {
    outDir: 'dist',
  },
  server: {
    host : true,
    proxy: {
      '/api': {
        target: process.env.URL, // Добавлен http://
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, ''),
      },
    },
  },
});
