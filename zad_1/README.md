## Decision Rule API

Proste API z regułą decyzyjną opartą na sumie dwóch liczb. Serwis obsługuje endpoint `/api/v1.0/predict`, który przyjmuje parametry `num1` i `num2` (domyślnie 0).

## Reguła decyzyjna
- Jeśli suma dwóch liczb > 5.8: predykcja = 1
- W przeciwnym razie: predykcja = 0

## Uruchomienie
- Lokalnie: `pip install -r requirements.txt && python app.py`
- Docker: `docker build -t decision-rule-api . && docker run -p 5000:5000 decision-rule-api`

API obsługuje metody GET i POST, zwracając wynik w JSONie z kluczami "prediction" i "features".