from bs4 import BeautifulSoup
import requests
import csv

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#==================   [FUNCTIONS]   ======================#

def getHTML(pn):

#	loops for all pages from 'adoro cinema'

	link = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/?page="
	pn = str(pn)
	link = link+pn

	with open('cat.html') as html_file:
		cat = BeautifulSoup(html_file,'lxml')

	return (cat)


def getNames(cat):

#	fetch all the 'movie name' from 'adoro cinema'
	
	nameLIST = []

	for title in cat.find_all('h2'):
	    name = title.a.text[1:len(title.a.text)-1]
	    nameLIST.append(name)

	return (nameLIST)


def getLIST(cat):

#	fetch all genres of the movies from 'adoro cinema'
#	treat all the data

	genreLIST = []

	for genre in cat.find_all('div', class_="oflow_a"):
	    temp = ""
	    if "genre" in str(genre):
	        temp = genre.text
	    genreLIST.append(temp)


	l = []
	for i in genreLIST:
	    if i != '':
	        l.append(i[1:len(i)-1])


	generos = []
	for i in l:
	    aux = i.split(',')
	    generos.append(aux)


	for filme in generos:
	    for i in range(len(filme)):
	        if filme[i][0] == ' ':
	            aux = filme[i].split()
	            filme[i] = ''.join(aux)
	        if filme[i][len(filme[i])-1] == ' ':
	            aux = filme[i].split()
	            filme[i] = ''.join(aux)
	return (generos)


def makeDic(nameLIST,generos):

#	creates a dic for with 'movie name' key and 'genres'

	dic = {}
	size = len(generos)

	for i in range(0,size):
		dic[nameLIST[i]] = generos[i]

	return (dic)


def get_the_movie_genres(j,positions,allgenres):

#	will put 1 on the position where the genre is refered
#	positions is a dic for all the possible genres
#	allgenres is a list of the genres of the correspondly movie

	for key in positions:
		if positions[key] == j:
			allgenres[key] = 1


def gettest(generos):
	
#	separates all genres to use on a machine learning case

	positions = {0:'Ação',1:'Animação',2:'Artes Marciais',3:'Aventura',4:'Biografia',5:'Bollywood',6:'Clássico',7:'Comédia',8:'Comédia dramática',9:'Comédia Musical',10:'Crime',11:'Desenho Animado',12:'Documentário',13:'Doramas',14:'Drama',15:'Épico',16:'Erótico',17:'Espetáculo',18:'Espionagem',19:'Esporte',20:'Experimental',21:'Família',22:'Fantasia',23:'Faroeste',24:'Ficção científica',25:'Guerra',26:'Histórico',27:'Movie night',28:'Musical',29:'Ópera',30:'Outros',31:'Policial',32:'Romance',33:'Show',34:'Suspense',35:'Terror'}

	test = []

	for i in generos:
		allgenres = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		for j in i:
			get_the_movie_genres(j,positions,allgenres)
		
		test.append(allgenres)

	return test


def IA(nameLIST,generos):

#	creates and train a set

	train_x = gettest(generos)
	train_y = []

	for i in range(0,180):
		if i < 90:
			train_y.append(1)
		else:
			train_y.append(0)

	model = LinearSVC()

	model.fit(train_x[:20]+train_x[150:],train_y[:20]+train_y[150:])

	predict = model.predict(train_x[20:40]+train_x[100:150])

	accurary = accuracy_score(train_y[20:40]+train_y[100:150],predict) * 100

	print("You predicted {:.2f}% correctly".format(accurary))


def writecsv(nameLIST,generos):

#	writes the 'movie names' and 'genres' inside a csv file

	with open('movies.csv', mode='w') as file:
	    fieldnames = ['name', 'genre']
	    writer = csv.DictWriter(file, fieldnames=fieldnames)

	    writer.writeheader()
	    for i in range(len(generos)):
	    	writer.writerow({'name': nameLIST[i],'genre': generos[i]})


#==============   [MAIN]   ===================#

def main():

	nameLIST = []
	generos = []
	
	for i in range(1,10):
		print(i)
		cat = getHTML(i)
		nameLIST = nameLIST + getNames(cat)
		generos = generos + getLIST(cat)

	dic = makeDic(nameLIST,generos)

	IA(nameLIST,generos)

	writecsv(nameLIST,generos)

	return 0


main()