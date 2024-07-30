FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY app.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
