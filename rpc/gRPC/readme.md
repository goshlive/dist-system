To use this demo, follow steps below:
1. Create a new python environment:
    python -m venv myenv
2. Execute:
    myenv\Scripts\activate
    Or, in VS Code, click Ctrl+Shift+P --> Python: Select Interpreter, choose an environment
3. Install dependencies
    pip install -r requirements.txt
4. Define the contract file:
    processor.proto
5. Execute:
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. processor.proto
    It will create the stub files:
    - processor_pb2_grpc.py
    - processor_pb2.py
6. 
