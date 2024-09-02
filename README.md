
## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mrsk005/Dynamic-Allocation-Of-Bandwidth-Using-LEO-Satellites.git
    cd Dynamic-Allocation-Of-Bandwidth-Using-LEO-Satellites
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```

5. **Access the application:**

    Open a web browser and go to `http://127.0.0.1:5000` to view the application.

## Components

- **DRL**: The Deep Reinforcement Learning component is used for decision-making regarding bandwidth allocation.
- **FCMR**: The Fuzzy CNN-based Multi-Task Routing component is used for routing based on the allocation decisions.
- **Flask**: The web framework used to serve the application and handle user interactions.

## Notes

- Ensure that you have the necessary environment variables set up, especially `SECRET_KEY`.
- The actual DRL and FCMR implementations are not included in this template. You need to implement these components according to your specific requirements.
- For more details on how to configure and use each component, refer to their respective documentation and implementation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
