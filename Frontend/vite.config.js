import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://lumi-lspp-eehwhca8ahe5dchp.centralindia-01.azurewebsites.net/', // Your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // Removes the "/api" prefix before forwarding to Flask
      },
    },
  },
})