# Banjara Backpacker - Travel Blog Platform

A full-stack travel blog platform built with Flask and React, containerized using Docker.

## Project Overview

This project consists of multiple microservices working together to provide a complete travel blog platform:

### Services

1. **Frontend Service (React + Vite)**
   - Port: 5173
   - Features:
     - User authentication (login/register)
     - Blog post viewing and creation
     - Responsive design
     - Modern UI with Tailwind CSS

2. **Authentication Service (Flask)**
   - Port: 5001
   - Features:
     - User registration
     - User login
     - JWT token management
     - User profile management

3. **Blog Service (Flask)**
   - Port: 5002
   - Features:
     - Blog post CRUD operations
     - Comment system
     - User-specific blog management

4. **Database (PostgreSQL)**
   - Port: 5432
   - Features:
     - User data storage
     - Blog post storage
     - Comment storage
     - Secure data management

## Prerequisites

- Docker
- Docker Compose
- Git

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd banjaraBackpacker_flaskWebApp
   ```

2. Create a `.env` file in the root directory with the following variables:
   ```env
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_DB=your_db_name
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   ```

3. Start the services:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: http://localhost:5173
   - Auth Service: http://localhost:5001
   - Blog Service: http://localhost:5002

## Project Structure

```
banjaraBackpacker_flaskWebApp/
├── frontendService/          # React frontend
├── authUser/                 # Authentication service
├── blogPostService/         # Blog service
├── docker-compose.yml       # Docker compose configuration
└── .env                     # Environment variables
```

## API Endpoints

### Authentication Service
- POST `/api/register` - User registration
- POST `/api/login` - User login
- GET `/api/user` - Get user profile
- PUT `/api/user` - Update user profile

### Blog Service
- GET `/api/posts` - Get all blog posts
- POST `/api/posts` - Create new blog post
- GET `/api/posts/<id>` - Get specific blog post
- PUT `/api/posts/<id>` - Update blog post
- DELETE `/api/posts/<id>` - Delete blog post

## Docker Configuration

The project uses Docker Compose to manage multiple services:

```yaml
services:
  frontend:
    build: ./frontendService
    ports:
      - "5173:5173"
    depends_on:
      - auth
      - blog

  auth:
    build: ./authUser
    ports:
      - "5001:5001"
    depends_on:
      - postgres

  blog:
    build: ./blogPostService
    ports:
      - "5002:5002"
    depends_on:
      - postgres

  postgres:
    image: postgres:latest
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

## Docker Networking Evolution

### Initial Configuration (Working but Not Ideal)

Initially, our frontend service was configured to use localhost URLs:

```yaml
frontend-service:
  environment:
    - VITE_AUTH_SERVICE_URL=http://localhost:5001
    - VITE_BLOG_SERVICE_URL=http://localhost:5002
```

This worked because of port mappings in our services:
```yaml
auth-service:
  ports:
    - "5001:5001"  # Maps container port 5001 to host port 5001

blog-service:
  ports:
    - "5002:5002"  # Maps container port 5002 to host port 5002
```

#### How it Worked:
1. Frontend container made requests to localhost:5001
2. These requests reached the host machine
3. Host machine forwarded requests to the appropriate container
4. Communication path: Frontend Container → Host Machine → Backend Container

#### Why it Worked but Wasn't Ideal:
- Relied on port mappings to the host machine
- Bypassed Docker's internal networking
- Less efficient due to extra hop through host machine
- Less secure than direct container communication
- Didn't follow Docker best practices

### Improved Configuration (Current)

We updated to use Docker's internal DNS and direct container communication:

```yaml
frontend-service:
  environment:
    - VITE_AUTH_SERVICE_URL=http://auth-service:5001
    - VITE_BLOG_SERVICE_URL=http://blog-service:5002
```

#### Benefits of New Configuration:
1. **Direct Communication**:
   - Frontend Container → Backend Container
   - No intermediate hop through host machine
   - More efficient request routing

2. **Docker DNS**:
   - Uses Docker's internal DNS resolution
   - Service names resolve to container IPs
   - More reliable container discovery

3. **Security**:
   - Better network isolation
   - Proper container-to-container communication
   - Follows Docker security best practices

4. **Performance**:
   - Reduced network latency
   - More efficient request handling
   - Better resource utilization

#### Implementation Details:
```yaml
# docker-compose.yml
services:
  frontend-service:
    environment:
      - VITE_AUTH_SERVICE_URL=http://auth-service:5001
      - VITE_BLOG_SERVICE_URL=http://blog-service:5002
    networks:
      - banjaraBackpacker-network

  auth-service:
    networks:
      - banjaraBackpacker-network

  blog-service:
    networks:
      - banjaraBackpacker-network

networks:
  banjaraBackpacker-network:
    driver: bridge
```

This configuration ensures:
- All services are on the same Docker network
- Direct container-to-container communication
- Proper service discovery
- Better security and performance

