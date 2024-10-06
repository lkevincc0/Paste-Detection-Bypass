
# Paste-Detection-Bypass

[English](#english) | [中文](#中文)

---

## English

### Project Description
The purpose of this project is to bypass the automatic paste detection (physically) of the code learning site, such as Grok Academy.

### Prerequisites
The key factor for success is to configure the environment correctly and turn off the auto-indentation in the editor.  
For example, for Grok Academy, you should go to settings and adjust the value for "Indent using space(s)" to `-1`.

### Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/lkevincc0/Paste-Detection-Bypass.git
    ```

2. Navigate into the project directory:

    ```bash
    cd Paste-Detection-Bypass
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Paste your code into the `code.txt` file.
2. Depending on your operating system, follow the relevant steps:

#### For Linux/macOS (using `run.sh`):
1. Execute the `run.sh` file:

    ```bash
    ./run.sh
    ```

#### For Windows:
1. Execute the `run.bat` file:

    ```cmd
    run.bat
    ```

Or, manually activate the environment and run the script:

```cmd
conda activate myenv
python main.py
```

### Then,
Move the mouse and click on the input box to complete the paste process.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 中文

### 项目描述
该项目的目的是绕过代码学习网站的自动粘贴检测（物理方式），例如 Grok Academy。

### 前提条件
成功的关键是正确配置环境，并关闭编辑器中的自动缩进功能。  
例如，对于 Grok Academy，您应进入设置并将 "Indent using space(s)" 的值调整为 `-1`。

### 安装

要安装必要的依赖，请按照以下步骤操作：

1. 克隆此仓库：

    ```bash
    git clone https://github.com/lkevincc0/Paste-Detection-Bypass.git
    ```

2. 进入项目目录：

    ```bash
    cd Paste-Detection-Bypass
    ```

3. 安装所需的 Python 包：

    ```bash
    pip install -r requirements.txt
    ```

### 使用方法
1. 将您的代码粘贴到 `code.txt` 文件中。
2. 根据您的操作系统，执行以下操作：

#### 对于 Linux/macOS (使用 `run.sh`):
1. 执行 `run.sh` 文件：

    ```bash
    ./run.sh
    ```

#### 对于 Windows:
1. 执行 `run.bat` 文件：

    ```cmd
    run.bat
    ```

或者手动激活环境并运行脚本：

```cmd
conda activate myenv
python main.py
```

### 然后，
移动鼠标并点击输入框以完成粘贴过程。

### 许可证
该项目根据 MIT 许可证授权 - 详情请参阅 [LICENSE](LICENSE) 文件。
