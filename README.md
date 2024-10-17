# 🚗Carpooling Application

## Overview

This is a web-based carpooling application developed using Flask, designed to facilitate ride sharing between drivers and riders. The application allows users to offer and request rides, manage scheduled rides, and communicate in real-time through a chat feature. It includes functionalities for ride acceptance, cancellations, user management, and reporting.

## Features

- **User Registration & Authentication**: Users can register as drivers or riders, manage their profiles, and log in.
- **Ride Management**: 
  - Drivers can offer rides, schedule them, and manage availability.
  - Riders can request rides, accept offers, and cancel requests.
- **Real-Time Communication**: Utilizes WebSocket (Socket.IO) for real-time messaging between users.
- **Reporting System**: Users can submit reports against other users.
- **User Management**: Admin features for activating, suspending, or banning users.
- **Scheduled Rides**: Users can request or offer recurring rides based on specific patterns.

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite (with SQLAlchemy ORM)
- **WebSocket**: Flask-SocketIO
- **Frontend**: HTML, CSS (Bootstrap for styling)

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- SQLite