## Version History

### v1.2
- Fixed backend services to bind to 0.0.0.0 instead of localhost, allowing proper communication between containers
- Updated Vite proxy configuration to correctly route API requests
- Ensured frontend components are using the correct API endpoints
- Implemented working authentication system with registration and login
- Established proper communication between frontend and backend services
- Configured correct routing of API requests through the proxy
- Set up proper container networking in Docker

### v1.1
- Initial setup of microservices architecture
- Basic authentication system implementation
- Blog post functionality
- Docker containerization

### v1.0
- Project initialization
- Basic project structure setup

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Environment Configuration

The project uses environment-specific configurations to handle different deployment scenarios (development vs production).

### Configuration System

Each service (auth and blog) has its own `config.py` that manages environment-specific settings:

```python
# Example from authUser/config.py
class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'localhost'
    PORT = 5001

class ProductionConfig(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5001
```

### Development Workflow

1. **Local Development**:
   - By default, services run in development mode
   - Host is set to `localhost`
   - Debug mode is enabled
   - Database connection uses localhost
   - Run services directly:
     ```bash
     # Auth Service
     cd authUser
     python run.py

     # Blog Service
     cd blogPostService
     python run.py
     ```

2. **Production (Docker)**:
   - Services run in production mode
   - Host is set to `0.0.0.0` for container networking
   - Debug mode is disabled
   - Database connection uses Docker service names
   - Run using Docker Compose:
     ```bash
     docker-compose up --build
     ```

### Environment Variables

The application uses the following environment variables:

- `FLASK_ENV`: Controls the environment (development/production)
  - When set to `development`:
    - Enables debug mode
    - Shows detailed error pages
    - Enables auto-reloader
    - Uses localhost for connections
    - Enables development-specific features
  - When set to `production`:
    - Disables debug mode for security
    - Shows minimal error pages
    - Disables auto-reloader
    - Uses 0.0.0.0 for container networking
    - Optimizes for performance
    - Enables production-specific security features
  - Default: `development` if not specified

  > **Implementation Note**: While Flask has some built-in environment handling, we've implemented our own configuration system using Python classes. This gives us more control and flexibility over environment-specific settings. The configuration is managed through `config.py` in each service, which uses the `FLASK_ENV` variable to determine which settings to apply.

- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `POSTGRES_HOST`: Database host
- `POSTGRES_PORT`: Database port

### Benefits of This Setup

1. No need to manually change code between environments
2. Configuration is centralized and maintainable
3. Environment-specific settings are clearly separated
4. Easy to add new environments (staging, testing, etc.)
5. Follows industry best practices for configuration management

## Database Persistence

### Docker Volume Management

The project uses Docker volumes to persist database data. Here's how it works:

1. **Data Persistence**:
   - Database data is stored in a Docker volume named `postgres_data`
   - This volume persists even when containers are removed
   - Data remains intact after `docker-compose down`

2. **Volume Management Commands**:
   ```bash
   # To see all volumes
   docker volume ls

   # To inspect the postgres_data volume
   docker volume inspect postgres_data

   # To remove the volume (WARNING: This will delete all data)
   docker volume rm postgres_data
   ```

3. **Common Scenarios**:
   - `docker-compose down`: Stops containers but preserves data
   - `docker-compose down -v`: Stops containers AND removes volumes (deletes data)
   - `docker-compose up --build`: Rebuilds containers but preserves data

4. **Backup and Restore**:
   ```bash
   # Backup database
   docker exec -t your-postgres-container pg_dump -U your-user your-database > backup.sql

   # Restore database
   cat backup.sql | docker exec -i your-postgres-container psql -U your-user your-database
   ```

### Best Practices

1. **Development**:
   - Use `docker-compose down` during development
   - Data persists between restarts
   - Helps maintain development state

2. **Production**:
   - Regularly backup the database
   - Use `docker-compose down -v` only when you want to reset the database
   - Consider using external volume mounts for better control

3. **Testing**:
   - Use `docker-compose down -v` to start with a clean database
   - Helps ensure tests start with known state

## Database Management

### pgAdmin Setup

The project includes pgAdmin for database management. Here's how to use it:

1. **Access pgAdmin**:
   - URL: http://localhost:5050
   - Default credentials:
     - Email: admin@admin.com
     - Password: admin

2. **Automatic Server Registration**:
   - The PostgreSQL server is automatically configured
   - No need to manually add the server
   - Configuration is stored in `pgadmin/servers.json`

3. **Server Details**:
   - Name: Banjara Backpacker DB
   - Host: postgres
   - Port: 5432
   - Database: banjara
   - Username: postgres
   - Password: (from your .env file)

4. **Persistent Configuration**:
   - pgAdmin data is stored in a Docker volume
   - Server configuration persists between restarts
   - No need to reconfigure after `docker-compose down`

