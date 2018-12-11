# Gauge Python Selenium Example Project

This project serves as an example for writing Automation using [Gauge.](https://docs.gauge.org/latest/installation.html)

This project uses: 
- [Selenium](http://selenium-python.readthedocs.org/)
- Snap CI has been setup to run the Gauge Specs from this project.
<br />

# Concepts Covered

- Use [Webdriver](http://docs.seleniumhq.org/projects/webdriver/) as base of implementation
- [Concepts](http://getgauge.io/documentation/user/current/specifications/concepts.html)
- [Specification](http://getgauge.io/documentation/user/current/gauge_terminologies/specifications.html), [Scenario](http://getgauge.io/documentation/user/current/specifications/scenarios.html) & [Step](http://getgauge.io/documentation/user/current/specifications/steps.html) usage
- [Table driven execution](http://getgauge.io/documentation/user/current/execution/table_driven_execution.html)
- [External datasource (special param)](http://getgauge.io/documentation/user/current/specifications/parameters.html#special-parameters)
<br />

## Pre Requisites

- [Python 3](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe)
- [Install Gauge](https://docs.gauge.org/latest/installation.html) \
    **On Windows**
    1. Install Chocolatey by executing the following command. \
    ` @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString(‘https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

    2. Install Gauge by executing the following command. \
    `choco install gauge`

    **On MacOS**
    1. Update Homebrew. \
    `brew update`

    2. Install Gauge using Homebrew. \
    `brew install gauge`

    **On Linux**
    1. First, add Gauge’s GPG key with this command. \
    `sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B`

    2. Then add Gauge to the repository list using this command. \
    `echo deb https://dl.bintray.com/gauge/gauge-deb nightly main | sudo tee -a /etc/apt/sources.list`

    3. Finally, install Gauge using these commands. \
    `sudo apt-get update` \
    `sudo apt-get install gauge`

    - Open Command Prompt and execute following commands. \
    `[pip / pip3] install getgauge` \
    `gauge install python` \
    `gauge install html-report` \
    `gauge install json-report` \
    `gauge install xml-report` \
    `gauge install spectacle` \
    `gauge install flash`

    - You can check the installation using the following command. \
    `gauge -v`

      If the installation is success, it will output like this:

    ```markdown
        Gauge version: <version number>
        Plugins
        -------
        flash (<version number>)
        html-report (<version number>)
        python (<version number>)
        json-report (<version number>)
        spectacle (<version number>)
        xml-report (<version number>)
    ```
<br />

## Executing specs

### Set up
This project requires pip to install dependencies. To install dependencies run :  
````
pip install -r requirements.txt
````

Run the following command to install chromedriver, if it fails then download it from [here](http://chromedriver.storage.googleapis.com/index.html) and add it to the `PATH` variable.

```
[pip / pip3] install chromedriver_installer
```

### All specs
````
gauge run specs
````
This will also compile all the supporting code implementations.
