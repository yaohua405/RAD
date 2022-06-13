# Application
Ransomware Anomaly Detection project for the Capstone 1, Capstone 2, and senior project sections of Florida International University Spring 2022

Capstone 2 students:
  Bryan Simmons
  Alwahab Mohammad
  Sebastian Duenas
  Daniel Riquelme Rebollar
 
Capstone 1 students:
  Blake Prieto
  Ivan Rosyaykin
  Ricardo Tacconi
  
Senior Project students:
  Ian Agrela De Freites
  Yaohua Hu
  Brendan Wojtczak

File structure:
- Trained models - Contains models that were trainined using four different 
    thresholds: 0.8, 0.85, 0.9, and 0.95.
    Trained models should only be used for testing. New models should be created on the device the application is running on.
- RAD.py - The primary driver code for the application. Use "python RAD.py -h" to 
    see usage
- DataStructureDefinition.py - Pulls in the Sysmon Archive logs, parses them, and
    passes the data to the algorithm for analysis
- DissimilarityAlgorithm.py - Analyzes the Sysmon Archive log events and, if the option 
    is selected, returns a prediction of whether each event is considered an
    anomaly.
- KeyValues.py - Contains a definition for which attributes of each Event ID are 
    considered relevant. This can be modified to include or exclude attributes for fine-tuning the algorithm.
- SysmonConfig - Contains the executable, configuration, and instructions for 
    setting up the Sysmon application for creating logs to be parsed using the 
    application.

Installation guide:
1. Install Sysmon using instructions in SysmonConfig > Sysmon_Instructions.pdf
2. Train model on Sysmon Archive files using 'python RAD.py'
3. Generate predictions using 'python RAD.py -p'

note - If program is not run as admin it will request admin rights and run in a new window

Program usage: 
  -i (input path) -> Use provided log location instead of default
  -p              -> Return a prediction of the events analyzed
  -s              -> Do not delete log files after analyzing them
  -f (input file) -> Only analyze the file given
  -a              -> Analyze all logs files in the target folder (not recommended)
