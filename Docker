# Use Python 3.9 slim image
From python:3.9-slim
# Set working directory
WorkDir/ app
# Copy requirement first for better caching
COPY requirements.txt 
# Install dependency
RUN pip instal --no-cache-dir -r requirments.txt
COPY app.py
# Expose the port
EXPOSE 5000
# RUN the application
CMD ["python", "app.py"]
