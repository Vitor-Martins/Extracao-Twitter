# Extracao-Twitter
Scripts para extraçao de dados no Twitter

**Observações:**
* Sou iniciante em Python e quebrei um poouco a cabeça com alguns detalhes, por exemplo, no linux(Ubuntu 16.04) o Python 2 já vem instalado no sistema operacional, logo instalei a versão do Python 3, pois era versão que gostaria de trabalhar. Achando que estava safo, comecei a instalar os módulos do Python utilizando o pip e nada funcionava quando importava, aí que estava a minha surpresa quando verifiquei a versão do Python instalado (Python --version), a versão setada no sistema ainda era o Python 2. É só mudar as configurações do sistema para pegar o Python 3 como default, mas não vou entrar nesse ponto aqui, o importante é verificar a versão do Python para instalar os pacotes e exectar a instância correta.
* Criar um app no Twitter para as credenciais de acesso a API do Twitter - https://apps.twitter.com/ - https://blog.difluir.com/2013/06/como-criar-uma-app-no-twitter/


## Arquivo de Streamming do Twiiter salvando em base de dados MySQL (twitterStream_to_mysql.py)

* O Python 3 suporta emoji (utf8mb4)
* Tutoriais:
  * http://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/
  * https://miningthedetails.com/blog/python/TwitterStreamsPythonMySQL/
  * http://casadepyssaros.com.br/page/9/mysqldb-no-python-3/
* Instale o Mysql
* Instalei o MySQL Workbench, mas se quiser se aventurar na linha de comando é com vocês.
* Instale o conector Mysql via terminal: sudo apt-get install python-mysqldb
* Instale o módulo do mysql via terminal: pip install mysql-connector-python-rf --user
* Ao criar o banco e as tabelas não esqueça de setar o unicode utf8mb4. Criando no Workbench não aparece na lista de unicode, mas é possível configurar via script no próprio Workbench.


