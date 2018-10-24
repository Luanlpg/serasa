# Serasa-Climatempo

Serasa-Climatempo é uma API que recebe o nome de um estado e retorna informaçoes de clima para cada mês.


Quero pedir desculpas antecipadamente, pois não consegui encontrar tempo o suficiente para entregar um código
de qualidade, deixei faltar muitas coisas que gostaria de entregar, portanto, peço desculpas.



## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+, pip(Atualizado) e GeckoDriver(Firefox-Atualizado)))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone github.com/Luanlpg/serasa.git`

- Acesse o repositório: `cd serasa`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando consulta por cidade

- Acesse o projeto django com: `cd climatempo`

- Rode o python: `python`

- importe a classe Climatempo com: `from clima import ClimaTempo`

- Instancie a classe com : `c = ClimaTempo()`

- Chame o metodo de parser com: `c.parser('<NOME DA CIDADE QUE DESEJA>')`

- Aguarde até 5 min. para receber o resultado.(SALENIUM È MUUUITO LENTO!)
