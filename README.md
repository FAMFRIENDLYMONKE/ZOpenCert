# ZCertify 🏆

A robust platform for generating and managing verifiable digital badges and certificates using the Open Badges v2.0 specification.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

- **Digital Badge Issuance**: Create and issue verifiable digital badges
- **Secure Verification**: Each badge comes with a unique verification URL
- **Batch Processing**: Issue badges to multiple recipients at once
- **Email Integration**: Automatic email notifications to badge recipients
- **Admin Dashboard**: Manage and monitor badge issuance
- **API Authentication**: Secure endpoints with API key authentication
- **Cross-Origin Support**: Built-in CORS support for web integration

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MongoDB
- Node.js (for frontend)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FAMFRIENDLYMONKE/ZOpenCert.git
   cd ZOpenCert
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## 🛠 Tech Stack

- **Backend**: FastAPI + MongoDB
- **Authentication**: API Key Authentication
- **Email**: SMTP Integration
- **Standards**: Open Badges v2.0 Compliant

## 🔗 API Documentation

After running the server, visit:

- API Docs: https://localhost:8000/docs
- ReDoc: https://localhost:8000/redoc

## 🌐 Related Projects

- [Zairza-Cert-Issuer-Authority](https://github.com/zairza-cetb/Zairza-Cert-Authority-Profile): Certificate Generation Frontend
- [ZCertify Frontend](https://github.com/FAMFRIENDLYMONKE/ZCertify): Official Frontend Repository

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Authors

- **Initial work** - [FAMFRIENDLYMONKE](https://github.com/FAMFRIENDLYMONKE)

## 💖 Acknowledgments

- [Zairza](https://github.com/zairza-cetb) - The technical club of CET, Bhubaneswar
- [Open Badges](https://openbadges.org/) - For the badge standards specification