## Local Development with Docker

### Option 1: Mixed Development (Recommended)
Run frontend and backend services locally while using Docker for database and pgAdmin.

1. Create a `docker-compose.dev.yml` file (already created above) with only database services:
   ```yaml
   # docker-compose.dev.yml
   version: '3.8'
   services:
     db:
       image: postgres:latest
       ports:
         - "5432:5432"
       environment:
         - POSTGRES_USER=${POSTGRES_USER}
         - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
         - POSTGRES_DB=${POSTGRES_DB}
       volumes:
         - postgres_data:/var/lib/postgresql/data
       networks:
         - banjaraBackpacker-network

     pgadmin:
       image: dpage/pgadmin4
       ports:
         - "8080:80"
       environment:
         - PGADMIN_DEFAULT_EMAIL=${PGADMIN_DEFAULT_EMAIL}
         - PGADMIN_DEFAULT_PASSWORD=${PGADMIN_DEFAULT_PASSWORD}
         - PGADMIN_SERVER_JSON_FILE=/pgadmin4/servers.json
       volumes:
         - ./pgadmin/servers.json:/pgadmin4/servers.json
         - pgadmin_data:/var/lib/pgadmin
       depends_on:
         - db
       networks:
         - banjaraBackpacker-network

   volumes:
     postgres_data:
     pgadmin_data:

   networks:
     banjaraBackpacker-network:
       driver: bridge
   ```

2. Start only the database services:
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

3. Run frontend and backend services locally:
   ```bash
   # Terminal 1 - Frontend
   cd frontendService
   npm install
   npm run dev

   # Terminal 2 - Auth Service
   cd authUser
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python run.py

   # Terminal 3 - Blog Service
   cd blogPostService
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python run.py
   ```

4. Update your `.env` files to use localhost:
   ```env
   # authUser/.env and blogPostService/.env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/banjaraBackpacker
   ```

   ```env
   # frontendService/.env
   VITE_AUTH_SERVICE_URL=http://localhost:5001
   VITE_BLOG_SERVICE_URL=http://localhost:5002
   ```

### Option 2: Full Docker Development

If you prefer to run everything in Docker:

1. **Create a Development Docker Compose**:
   ```yaml
   # docker-compose.dev.yml
   version: '3.8'
   services:
     frontend-service:
       build: 
         context: ./frontendService
         target: development
       ports:
         - "5173:5173"
       environment:
         - VITE_AUTH_SERVICE_URL=http://localhost:5001
         - VITE_BLOG_SERVICE_URL=http://localhost:5002
         - NODE_ENV=development
       volumes:
         - ./frontendService:/app
         - /app/node_modules
       command: npm run dev

     auth-service:
       build: 
         context: ./authUser
         target: development
       ports:
         - "5001:5001"
       environment:
         - FLASK_ENV=development
         - POSTGRES_HOST=db
       volumes:
         - ./authUser:/app
       command: flask run --host=0.0.0.0

     blog-service:
       build: 
         context: ./blogPostService
         target: development
       ports:
         - "5002:5002"
       environment:
         - FLASK_ENV=development
         - POSTGRES_HOST=db
       volumes:
         - ./blogPostService:/app
       command: flask run --host=0.0.0.0

     db:
       image: postgres:latest
       ports:
         - "5432:5432"
       environment:
         - POSTGRES_USER=${POSTGRES_USER}
         - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
         - POSTGRES_DB=${POSTGRES_DB}
       volumes:
         - postgres_data:/var/lib/postgresql/data

     pgadmin:
       image: dpage/pgadmin4
       ports:
         - "8080:80"
       environment:
         - PGADMIN_DEFAULT_EMAIL=${PGADMIN_DEFAULT_EMAIL}
         - PGADMIN_DEFAULT_PASSWORD=${PGADMIN_DEFAULT_PASSWORD}
         - PGADMIN_SERVER_JSON_FILE=/pgadmin4/servers.json
       volumes:
         - ./pgadmin/servers.json:/pgadmin4/servers.json
         - pgadmin_data:/var/lib/pgadmin
       depends_on:
         - db

   volumes:
     postgres_data:
     pgadmin_data:
   ```

2. **Start Development Environment**:
   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```

### Development Tips

1. **Hot Reloading**:
   - Frontend: Changes reflect immediately
   - Backend: Flask debug mode enabled
   - Database: Data persists between restarts

2. **Debugging**:
   - Use `docker-compose logs` to view service logs
   - Access pgAdmin at http://localhost:8080
   - Database accessible at localhost:5432

3. **Common Issues**:
   - If services can't connect to database, check POSTGRES_HOST
   - For frontend issues, check VITE_* environment variables
   - Ensure all required ports are available

4. **Best Practices**:
   - Use Option 1 for faster development cycles
   - Use Option 2 for consistent environment
   - Keep development and production configurations separate
   - Use volumes for persistent data