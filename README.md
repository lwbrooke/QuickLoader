# QuickLoader

QuickLoader is a simple Python application that allows you to load files quickly. It is designed to write files to the D:\ drive, and can automatically retry writing the file if the drive disappears and then reappears. QuickLoader also includes notifications to let you know when the file has been written to the drive, when no file is selected, and when no drive is detected.

## Installation

To install QuickLoader on your Windows computer, simply download the QuickLoader.exe file and double-click it to run the application. No additional installation steps are necessary.

## Usage

To use QuickLoader, simply launch the application and select a file to load by clicking the "Load File" button and using the file dialogue to select a file. QuickLoader allows you to select a single file at a time.

Once a file has been selected, QuickLoader will write it to the D:\ drive. If the drive disappears and then reappears, QuickLoader will automatically write the file to the drive again.

QuickLoader will notify you when the file has been written to the drive, as well as when no file is selected and when no drive is detected. This ensures that you always know the status of the file loading process.

## Development

To develop QuickLoader further, simply clone this repository and install the required dependencies by running:

```sh
pip install -r requirements.txt
```

To build a new executable for QuickLoader using PyInstaller, run:

```sh
pyinstaller --onefile --windowed quickloader.py
```

This will create a new QuickLoader.exe file in the dist directory.

## Troubleshooting

If you encounter any issues while using QuickLoader, please try the following steps:

1. Ensure that the D:\ drive is connected and accessible.
2. Check that the file you are trying to load is a valid file and can be opened.
3. Restart QuickLoader and try loading the file again.

If the issue persists, please submit a bug report to the QuickLoader GitHub repository.

## Credits

QuickLoader was created by Logan Brooke and is released under the MIT License. The inital README was generated using ChatGPT, and then tweaked from there.