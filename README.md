La base di dati PIZZERIA tiene traccia di tutte le prenotazioni di una pizzeria per asporto,
dei menu delle pizze e delle bevande, dei clienti e dei coupon (buoni sconto) messi a disposizione
dalla pizzeria. Ogni prenotazione ha un codice univoco, un cliente associato (posso controllare che
non venga inserito in due prenotazioni lo stesso nome), un orario di riferimento e la lista dei
codici dei prodotti (pizze e bevande) desiderati. I prodotti sono di due tipi: pizze o bevande.

Ogni pizza ha un codice univoco, un nome, (la lista di ingredienti) e un prezzo.
Ogni bevanda ha un codice univoco, un nome e un prezzo.
Ogni cliente è identificato da un nome (nome di battesimo e cognome).
Inoltre la pizzeria in particolari occasioni rilascia dei coupon a qualche cliente permettendogli
di avere diversi tipi di sconto.

Ogni coupon ha un codice univoco identificativo e un valore in euro pari al valore dello sconto applicabile.
(chiaramente dopo essere stato utilizzato viene eliminato dal database, inoltre un coupon può essere
utilizzato solamente se il prezzo scontato rimane maggiore di dieci euro,
 i coupon non sono cumulabili).