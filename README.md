# ModeloAgendamentoBarbearia

Aplicação protótipo para agendamento de barbearia (GUI em Tkinter + persistência em SQLite).  
Este repositório contém um exemplo simples de CRUD local (clientes e agendamentos) pensado para iniciantes que querem aprender a criar interfaces e salvar dados com SQLite.

![Screenshot da interface](assets/screenshot_gui.png.)

Principais pontos
- Interface gráfica com Tkinter e ttk (ComboBox) para seleção de serviços.  
- Persistência local com SQLite (uso de queries parametrizadas).  
- Estrutura modular: separação da camada de banco (db.py) e da GUI (appBarber.py).  
- Projeto ideal para aprendizado e para evoluir (ex.: autenticação, export CSV, relatórios).

Status
- Versão atual: protótipo
- Desenvolvimento: v2.0 (melhorias de UI com ComboBox e layout mais amigável)

Funcionalidades
- Cadastro básico de clientes (nome, celular).  
- Agendamento de serviços por cliente (data/hora, serviço selecionado via ComboBox).  
- Visualização de clientes e agendamentos (lista simples).  
- Armazenamento local em arquivo SQLite (barber.db por padrão).

Pré-requisitos
- Python 3.8+  
- Tkinter (vem com a maioria das instalações do Python; em algumas distribuições Linux instale o package `python3-tk`)  
- Não há dependências externas obrigatórias (opcionalmente você pode usar pandas para exportar relatórios).

Instalação rápida
1. Clone o repositório:
   git clone https://github.com/igordesouzabranco/ModeloAgendamentoBarbearia.git
2. Entre na pasta:
   cd ModeloAgendamentoBarbearia
3. (opcional) Crie e ative um ambiente virtual:
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows

Executar a aplicação
- Arquivo de entrada: `appBarber.py`  
- Execute:
  python appBarber.py

Estrutura proposta dos arquivos
- appBarber.py         -> interface e lógica de interação com o usuário (GUI)  
- db.py                -> classe Database para CRUD em SQLite  
- assets/              -> screenshots e imagens  
- README.md            -> este arquivo  
- requirements.txt     -> (opcional) dependências externas


Contribuições
- Pull requests são bem-vindos. Para grandes mudanças, abra uma issue descrevendo a proposta antes.

Contato
- Igor de Souza Branco — igordesouzabranco@gmail.com  

Licença
- MIT

_Last updated: 2026-01-03_
