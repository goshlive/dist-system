# Follow the instructions below to run:
1. Start all services:
docker compose up -d --build

2. Check the log:
docker compose logs -f

3. Run the Client:
python client.py

3. Checking all services:
docker compose ps

3. Checking individual log for payment services:
docker compose logs -f payment-1
docker compose logs -f payment-2
docker compose logs -f payment-3

4. Try stopping the elected leader, for.e.g:
docker compose stop payment-3

5. Allow few seconds (±3s), and check the log for new elected leader. For e.g. payment-2

6. Re-run the client:
python client.py

When a leader was down, a new one should automatically be elected and payment should be processed successfully.

7. Try re-starting again the previously down leader, for e.g. payment-3:
docker compose start payment-3

8. Re-run the client:
python client.py

Node payment-3 should become the leader again and payment should be processed successfully.
