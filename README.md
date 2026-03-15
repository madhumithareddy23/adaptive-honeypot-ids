# Adaptive Honeypot System for Network Intrusion Detection

This project simulates a honeypot-based intrusion detection system that monitors suspicious network activity and logs attacker behavior for analysis.

## Overview

Honeypots are security mechanisms designed to attract malicious attackers and study their behavior.  
This project creates a simulated environment where suspicious network activity is logged and analyzed.

## Features

- Simulated network traffic monitoring
- Honeypot service to capture suspicious requests
- Log generation for intrusion events
- Dashboard visualization of attack activity

## Tech Stack

Python  
HTML  
Log Monitoring

## Project Structure

controller_simple.py – Controls the honeypot monitoring process  
dashboard_writer.py – Generates dashboard output  
dataset_to_logs.py – Converts dataset events into log format  
fake_service.py – Simulates a vulnerable service for attackers  
stream_kdd.py – Streams dataset traffic for testing  
dashboard.html – Displays monitoring dashboard

## Dataset

This project uses the **NSL-KDD dataset**, a commonly used dataset for intrusion detection system research.

## Learning Outcome

Through this project, I explored how honeypot systems can be used to monitor attacker behavior and improve network security monitoring.
