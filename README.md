# Story Arc Extractor

This repository contains tools for extracting and analyzing story arcs from TV show transcripts using language models.

## Installation

To set up the project environment, follow these steps:

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory of the project with your Anthropic and OpenAI API keys:

```plaintext
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_anthropic_api_key_here` and `your_openai_api_key_here` with your actual API keys.

## Notebooks

- `story_arc.ipynb`: This Jupyter notebook contains the code for processing transcripts and extracting story arcs using the Anthropic API. It demonstrates how to read transcripts, send requests to the API, and parse the responses into structured data.

- `prompt_eval.ipynb`: This notebook is used for evaluating different prompts and their effectiveness in extracting desired information from the language model. It's useful for fine-tuning prompts to improve the quality of the model's responses.

Note : This notebook requires an OpenAI API key to run.

## Usage

To use the notebooks, ensure you have Jupyter installed and run:

```bash
jupyter notebook
```

Navigate to the `story_arc.ipynb` or `prompt_eval.ipynb` file and execute the cells in sequence.

## Contributing

Contributions to this project are welcome. Please open an issue to discuss proposed changes or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.