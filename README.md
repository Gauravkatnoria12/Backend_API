# Backend_API

A FastAPI project for building scalable and high-performance backend applications.

## Overview

This is a FastAPI-based backend application designed to provide RESTful APIs with modern Python web development practices.

## Features

- 🚀 **FastAPI Framework** - Modern, fast, and easy to use web framework
- 📝 **Automatic API Documentation** - Interactive Swagger UI and ReDoc
- ⚡ **High Performance** - Built on Starlette and Pydantic for speed and validation
- 🔧 **Type Hints** - Full Python type hint support
- 🐍 **Python 100%** - Pure Python implementation

## Tech Stack

- **FastAPI** - Web framework
- **Python** - Programming language
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server

## Installation

### Prerequisites

- Python 3.7+
- pip or poetry

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Gauravkatnoria12/Backend_API.git
cd Backend_API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
Backend_API/
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── ...                 # Other project files
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/Gauravkatnoria12/Backend_API/issues).
