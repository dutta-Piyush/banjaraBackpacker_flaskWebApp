import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: true,
    watch: {
      usePolling: true
    },
    proxy: {
      '/api/auth': {
        target: 'http://auth-service:5001',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api\/auth/, '/api')
      },
      '/api/blog': {
        target: 'http://blog-service:5002',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api\/blog/, '/api')
      }
    }
  }
})
