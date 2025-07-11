# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TANUSHREE PATRA

*INTERN ID*: CT08DG608

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

*DESCRIPTION*: 

In this task, I developed a Python-based File Integrity Checker as part of my internship assignment. The objective was to build a simple tool that could monitor changes in files within a specified directory by generating and comparing their cryptographic hash values. This helps ensure the integrity of files and detect any unauthorized modifications.

To implement this, I wrote a script using Python 3.12 in Visual Studio Code, leveraging standard libraries such as os, hashlib, json, and argparse. The script recursively scans all files in the selected directory, calculates their SHA-256 hash values, and stores these values in a JSON file named file_hashes.json. On future runs, it compares the current hash values with the previously stored ones to detect any new, modified, or deleted files. If the --update flag is used, it updates the hash file with the latest state.

I tested the script on my local system by running it through the VS Code terminal. After navigating to the appropriate directory, I executed the script with the update flag, and it successfully scanned the folder and saved hash values. The output displayed in the terminal confirmed the operation with messages like “Scanning directory: .” and “Hash values updated and saved successfully.” I also verified the generation of the file_hashes.json file in the project folder.

As part of the submission, I saved the Python script, the output JSON file, and relevant screenshots showing the code and terminal output. These files were organized and uploaded to a GitHub repository for final review. The task not only helped reinforce my understanding of Python file handling and hashing but also introduced me to practical aspects of integrity verification — a foundational concept in cybersecurity.

*OUTPUT*: 

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/60b1f793-68c4-41b7-b88b-1bb531d861e0" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/f888f4d7-5068-41c7-8fe2-acc819ca937e" />

[Codetech CS & EH Task 1.pdf](https://github.com/user-attachments/files/21186404/Codetech.CS.EH.Task.1.pdf)
