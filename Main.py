import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Kamera:
    nosaukums: str
    cena: float
    stavoklis: str
    saite: str

def iegut_kameras():
    url = "https://www.ebay.com/sch/i.html?_nkw=digital+camera&_sacat=0&LH_ItemCondition=1000|3000"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    # 🔍 Pārbaude: vai lapa ielādējas?
    print(f"Statusa kods: {response.status_code}")
    print("Lapas sākuma HTML saturs:")
    print(response.text[:1000])  # Izvada pirmos 1000 simbolus

    soup = BeautifulSoup(response.text, "html.parser")
    preces = soup.select(".s-item")

    kameras = []

    for prece in preces:
        nosaukums_elem = prece.select_one(".s-item__title")
        cena_elem = prece.select_one(".s-item__price")
        stavoklis_elem = prece.select_one(".SECONDARY_INFO")
        saite_elem = prece.select_one(".s-item__link")

        if not (nosaukums_elem and cena_elem and stavoklis_elem and saite_elem):
            continue

        try:
            cena = float(cena_elem.text.replace("$", "").replace(",", "").split()[0])
        except ValueError:
            continue

        kamera = Kamera(
            nosaukums=nosaukums_elem.text.strip(),
            cena=cena,
            stavoklis=stavoklis_elem.text.strip(),
            saite=saite_elem["href"]
        )
        kameras.append(kamera)

    return sorted(kameras, key=lambda k: k.cena)[:10]

def izvadit_kameras_terminali(kameras):
    print("\n10 lētākās digitālās kameras eBay (jaunas vai lietotas):\n")
    for i, kamera in enumerate(kameras, 1):
        print(f"{i}. {kamera.nosaukums}")
        print(f"   Cena: ${kamera.cena}")
        print(f"   Stāvoklis: {kamera.stavoklis}")
        print(f"   Saite: {kamera.saite}\n")

if __name__ == "__main__":
    kameras = iegut_kameras()
    izvadit_kameras_terminali(kameras)
