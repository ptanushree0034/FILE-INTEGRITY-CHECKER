# FILE-INTEGRITY-CHECKER

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: TANUSHREE PATRA

*INTREN ID*: CT08DG608

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

*TASK DESCRIPTION*: In today's digital world, maintaining data integrity is critical, especially in cybersecurity, where even the slightest modification of a file could indicate a security breach. This task involves developing a File Integrity Checker — a Python-based tool that monitors files for unauthorized changes by calculating and comparing their cryptographic hash values.

The primary objective of this task is to create a lightweight script using Python and its standard libraries (particularly hashlib, os, json, and argparse) to monitor the integrity of files in a specified directory. The tool ensures that no changes go undetected, which is essential for both security auditing and system reliability. File integrity monitoring is widely used in industries to detect tampering, malware injection, or accidental data corruption.

The tool works on a simple yet powerful principle: hashing. A hash function takes a file as input and produces a fixed-length alphanumeric value called a hash or checksum. If even a single byte in the file changes, the resulting hash will change drastically. This property allows us to detect whether a file has been altered.

The File Integrity Checker script begins by scanning all files in the target directory and computing their SHA-256 hashes — a cryptographically secure algorithm that ensures strong resistance to collisions and tampering. The hash values are stored in a local JSON file (file_hashes.json), which acts as a baseline or reference.

Later, when the tool is run again, it re-computes the hash values of the current files and compares them with the stored ones. The comparison detects:

New Files: Files that were added after the initial scan.

Modified Files: Files whose current hash doesn't match the previously stored hash.

Deleted Files: Files that were previously recorded but are now missing.

The script also provides an option to update the stored hashes if the current file state is verified and needs to be treated as the new baseline. This is useful for maintaining up-to-date records after legitimate changes.

This solution is implemented in a modular, user-friendly way. It accepts command-line arguments for the directory path and whether to update the hash records, making it suitable for integration into automated monitoring systems or cron jobs.

The tool enhances cybersecurity and system monitoring by offering an easy yet effective way to track changes to critical files. It can be particularly helpful for detecting unauthorized changes in configuration files, system logs, scripts, or any sensitive files that should remain unaltered unless explicitly modified by an authorized user.

In summary, this task delivers a practical solution to file integrity monitoring, applying core concepts of cryptography and system security using Python. It reflects how simple tools can play a major role in identifying unauthorized access, malware activity, or accidental changes, making it highly relevant in cybersecurity, system administration, and compliance auditing.
