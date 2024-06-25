HTTP Request Analyst

## Overview

The HTTP Request Analyst is a Python-based tool designed to analyze HTTP requests. This tool captures and parses HTTP request data, providing detailed insights and metrics that are useful for debugging, performance analysis, and security auditing.

## Features

- Capture HTTP requests in real-time.
- Parse and analyze HTTP request headers, methods, URLs, and payloads.
- Generate detailed reports on captured HTTP requests.
- Supports filtering and searching through captured data.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- `requests` library
- `Flask` library (if capturing via a proxy server)
- `scapy` library (if capturing via packet sniffing)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/HTTP-Request-Analyst-.git
    cd http-request-analyst
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Capture HTTP requests via a proxy server:
    ```bash
    python http_request_analyst.py --mode proxy --host <host> --port <port>
    ```

2. Capture HTTP requests via packet sniffing:
    ```bash
    python http_request_analyst.py --mode sniff --interface <network-interface>
    ```

3. Analyze a specific HTTP request log file:
    ```bash
    python http_request_analyst.py --mode analyze --file <log-file>
    ```

    Replace `<host>`, `<port>`, `<network-interface>`, and `<log-file>` with the actual values.

### Example

Capture HTTP requests via a proxy server on localhost port 8080:

```bash
python http_request_analyst.py --mode proxy --host localhost --port 8080
```

Capture HTTP requests via packet sniffing on the `eth0` network interface:

```bash
python http_request_analyst.py --mode sniff --interface eth0
```

Analyze a specific HTTP request log file:

```bash
python http_request_analyst.py --mode analyze --file http_requests.log
```

## Options

- `--mode`: Mode of operation (proxy, sniff, analyze).
- `--host`: Host address for the proxy server (required for proxy mode).
- `--port`: Port number for the proxy server (required for proxy mode).
- `--interface`: Network interface for packet sniffing (required for sniff mode).
- `--file`: Path to the HTTP request log file (required for analyze mode).

## Legal Disclaimer

This tool is intended for educational purposes and ethical use only. Unauthorized use of this tool to capture or analyze HTTP requests without proper authorization is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj
