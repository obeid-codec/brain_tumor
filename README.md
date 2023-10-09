# Brain Tumor Classification

This project utilizes machine learning and convolutional neural networks (CNNs) to classify brain tumors based on MRI images. After running the project, users can access a web page where they can upload an MRI brain picture and click the "Predict" button. The system will then provide a prediction of the type of brain tumor along with its accuracy score.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Method 1: Manual Installation](#method-1-manual-installation)
  - [Method 2: Docker Installation](#method-2-docker-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your system.
- Works on all major platforms.

## Installation

There are two ways to install and run this project.

### Method 1: Manual Installation

1. Clone or download the project repository.
2. Upload the files inside the `api` folder and the `docker-compose.yml` file to your host server.
   - Your directory structure should look like this:
     ```
     - docker-compose.yml
     - api/
     ```
3. Open a terminal and navigate to the directory containing `docker-compose.yml`.
4. Build the Docker containers:
   ```bash
   docker-compose build
```
5. Start the application in the background:
   ```bash
   docker-compose up -d
```
The application will be accessible on port 80 by default.

### Method 2: Docker Installation

To install and run the application using Docker, follow these steps:

1. Upload the `docker-compose.prod.yml` file to your host server if you haven't already.

2. Open a terminal and navigate to the directory containing `docker-compose.prod.yml`.

3. Pull the required Docker images:

   ```bash
   docker-compose -f docker-compose.prod.yml pull
 ```
 
3. Start the application in the background:

   ```bash
   docker-compose -f docker-compose.prod.yml up -d
 ```
 
The application will be accessible on port 80 by default.

### Usage
Provide instructions on how to use your application or any additional setup/configuration that may be required. Include examples if necessary.

### Configuration
Explain how users can configure your application, including environment variables, configuration files, or any other customization options.

### Contributing
Explain how others can contribute to your project. Include guidelines for reporting issues, making pull requests, and any coding standards you may have.