# Serasa-Climatempo

Serasa-Climatempo é uma API que recebe o nome de um estado e retorna informaçoes de clima para cada mês.



## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+, pip(Atualizado) e GeckoDriver(Firefox-Atualizado)

- Instalação básica do geckodriver: https://take.net/blog/take-test/instalacao-geckodriver-driver-para-abrir-o-firefox-no-selenium/

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone github.com/Luanlpg/serasa.git`

- Acesse o repositório: `cd serasa`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando consulta por cidade

- Acesse o projeto django com: `cd climatempo`

- Rode o python: `python`

- importe a classe Climatempo com: `from core.clima import ClimaTempo`

- Instancie a classe com : `c = ClimaTempo()`

- Chame o metodo de parser com: `c.parser('<NOME DA CIDADE QUE DESEJA>')`
(Ex. `c.parser('São Carlos`)
- Aguarde até 5 min. para receber o resultado.(SALENIUM È MUUUITO LENTO!)
