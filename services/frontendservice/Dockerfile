# Use Node.js as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Set environment variables
ENV NODE_ENV=development
ENV VITE_HOST=0.0.0.0
ENV VITE_PORT=5173

# Expose port 5173 (default Vite dev server port)
EXPOSE 5173

# Start the development server with host flag
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]