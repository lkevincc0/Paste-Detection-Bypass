# Paste-Detection-Bypass

The purpose of this project is to bypass the automatic paste detection (physically) of the code learning site, such as grok academy...

## Prerequisites
The key factor for success is to configure the environment correctly and turn off the auto-indentation in the editor.
For example, as to Grok Academy, you should enter setting and adjust the value Indent using space(s), type '-1'.

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

    ```bash
    git clone git@github.com:lkevincc0/Paste-Detection-Bypass.git
    ```

2. Navigate into the project directory:

    ```bash
    cd Paste-Detection-Bypass
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### For Linux/macOS (using `run.sh`):
1. Execute the `run.sh` file:

    ```bash
    ./run.sh
    ```

### For Windows:
1. Execute the `run.bat` file:

    ```cmd
    run.bat
    ```

Or, manually activate the environment and run the script:

```cmd
conda activate myenv
python main.py

