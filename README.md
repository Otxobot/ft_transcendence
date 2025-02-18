# ft_transcendence

**ft_transcendence** is a multiplayer Pong platform that combines gaming and social interaction. It features real-time gameplay, user management, tournaments, and more, built with modern full-stack technologies.

---

## 🚀 Features
- 🎮 **Multiplayer Pong Game**: Real-time gameplay with matchmaking and spectating options.
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
- **Real-Time**: WebSocket or similar technologies for live gameplay and chat.

---
## Project Layout
```
.
├── backend
│   ├── accounts
│   ├── django_debug.log
│   ├── Dockerfile
│   ├── env_example
│   ├── live_chat
│   ├── manage.py
│   ├── media
│   ├── memo
│   ├── myproject
│   ├── requirements.txt
│   ├── run.sh
│   ├── static
│   ├── templates
│   └── two_factor_auth
├── docker-compose.yml
├── frontend
│   ├── Dockerfile
│   ├── entrypoint.sh
│   └── pong-app
├── grafana
│   ├── alert.rules.yml
│   ├── config.yml
│   ├── dashboards
│   └── provisioning
├── Makefile
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── prometheus
│   └── alert.rules.yml
├── README.md
├── remote_pong
│   └── game_manager.py
├── TODO
└── tree.txt
```

