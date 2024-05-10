# MobileSAM FastAPI Service

Welcome to the MobileSAM FastAPI Service! This service provides an API endpoint for segmenting images using the MobileSAM model.

## Setup

To set up the project environment, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/garima5270/mobilesam-fastapi.git
   ```
   
2. **Navigate to the Project Directory:** Change your current directory to the project directory:

   ```bash
   cd mobilesam-fastapi
   ```
   
3. **Install Dependencies:** Install the required Python dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
   
## To run the FastAPI service, follow these steps:
   
1. **Start the Service:** Run the following command to start the FastAPI service:
   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```
   
2. **Access the Service:** Once the service is running, you can access it at http://127.0.0.1:8000.

## Interacting with the Service

   You can interact with the service using HTTP requests. Here are some examples:
   
1. **Segment an Image:** You can segment an image by sending a POST request to the /segment-image endpoint with the image file attached as form data. Here's a sample cURL command:

   ```bash
   curl -X POST -F "file=@/path/to/your/image.jpg" http://127.0.0.1:8000/segment-image
   ```
   
2. **Swagger Documentation:** Explore the API endpoints and interact with them using the Swagger UI. Access the Swagger documentation at http://127.0.0.1:8000/docs.

## Docker Support

   To run the service inside a Docker container, follow these steps:
   
1. **Build the Docker Image:** Build the Docker image using the provided Dockerfile. Run the following command in the project directory:

   ```bash
   docker build -t mobilesam-fastapi .
   ```
   
2. **Run the Docker Container:** After building the Docker image, run the Docker container using the following command:

   ```bash
   docker run -p 8000:8000 mobilesam-fastapi
   ```

## License

This project is licensed under the MIT License.
