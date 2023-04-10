from jinja2 import Template
import requests
from bs4 import BeautifulSoup





texto_lista = []   # lista que recebe as perguntas extraidas do google forms

def extrair_perguntas():  # função para extrair perguntas do google forms 

    url = "https://docs.google.com/forms/d/e/1FAIpQLSfQiaWOaVV4kYK_uhoXtZrYdUQ8tBW4F7r8mvvUqAPHF95g7w/viewform" # url que quero extrair perguntas
    response = requests.get(url)  # metodo para extrair
    response.encoding = 'ISO-8859-1' # Define a codificação do conteúdo (Acentos)
    soup = BeautifulSoup(response.content, "html.parser") 

    n=0
    for texto in soup.find_all(class_="M7eMe"): # pega o texto que esta dentro da classe html M7eMe
     

        if(n>9): # so salva na lista depois da intereção 9 pq antes são campos que não interessam 
         # print(texto)
         # print(texto.text.strip())
          texto_lista.append(texto.text.strip()) # adicionando na lista
        n=n+1
   # print(texto_lista)

 
 


 
 
 
def gera_html_ne(base,nome_pagina, ii): # função para gerar html usando jinja2
    

	# passando os parametros para variaveis locais
    i=ii 
    linhas = base
   
    

    # Defina o modelo Jinja2

    template = Template("""

    <!DOCTYPE html>
    <html>
    <head>
 

    
    <meta charset="ISO-8859-1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	
    <title>QUESTIONÁRIO DE ESQUEMAS DE YOUNG — YSQ – S3</title>
	
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>

    <script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.js"></script>


    <link href="style.css" rel="stylesheet">

    </head>

    <body>


<form action="processa_respostas.py" method="post" >
		
		
			<h1>QUESTIONÁRIO DE ESQUEMAS DE YOUNG — YSQ – S3</h1>


    	<div class="div_geral">
		
			<label for="data" class="titulo">Data:</label>
			<input type="date" id="data" name="data" required disabled>
		
		</div>

		<div class="div_geral">


            <label for="cpf" class="titulo">CPF - (Apenas Números):</label>
			<input type="text" id="cpf" name="cpf" placeholder="Digite seu CPF" data-toggle="tooltip" title="Insira seu cpf" required oninvalid="this.setCustomValidity('O campo cpf não está preenchido, por favor preencha.')" oninput="setCustomValidity('')">

		</div>
		
		
			

		<div class="div_geral">
		
			<label for="nome" class="titulo">Nome:</label>
			<input type="text" id="nome" name="nome" placeholder="Digite seu nome" data-toggle="tooltip" title="Insira seu nome completo" required oninvalid="this.setCustomValidity('O campo nome não está preenchido, por favor preencha.')" oninput="setCustomValidity('')">
		
		</div>
			
		<div class="div_geral">
		
			<label for="datanasc" class="titulo">Data de Nascimento:</label>
			<input type="date" id="datanasc" name="datanasc"  min="1900-01-01" max="2018-12-31"  required placeholder="Digite sua data de nascimento" data-toggle="tooltip" title="Insira sua data de nascimento"  oninvalid="this.setCustomValidity('O campo data de nascimento não está preenchido, por favor preencha.')" oninput="setCustomValidity('')" onchange="calcularIdade()">

		</div>
				
		<div class="div_geral">
		
			<label for="idade" class="titulo">Idade:</label>
			<input type="number" id="idade" name="idade" min="1" max="150" required>
		
		</div>

		

		<div class="div_geral">
			<label for="genero" class="titulo">Gênero:</label>
			<div class="form-check form-check-inline">

				<input class="form-check-input" type="radio" id="genero_feminino" name="genero" value="feminino" required>
				<label class="form-check-label" for="genero_feminino">Feminino</label>
			
			</div>
			
			<div class="form-check form-check-inline">
			
				<input class="form-check-input" type="radio" id="genero_masculino" name="genero" value="masculino" required>
				<label class="form-check-label" for="genero_masculino">Masculino</label>
			</div>

				<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="genero_outro" name="genero" value="outro" required>
				<label class="form-check-label"  for="genero_masculino">Outro</label>
			
			</div>	
		</div>



		<div class="div_geral">



				<label for="estado_civil" class="titulo">Estado civil:</label>

			<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="estado_civil_solteiro" name="estado_civil" value="solteiro" required>
				<label class="form-check-label" for="estado_civil_solteiro">Solteiro</label>
			</div>

			<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="estado_civil_casado" name="estado_civil" value="casado" required>
				<label class="form-check-label" for="estado_civil_casado">casado</label>
			</div>
			<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="estado_civil_divorciado" name="estado_civil" value="divorciado" required>
				<label class="form-check-label" for="estado_civil_divorciado">Divorciado</label>
			</div>
			<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="estado_civil_viuvo" name="estado_civil" value="viuvo" required>
				<label class="form-check-label" for="estado_civil_viuvo">Viuvo</label>
			</div>
			<div class="form-check form-check-inline">
				<input class="form-check-input" type="radio" id="estado_civil_separado" name="estado_civil" value="separado" required>
				<label class="form-check-label" for="estado_civil_separado">Separado</label>
			</div>
			
			
			
			
		</div>
    


     {% for linha in base %}




	<div class="div_geral">


		<label for="r1-{{loop.index + i}}" class="titulo">{{ linha }}</label>
			
			<div class="form-check form-check-inline">	
			
				<input class="form-check-input" type="radio" id="r1" name="r1-{{loop.index + i}}" value="1" required>
				<label class="form-check-label for="r1">1</label>
			</div>

			<div class="form-check form-check-inline">

				<input class="form-check-input" type="radio" id="r2" name="r1-{{loop.index + i}}" value="2" required>
				<label class="form-check-label for="r2">2</label>

			</div>

			<div class="form-check form-check-inline">
				
				<input class="form-check-input" type="radio" id="r3" name="r1-{{loop.index + i}}" value="3" required>
				<label class="form-check-label for="r3">3</label>
			
			</div>

			<div class="form-check form-check-inline">
				
				<input class="form-check-input" type="radio" id="r4" name="r1-{{loop.index + i}}" value="4" required>
				<label class="form-check-label for="r4">4</label>
			
			</div>
			
			<div class="form-check form-check-inline">
			
				<input class="form-check-input" type="radio" id="r5" name="r1-{{loop.index + i}}" value="5" required>
				<label class="form-check-label for="r5">5</label>
			
			</div>
			
			<div class="form-check form-check-inline">
				
				<input class="form-check-input" type="radio" id="r6" name="r1-{{loop.index + i}}" value="6" required>
				<label class="form-check-label for="r6">6</label>
			
			</div>

		</div>
        {% set i = i + 1 %}







     {% endfor %}

	<div class="div_enviar">

		<button type="submit" class="btn btn-primary" value="Enviar">Enviar</button>
	
		
	
	</div>


  
	</form>


    <script src="validacoes_campos_javascript.js"></script>

    </body>
    </html>
    """)

    # Renderize o modelo com o dicionário Python e escreva o resultado em um arquivo "index.html"
    with open(nome_pagina, "w") as f:
        html = template.render(base=linhas,i=ii)
        f.write(html)
    print(f'Template {nome_pagina} criado')






extrair_perguntas() # executa a função de extrair as perguntas do google forms

ii=0 
gera_html_ne(texto_lista,'index.html',ii) # executando o gera_html_ne
