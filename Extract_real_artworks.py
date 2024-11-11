from py2neo import Graph, Node, Relationship
from io import BytesIO
from PIL import Image
import requests
from neo4j import GraphDatabase

driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=('neo4j', 'neo4j'))

query = """
MATCH (a:Artwork) with count(distinct a ) as Tot return Tot 
"""

with driver.session() as session:
    result = session.run(query)
    Tot = result.single()[0]
driver.close()
query = """match (a:Artwork)--(s:Style) with count(DISTINCT a) as N_art, s.name as Stile return *"""
N_style = {}
T = 50000
print("Percentuale|", "Stile|", "Numero di artwork in 50k|")
with driver.session(database='neo4j') as session:
 for record in session.run(query):
     P_stile = record['N_art'] / Tot * 100        #percentuale di artwork di un dato stile sul totale di ArtGraph
     style = record['Stile']             #stile
     print(str(round(P_stile, 2)) + '%  |', style + '  |', str(50000 * round(P_stile) / 100) + ' |')
     N_style[style] = T * round(P_stile) / 100 #Dizionario contenente i vari stili e il numero di artwork da inserire nel nuovo dataset in base alla percentuale calcolata prima
for keys, values in N_style.items():
    query = """
       MATCH (a:Artwork)--(s:Style)
       WHERE EXISTS(a.image_url) and s.name = $stile
       RETURN a.image_url AS url, a.name AS name
       """
    n = 0
    with driver.session(database='neo4j') as session:
        for record in session.run(query, {"stile": keys}):
            if n < values:
                url = record['url']
                name = record['name']
                filename = f"/Users/Asus/Desktop/Real_art/{name}"
                try:
                    response = requests.get(url)
                    img = Image.open(BytesIO(response.content))
                    # salvataggio dell'immagine compressa
                    img.save(f"{filename}", optimize=True, quality=50)
                    n += 1
                except Exception as e:
                    print(f"Errore nel scaricare: {filename}: {e}")