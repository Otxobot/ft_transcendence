# ft_transcendence

**ft_transcendence** is a multiplayer Pong platform that combines gaming and social interaction. It features real-time gameplay, user management, tournaments, and more, built with modern full-stack technologies.

---

## 🚀 Features
- 🎮 **Multiplayer Pong Game**: 4 and 2 player pong game.
- 🏆 **Tournaments**: Create and join tournaments.
- 👥 **User Management**: 
  - User profiles with customizable settings.
  - Add/remove friends via a friend request workflow.
  - View match history.
- 💬 **Live Chat**: Real-time messaging between users.
- 📊 **Monitoring**: Integrated Prometheus and Grafana for system metrics.

---

## 🛠️ Tech Stack
- **Frontend**: Angular  
- **Backend**: Django  
- **Database**: PostgreSQL  
- **DevOps**: Docker for containerization  
- **Monitoring**: Prometheus and Grafana  
- **Real-Time**: WebSocket technologies for live chat.

---
## Project Layout
```
.
├── backend
│   ├── accounts                # User management app
│   ├── django_debug.log         # Debug log file
│   ├── Dockerfile               # Dockerfile for backend container
│   ├── env_example              # Example environment variables file
│   ├── live_chat                # Live chat app
│   ├── manage.py                # Django management script
│   ├── media                    # Uploaded media files
│   ├── memo                     # Additional backend scripts or notes
│   ├── myproject                # Main Django project folder
│   ├── requirements.txt         # Backend Python dependencies
│   ├── run.sh                   # Script to run backend services
│   ├── static                   # Static files for the project
│   ├── templates                # HTML templates
│   └── two_factor_auth          # Two-factor authentication module
├── docker-compose.yml           # Docker Compose configuration
├── frontend
│   ├── Dockerfile               # Dockerfile for frontend container
│   ├── entrypoint.sh            # Entrypoint script for the frontend
│   └── pong-app                 # Frontend application files
├── grafana
│   ├── alert.rules.yml          # Alerting rules for Grafana
│   ├── config.yml               # Grafana configuration file
│   ├── dashboards               # Predefined Grafana dashboards
│   └── provisioning             # Provisioning setup for Grafana
├── Makefile                     # Build automation script
├── nginx
│   ├── Dockerfile               # Dockerfile for Nginx container
│   └── nginx.conf               # Nginx configuration
├── prometheus
│   └── alert.rules.yml          # Alerting rules for Prometheus
├── README.md                    # Project documentation (this file)
├── remote_pong
│   └── game_manager.py          # Remote Pong game manager script
├── TODO                         # List of tasks to complete
└── tree.txt                     # Output of the `tree` command
```

