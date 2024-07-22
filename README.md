# GitHub Filler
> Want to look like a productive developer? I got you.

![GitHub release (latest by date)](https://img.shields.io/badge/release-v1.0.0-green)
![language (python)](https://img.shields.io/badge/language-python-blue)
![language (Bash)](https://img.shields.io/badge/language-Bash-green)
![license](https://img.shields.io/badge/license-GPL--3.0-yellow)

### What is GitHub-Filler?

GitHub Filler is a CLI tool based on the [Commitify](https://github.com/liamarguedas/Commitify) designed to generate fake commits over a specified date range, improving your GitHub contribution graph. It creates the appearance of consistent activity, helping to simulate a more productive developer profile.

### Before
![After](https://raw.githubusercontent.com/liamarguedas/GitHub-Filler/master/img/before.png)

### After
![Before](https://raw.githubusercontent.com/liamarguedas/GitHub-Filler/master/img/after.png)
___

## Get Stared

### 1. Pre-requisites:

Before you begin, you'll need to install the prerequisites:
- [Python 3.x](https://www.python.org/downloads/)
- Git installed and connected to your GitHub account.
- Create a new repository on GitHub. You can name it as you wish, but ensure it remains empty. Do not add any files, including `LICENSE` or `README.md`. Optional: Set it to private.
### 2. Clone GitHub-Filler:

- Clone the repository with the following commands:
     ```bash
     git clone https://github.com/liamarguedas/GitHub-Filler.git
     cd GitHub-Filler
     ```
### 3. Execute the tool
- Run the following command:
  ```bash
  python main.py
  ```
  
### 4. **Configuration**:
   - Upon running `main.py`, the CLI will prompt you for repository information and GitHub-Filler configuration.
   - You can set your own configuration or leave it blank to use the default settings.
     - **Repository URL**: Provide the URL of the GitHub repository you created earlier.
     - **Branch**: Specify the branch of the repository. If left blank, "master" will be used.
     - **Commits**: Enter the number of commits GitHub Filler will execute daily. Leaving this blank will result in a random number of commits each day.
     - **File**: Choose the file type to be added to the repository. Specify only the extension (e.g., `py`, `js`, `rs`) without the dot. If left blank, Python files (`py`) will be used by default.
     - **Starting date**: Specify a start date from which the tool will begin filling your contributions graph.
     - **Ending date**: Specify a end date from which the tool will stop filling your contributions graph.
       
     *Note: Date format should be **year, month, day** without leading zeros, example: 04/23/2024 should be provided as -> 2024, 4, 23*
     
     *Note: Providing the repository URL is mandatory.*

5. **Ready to Use**:
   - Once the configuration is complete, the tool will start populating your contribution graph.
   
**IMPORTANT**: Filling one entire year can take up to an hour, so if you've configured it to fill five years, it may take about five hours. Keep this in mind, as the     tool will be making time and calendar changes to your computer and you likely won't be able to use it while it's running.

With these steps completed, GitHub-Filler is set up and ready to demonstrate consistent activity on your GitHub Account.

## Platform Compatibility

- **Windows**: Fully supported and ready to use.
- **Linux / macOS**: Fully supported and ready to use.

## Donations

GitHub Filler is a freely available, open-source CLI Tool crafted during my limited free time. If you find value in the project and wish to contribute to its ongoing development, kindly consider making a small donation. Your support is genuinely appreciated!

[Donate with PayPal](https://www.paypal.me/ILIAMFTW)

## Contributors

<a href="https://github.com/liamarguedas/GitHub-Filler/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liamarguedas/GitHub-Filler" />
</a>

## License

GitHub-Filler was created by [Liam Arguedas](https://github.com/liamarguedas)
and is licensed under the [GPL-3.0 license](/LICENSE).
