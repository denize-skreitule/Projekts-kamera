# eBay Digitālo Kameru Meklētājs

## 📝 Projekta uzdevums

Šī Python programma automātiski iegūst 10 lētākās digitālās kameras no eBay (https://www.ebay.com/), kuras ir jaunas vai lietotas. Programma izmanto tīmekļa skrāpēšanu, lai analizētu meklēšanas rezultātu lapu un atlasītu atbilstošās preces, pamatojoties uz to cenu.

## 🧰 Izmantotās Python bibliotēkas

| Bibliotēka       | Iemesls izmantošanai |
|------------------|----------------------|
| `requests`       | Lai veiktu HTTP pieprasījumus uz eBay meklēšanas lapu |
| `BeautifulSoup`  | HTML satura parsēšanai un vajadzīgās informācijas iegūšanai no tīmekļa lapas |
| `dataclasses`    | Tiek izmantota, lai definētu strukturētu datu tipu `Kamera`, kas glabā informāciju par katru kameru |

## 🗃️ Datu struktūras

Programmā tiek izmantota `dataclass` struktūra `Kamera`, kas satur sekojošus laukus:

- `nosaukums` – kameras nosaukums
- `cena` – kameras cena (float)
- `stāvoklis` – jauna vai lietota
- `saite` – tiešā saite uz eBay lapu

Tas nodrošina pārskatāmu un strukturētu datu apstrādi.

## 💡 Lietošanas instrukcija

1. Pārliecinieties, ka jums ir instalēta Python 3.x versija.
2. Instalējiet nepieciešamās bibliotēkas:
    ```bash
    pip install requests beautifulsoup4
    ```
3. Palaidiet skriptu:
    ```bash
    python main.py
    ```
4. Rezultātā jūs saņemsiet konsolē 10 lētāko digitālo kameru sarakstu ar cenām, stāvokli un saitēm uz eBay.

## ⚠️ Piezīme

eBay var izmantot aizsardzību pret robotprogrammatūrām. Ja netiek iegūti dati vai tiek parādīta kļūda, ieteicams izmantot `Selenium` ar pārlūka simulāciju vai pārskatīt pieprasījuma galvenes (`headers`).

## 🔗 Resursi

- eBay meklēšanas lapa: [https://www.ebay.com/](https://www.ebay.com/)
- Python dokumentācija: [https://docs.python.org/3/](https://docs.python.org/3/)
