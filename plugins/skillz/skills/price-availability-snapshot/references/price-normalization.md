# Price normalization

## Comparable offers

Angebote sind direkt vergleichbar, wenn Kandidat, relevante Variante, Region, Zustand und Bundle-Kontext ausreichend übereinstimmen. Abweichungen bleiben sichtbar.

## Effective price

`effectivePrice` darf nur aus expliziten numerischen Bestandteilen berechnet werden. Unbekannte Versand-, Steuer- oder Pflichtzubehörkosten werden nicht als null angenommen.

## TCO

TCO benötigt einen expliziten Horizon. Trenne bekannte und angenommene Kosten; jede Annahme erhält Quelle oder Begründung. `quote-required` ist ein valider Zustand und kein Anlass für eine Schätzung.
