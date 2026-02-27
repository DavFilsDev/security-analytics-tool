# Security Analytics Tool 🔒

A progressive Python project evolving from a simple calculator into a comprehensive security analytics platform. Built for learning Python while creating practical cybersecurity tools.

## 🎯 Project Vision

Transform a basic calculator into an AI-enhanced security analytics tool that demonstrates real-world Python applications in cybersecurity. Each phase introduces new concepts while building upon previous knowledge.

## 📚 Learning Path & Implementation Phases

### Phase 0: Foundation - Core Calculator
**Goal:** Master basic Python syntax, functions, and error handling

```python
# Simple calculator operations as the foundation
- Basic arithmetic operations (add, subtract, multiply, divide)
- Type hints and docstrings
- Basic error handling
```

### Phase 1: Enhanced Math Operations
**Goal:** Add mathematical functions relevant to security/cryptography

```python
# Security-related math utilities
- Power and modulus operations
- Binary XOR for crypto basics
- Prime number checking
- Greatest Common Divisor (GCD) for RSA foundation
```

### Phase 2: Password Security Module
**Goal:** Build practical security tools with string manipulation

```python
# Password analysis and generation
- Password strength checker with scoring
- Password entropy calculator
- Random password generator
- Common password detector
```

### Phase 3: Network Utilities
**Goal:** Learn socket programming and network concepts

```python
# Network scanning and analysis
- Port scanner with service detection
- IP address validator
- Subnet calculator
- Simple bandwidth calculator
```

### Phase 4: Cryptography Basics
**Goal:** Understand encryption fundamentals

```python
# Classical and modern crypto
- Caesar cipher (encrypt/decrypt)
- Vigenère cipher
- Base64 encoder/decoder
- Simple hash functions
- XOR cipher
```

### Phase 5: Log Analysis
**Goal:** File I/O and data processing

```python
# Security log analysis
- SSH failed login detector
- Log file parser
- Attack pattern recognition
- Report generator (CSV/JSON)
- Log statistics calculator
```

### Phase 6: Data Visualization
**Goal:** Create visual representations of security data

```python
# Visual analytics
- Attack timeline graphs
- Password strength distribution charts
- Network traffic plots
- Heat maps for attack sources
```

### Phase 7: Anomaly Detection
**Goal:** Introduction to AI/ML concepts

```python
# Statistical anomaly detection
- Traffic baseline calculator
- Z-score anomaly detector
- Moving average for trends
- Simple threshold alerts
- Confidence scoring
```

### Phase 8: Simple Malware Detection
**Goal:** Basic ML implementation

```python
# Heuristic-based detection
- File entropy calculator
- Suspicious API call detector
- Simple weighted scoring system
- Probability calculator (sigmoid)
- Detection report generator
```

### Phase 9: API Development
**Goal:** Create web interface for tools

```python
# REST API with Flask/FastAPI
- API endpoints for all tools
- Authentication middleware
- Request rate limiting
- API documentation (Swagger)
- Docker containerization
```

### Phase 10: Advanced Features
**Goal:** Production-ready enhancements

```python
# Professional features
- Database integration (SQLite/PostgreSQL)
- User management system
- Job scheduling for scans
- Email alerts
- Web dashboard
- Performance optimization
- Comprehensive test coverage
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/DavFilsDev/security-analytics-tool.git
cd security-analytics-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (as we add them)
pip install -r requirements.txt
```

### Basic Usage
```python
from src.core.operations import add, subtract
from src.security.password_checker import check_password_strength

# Start with basic calculator
result = add(10, 5)
print(f"10 + 5 = {result}")

# Then try password checking
password_analysis = check_password_strength("MySecureP@ss123")
print(f"Password strength: {password_analysis['strength']}")
```

## 📁 Project Structure
```
security-analytics-tool/
├── src/
│   ├── core/           # Basic operations (Phase 0-1)
│   ├── security/       # Password tools (Phase 2)
│   ├── network/        # Network utilities (Phase 3)
│   ├── crypto/         # Encryption (Phase 4)
│   ├── logs/           # Log analysis (Phase 5)
│   ├── viz/            # Visualization (Phase 6)
│   ├── ai/             # Anomaly detection (Phase 7-8)
│   └── api/            # Web interface (Phase 9-10)
├── tests/              # Unit tests
├── data/               # Sample data and logs
├── docs/               # Documentation
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## ✅ Progress Tracking

- [x] Phase 1: Enhanced Math Operations
- [ ] Phase 2: Password Security
- [ ] Phase 3: Network Utilities
- [ ] Phase 4: Cryptography Basics
- [ ] Phase 5: Log Analysis
- [ ] Phase 6: Data Visualization
- [ ] Phase 7: Anomaly Detection
- [ ] Phase 8: Malware Detection
- [ ] Phase 9: API Development
- [ ] Phase 10: Advanced Features

## 🤝 Contributing
Perfect for learning! Each phase builds on the previous. Start with Phase 0 and work your way up.

## 📝 License
MIT License - feel free to use for learning!

## ⭐ Success Metrics
- Complete all 10 phases
- 90%+ test coverage
- Working API with documentation
- Real security insights from your tools