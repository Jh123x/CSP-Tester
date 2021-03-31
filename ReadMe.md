# CSP Tester

Test your Content-Security-Policy using this simple python application to check if a `.html` page renders correctly given a certain Content Security Policy
The original repo can be found [here](https://github.com/Jh123x/CSP-Tester)

## What is the point of using Content-Security-Policies in your headers?

The use of Content Security Policy Serves as a very good counter measure to Cross-Site-Scripting.
You can learn more about Cross Site Scripting [here](https://github.com/Jh123x/xss-demo).

Content Security Policy allows your browser to restrict the running of different javascript which is received by the client. Some of which might be malicious.

For more information on Content Security Policy, you can visit [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

## Quick start

1. Clone the application to a directory
1. Run the `server.py` file

The default index_page will be run and you can visit your page at [http://localhost:3000](http://localhost:3000)

Check your console to see which javascript has been executed.

## Config file information

| Option | Description                                      | Possible values             | Remarks                                                                                                                                            |
| ------ | ------------------------------------------------ | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| https  | Loads the webpage in HTTP or HTTPS               | True or False               | Decides if the webpage is rendered in HTTP or HTTPS. In the case of HTTPS, the certificate will be automatically generated and will be self signed |
| host   | The host to be hosted on                         | localhost or other domains  | It will be localhost by default. You can also set it to 0.0.0.0 to make it discoverable at the ip address of the machine to your local network     |
| port   | Port that the website is listening on            | Integer between 1 and 65535 | Some operating systems block lower number ports so take that into account when choosing a port. The default port value is 3000                     |
| debug  | Debug mode                                       | True or false               | False by default. This decides if the flask server runs in debug mode or note                                                                      |
| csp    | The Content Security Policy that you want to set | Any valid CSP value         | The CSP will be appended to the header of the reponses which are sent to the client.                                                               |

# Additional information

Some useful tools

### [CSPScanner](https://cspscanner.com/)

A tool to scan and rate the CSP of your domain
<br>

### [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/)

CSP Evaluator allows developers and security experts to check if a Content Security Policy (CSP). Also provides sample safe and unsafe Content-Security-Policies
<br>

## Tech stack

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
1. [Configparser](https://docs.python.org/3/library/configparser.html)
