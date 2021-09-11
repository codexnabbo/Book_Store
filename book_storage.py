
import mysql.connector

def cls(): print("\n" * 100)
connessione = mysql.connector.connect(host="sql4.freesqldatabase.com" ,user="sql4436340",password="gTbCnwyrKR",db="sql4436340")
def one():
    titolo = input("Titolo: ")
    sottotitolo = input("sottotitolo: ")
    autore = input("Autore: ")
    categoria = input("Categoria: ")
    casaeditrice= input("Casa editrice: ")
    isbn = input("ISBN: ")

    cursore = connessione.cursor()
    sql = f"INSERT INTO Book(isbn,title,subtitle,author,type,casa_editrice) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (isbn,titolo,sottotitolo,autore,categoria,casaeditrice)
    cursore.execute(sql, val)
    connessione.commit()

def two():
    print("inserire * nei campi non conosciuti")
    print("iserire tutti * per vedere tutti i libri")
    titolo = input("Titolo: ")
    sottotitolo = input("sottotitolo: ")
    autore = input("Autore: ")
    categoria = input("Categoria: ")
    casaeditrice= input("Casa editrice: ")
    isbn = input("ISBN: ")
    cursore = connessione.cursor()
    sql = f"SELECT isbn, title, subtitle, author, type, casa_editrice FROM Book WHERE "
    count = 0
    valori = []
    if titolo!= "*":
        sql=sql+f"title=%s"
        count+=1
        valori.append(titolo)
    if sottotitolo != "*":
        if count > 0:
            sql = sql + " AND"
        sql = sql+f" subtitle=%s"
        count+=1
        valori.append(sottotitolo)
    if autore != "*":
        if count > 0:
            sql = sql + " AND"
        sql = sql+f" author=%s"
        count+=1
        valori.append(autore)
    if categoria != "*":
        if count > 0:
            sql = sql + " AND"
        sql = sql+f" type=%s"
        count+=1
        valori.append(categoria)
    if isbn != "*":
        if count > 0:
            sql = sql + " AND"
        sql = sql+f" isbn=%s"
        count+=1
        valori.append(isbn)
    if casaeditrice != "*":
        if count > 0:
            sql = sql + " AND"
        sql = sql+f" casa_editrice=%s"
        count+=1
        valori.append(casaeditrice)
    
    if count == 0:
        sql=sql+" 1"
        cursore.execute(sql)
    else:
        val=tuple(valori)
        cursore.execute(sql,val)
    print()
    for i in cursore:
        print(f"\n\
            ISBN:{i[0]}\n\
            TITOLO:{i[1]}\n\
            SOTTOTITOLO:{i[2]}\n\
            AUTORE:{i[3]}\n\
            CATEGORIA:{i[4]}\n\
            CASA EDITRICE:{i[5]}\n\
            ------------------------------------------")
    
    print("\n" *5)
    input("Premi invio per continuare...")


switcher = {
    1: one,
    2: two,
}

def switch(scelta):
    return switcher.get(scelta, "numero errato")()


def main():
    cls()
    print("\
.--.      .--.    .-''-.    .---.        _______      ,-----.    ,---.    ,---.    .-''-.   \n\
|  |_     |  |  .'_ _   \   | ,_|       /   __  \   .'  .-,  '.  |    \  /    |  .'_ _   \  \n\
| _( )_   |  | / ( ` )   ',-./  )      | ,_/  \__) / ,-.|  \ _ \ |  ,  \/  ,  | / ( ` )   ' \n\
|(_ o _)  |  |. (_ o _)  |\  '_ '`)  ,-./  )      ;  \  '_ /  | :|  |\_   /|  |. (_ o _)  | \n\
| (_,_) \ |  ||  (_,_)___| > (_)  )  \  '_ '`)    |  _`,/ \ _/  ||  _( )_/ |  ||  (_,_)___| \n\
|  |/    \|  |'  \   .---.(  .  .-'   > (_)  )  __: (  '\_/ \   ;| (_ o _) |  |'  \   .---. \n\
|  '  /\  `  | \  `-'    / `-'`-'|___(  .  .-'_/  )\ `\"/  \  ) / |  (_,_)  |  | \  `-'    / \n\
|    /  \    |  \       /   |        \`-'`-'     /  '. \_/``\".'  |  |      |  |  \       /  \n\
`---'    `---`   `'-..-'    `--------`  `._____.'     '-----'    '--'      '--'   `'-..-'   ")
    print("\
  ____   ____   ____  _  __   _____ _______ ____  _____  ______ \n\
 |  _ \ / __ \ / __ \| |/ /  / ____|__   __/ __ \|  __ \|  ____|\n\
 | |_) | |  | | |  | | ' /  | (___    | | | |  | | |__) | |__   \n\
 |  _ <| |  | | |  | |  <    \___ \   | | | |  | |  _  /|  __|  \n\
 | |_) | |__| | |__| | . \   ____) |  | | | |__| | | \ \| |____ \n\
 |____/ \____/ \____/|_|\_\ |_____/   |_|  \____/|_|  \_\______|\n\
")
    print("SCEGLI UN OPZIONE")
    print("1) AGGIUNGI LIBRO")
    print("2) CERCA LIBRO")

    scelta = int(input("scelta : "))
    switch(scelta)
    main()
if __name__ == "__main__":
    main()