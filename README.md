# Patient-Centric Question Answering System in collaboration with IBM Research

Hello and welcome to our project for the Software Engineering Project module in Trinity College Dublin. We are Group 11 and we are working together with IBM Research to improve analysation of clinical trial results in an attempt to help with solving important healthcare problems.

## Our Goal

We aim to create a web application that is a dashboard which allows users to interact with data in an intuitive way. Users will be able to interact with the data using Natural Language, specifying what they wish to extract from the data for example "Sort patients with diabetes by height", as opposed to other, time-consuming methods of trawling through data. They will then be presented with visualisations of this which will help with data analysis and they will also be able to download the extracted data in a human readable file.

## Data We Used

We are using public synthetic patient data made using Synthea. The specific file we use is the observations.csv file which can be found [here](https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip).

A link to the website hosting the data, SyntheticMass, can be found [here](https://synthea.mitre.org/).

## Prerequisites

* Docker installed on system
* Clone this repository to your local machine or download the latest release 

## How To Run

For ease of use Dockerfiles have been provided to run the program on localhost. You can decide to either manually run the docker files to your own preference or use the provided shell scripts for windows and unix to automatically run the required commands.

To use the shell scripts, just execute them from terminal in the repository's root folder. Once the script completes navigate to localhost:3000 in a browser to run.  

Once the program is running, you should see our homepage which looks like this:
<img width="1439" alt="Homepage screenshot" src="https://user-images.githubusercontent.com/72447771/232018318-ceb3379c-8315-4b37-9c04-7156ea3459af.png">

Here you can navigate to one of the additional pages found on the navigation bar or enter a query into the search bar.

Here are some examples of queries that you can enter:

* Give me the maximum weight of patients with heart rate less than 70.
* Show the cholesterol of patients with a weight greater than 80.
* Give me the mean blood pressure of patients with cloudy urine.
* What is the minimum heart rate of patients with a blood pressure greater than 120?

Once you have typed in a query, hit the enter button on your keyboard and then press the two buttons to update the cards and the graphs. 
<img width="136" alt="Buttons" src="https://user-images.githubusercontent.com/72447771/232018894-de9d67c6-0c39-43f8-bff1-6833a1080cf9.png">

The page will then display your results like so.
<img width="1437" alt="Results" src="https://user-images.githubusercontent.com/72447771/232019775-9bb5026d-b0a0-4bf8-bc83-ec7d13118d53.png">

You can download the data returned in a CSV file using the download CSV button at the search bar or enter a new query repeating the same process as before.

<img width="359" alt="Download CSV button" src="https://user-images.githubusercontent.com/72447771/232019809-8743f07d-2900-42d2-aab3-6ee6609ca2cd.png">

## Members of the Team
| Name                  | Year        | Course                        |
| :---                  |    :----:   | :---                          |
| Austeja Pakulyte      | 3rd Year    | Computer Science              |
| Constantin Pusch      | 3rd Year    | Computer Science & Business   |
| Kevin Morley          | 3rd Year    | Computer Science              |
| Andrew Furey          | 2nd Year    | Computer Science              |
| Anthony Oisin Gavril  | 2nd Year    | Computer Science              |
| Isobel Radford-Dodd   | 2nd Year    | Computer Science & Business   |
| Luke Barry            | 2nd Year    | Computer Science & Business   |
| Minghim Foun          | 2nd Year    | Computer Science              |
| Samuel Forster        | 2nd Year    | Computer Science              |


