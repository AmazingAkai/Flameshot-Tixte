# Flameshot-Tixte

Flameshot-Tixte is a script that allows you to upload screenshots taken with Flameshot to the Tixte image hosting service. This script has only been tested on Linux, and there is no guarantee that it will work on Windows or macOS.

## Prerequisites

Before using the Flameshot-Tixte script, you need to perform the following steps:

1. Clone the Flameshot-Tixte repository by running the following command in your terminal:

```bash
git clone https://github.com/AmazingAkai/Flameshot-Tixte
```

2. Install a copy-paste mechanism like xclip, as it is required by the pyperclip library. You can find instructions on how to install xclip [here](https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error).

3. Navigate to the Flameshot-Tixte directory:

```bash
cd Flameshot-Tixte
```

4. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

5. Create a `config.json` file in the Flameshot-Tixte directory with the following contents:

```json
{
  "authorization": "YOUR_AUTHORIZATION_KEY",
  "domain": "YOUR_DOMAIN"
}
```

Replace **YOUR_AUTHORIZATION_KEY** with your Tixte authorization key, and \*\*YOUR_DOMAIN with your desired domain on Tixte.

6. Install Flameshot if you haven't already. You can install Flameshot using your package manager.

# Usage

To use Flameshot-Tixte, follow these steps:

- Capture a screenshot using Flameshot. Use the Flameshot graphical interface or assign a shortcut key for the Flameshot screenshot tool.

- Run the following command in your terminal to upload the screenshot to Tixte using Flameshot-Tixte:

```bash
flameshot gui -r | python path/to/Flameshot-Tixte/main.py
```

- Replace `path/to/Flameshot-Tixte` with the actual path to the Flameshot-Tixte directory.

- Flameshot-Tixte will attempt to upload the screenshot to Tixte. If the upload is successful, the direct URL of the uploaded image will be copied to your clipboard, and a notification will be displayed indicating the successful upload.

- If the upload fails, a notification will be displayed indicating the failure.

# Shortcut Key

- You can create a shortcut key to execute the Flameshot-Tixte command. Set up a custom shortcut in your desktop environment's settings and assign the following command:

```bash
flameshot gui -r | python path/to/Flameshot-Tixte/main.py
```

- Remember to replace path/to/Flameshot-Tixte with the actual path to the Flameshot-Tixte directory.
