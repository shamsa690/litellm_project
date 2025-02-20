# litellm_project

ProjectCrew: Automated Blog Topic Generation

Overview

ProjectCrew is an AI-powered automation that generates blog topics using CrewAI's Flow framework and litellm for AI model integration. It utilizes gemini-1.5-flash to generate blog topics about Agentic AI.

Features

Uses Google's gemini-1.5-flash model for topic generation.

Implements CrewAI's Flow framework to structure the process.

Uses dotenv for environment variable management.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.8+

pip (Python package manager)

Setup

Clone the repository:

git clone https://github.com/your-repo/projectcrew.git
cd projectcrew

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory.

Add the required API keys (e.g., LITELLM_API_KEY).

Usage

Run the script to generate a blog topic:

python main.py

File Structure

projectcrew/
│── flow.py        # Main Flow class
│── main.py        # Entry point to kick off the process
│── .env           # Environment variables
│── README.md      # Project documentation
│── requirements.txt # Required dependencies

Troubleshooting

If you encounter issues:

Ensure API keys are correctly set in the .env file.

Check dependencies with pip freeze.

Verify Python version compatibility.

License

This project is licensed under the MIT License.
