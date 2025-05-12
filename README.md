# eBay Digitālo Kameru Meklētājs

Šī Python programma automātiski iegūst 10 jaunas vai lietotas lētākās digitālās kameras no eBay (https://www.ebay.com/). Programma analizē meklēšanas rezultātu lapu un atlasa atbilstošās preces, pamatojoties uz to cenu.

## Izmantotās Python bibliotēkas

| Bibliotēka       | Iemesls izmantošanai |
|------------------|----------------------|
| `requests`       | Lai veiktu HTTP pieprasījumus uz eBay meklēšanas lapu |
| `BeautifulSoup`  | HTML satura parsēšanai un vajadzīgās informācijas iegūšanai no tīmekļa lapas |
| `dataclasses`    | Tiek izmantota, lai definētu strukturētu datu tipu `Kamera`, kas glabā informāciju par katru kameru |

## Datu struktūras

Programmā tiek izmantota `dataclass` struktūra `Kamera`, kas satur sekojošus laukus:

- `nosaukums` – kameras nosaukums
- `cena` – kameras cena (float)
- `stāvoklis` – jauna vai lietota
- `saite` – tiešā saite uz eBay lapu

Tas nodrošina pārskatāmu un strukturētu datu apstrādi.

##  Lietošanas instrukcija

1. Instalējiet nepieciešamās bibliotēkas:
    ```bash
    pip install requests beautifulsoup4
    ```
2. Palaidiet skriptu:
    ```bash
    python main.py
    ```
3. Rezultātā tiks izvadīts 10 lētāko digitālo kameru saraksts ar cenām, stāvokli un saitēm uz eBay.

## Resursi

- eBay meklēšanas lapa: [https://www.ebay.com/](https://www.ebay.com/)
- Python dokumentācija: [https://docs.python.org/3/](https://docs.python.org/3/)