# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the frontend files into the Nginx document root
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Expose port 80 to make the frontend accessible
EXPOSE 80
