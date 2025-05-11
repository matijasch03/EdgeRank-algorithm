Uslovi da bi korisnik bio povezan sa drugim korisnikom u grafu:
	1) score reakcija na njegove objave (zavisi od lajkova, komentara i šerovanja)
	 -smanjuje se s vremenom ukoliko nema novih reakcija
	2) da li su korisnici prijatelji
	 -score se uvećava za konstantnu vrednost, nezavisno od vremena
	 
Kreiranje grafa:
	-prijatelji dvosmerno povezani
	-povezivanje sa jako popularnim korisnicima (univerzalno za sve korisnike)
	-povezivanje sa mnogo lajkovanim prijateljima prijatelja
	
Nakon kreiranja grafa, vrši se obilazak grafa po svim čvorovima (korisnicima) sa kojima je direktno povezan.
Za svakog korisnika se pretražuje 10 najpopularnijih objava i dodaje se u rečnik {ključ_objave:score}.
Lista se sortira po scoru i ispisuje se prvih 10.
