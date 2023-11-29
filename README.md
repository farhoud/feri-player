# FastAPI Translation API with Vue.js Frontend

This project combines a FastAPI API for text translation and a Vue.js frontend for a video player with subtitle selection and translation features.

## Features

- **Translation API Endpoint:** Provides a RESTful API endpoint for translating text using the facebook/mbart-large-50-many-to-many-mmt model.
- **Vue.js Video Player:** A frontend application built with Vue.js that includes a video player with subtitle selection and translation features.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python (version 3.7 or later)
- Pipenv (optional, but recommended for managing dependencies)
- Node.js and npm (for Vue.js frontend)

### Installation

#### Backend (FastAPI)

1. Clone the repository:

    ```bash
    git clone https://github.com/farhoud/feri-player.git
    ```

2. Navigate to the project directory:

    ```bash
    cd feri-player
    ```

3. Install dependencies:

    ```bash
    pipenv install
    ```

4. Run the FastAPI app:

    ```bash
    cd back
    pipenv run uvicorn main:app --reload
    ```

#### Frontend (Vue.js)

1. Navigate to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install dependencies:

    ```bash
    yarn install
    ```

3. Run the Vue.js app:

    ```bash
    yarn dev
    ```

The API should now be running locally at `http://127.0.0.1:8000`, and the Vue.js app at `http://localhost:8080`.

## API Usage

### Translate Endpoint

- **Endpoint:** `/translate/{text}`
- **Method:** GET
- **Example:** [http://127.0.0.1:8000/translate/Hello](http://127.0.0.1:8000/translate/Hello)

## Vue.js Frontend Features

- **Video Player:** The frontend includes a video player with playback controls.
- **Subtitle Selection:** Users can select subtitles for the video.
- **Translation Feature:** Translation of selected subtitles using the FastAPI Translation API.

## Built With

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/) - FastAPI web framework.
  - [Hugging Face Transformers](https://huggingface.co/transformers/) - State-of-the-art natural language processing models.

- **Frontend:**
  - [Vue.js](https://vuejs.org/) - Vue.js framework for building user interfaces.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc.

