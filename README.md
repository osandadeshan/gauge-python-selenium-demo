# Gauge example project, in Python [![Build Status](https://snap-ci.com/kashishm/gauge-example-python/branch/master/build_image)](https://snap-ci.com/kashishm/gauge-example-python/branch/master)

This project serves as an example for writing Automation using [Gauge](https://github.com/getgauge/gauge)

This project uses 

- [Selenium](http://selenium-python.readthedocs.org/)
- Snap CI has been setup to run the Gauge Specs from this project.

# Concepts covered

- Use [Webdriver](http://docs.seleniumhq.org/projects/webdriver/) as base of implementation
- [Concepts](http://getgauge.io/documentation/user/current/specifications/concepts.html)
- [Specification](http://getgauge.io/documentation/user/current/gauge_terminologies/specifications.html), [Scenario](http://getgauge.io/documentation/user/current/specifications/scenarios.html) & [Step](http://getgauge.io/documentation/user/current/specifications/steps.html) usage
- [Table driven execution](http://getgauge.io/documentation/user/current/execution/table_driven_execution.html)
- [External datasource (special param)](http://getgauge.io/documentation/user/current/specifications/parameters.html#special-parameters)

# Prerequisites
- Python 3
- [Java 1.7](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). [Required to bring up the [SUT](#setting-up-the-system-under-test-sut)
- [Install Gauge](http://getgauge.io/download.html)
  - Homebrew on Mac OS X :  
      ```
      brew install gauge
      ```
  - [Download Installer](http://getgauge.io/download.html)
- [Install Gauge-Python plugin](https://gauge-python.readthedocs.io/en/latest/installation.html) by running<br>
```
gauge --install python
[pip / pip3] install getgauge
```
- Google Chrome

## Setting up the System Under Test (SUT)

* Download [activeadmin-demo.war](https://bintray.com/artifact/download/gauge/activeadmin-demo/activeadmin-demo.war)
* Bring up the SUT by executing the below command
```
java -jar activeadmin-demo.war
```
* The SUT should now be available at [http://localhost:8080/](http://localhost:8080)


# Executing specs

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
gauge specs
````
This will also compile all the supporting code implementations.
