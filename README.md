# ExtracaoAzul: Monitoramento de Passagens e Milhas ✈️

Este projeto tem como objetivo monitorar preços de passagens aéreas (em reais e milhas) de forma automatizada, notificando o usuário por e-mail sempre que um voo estiver abaixo do preço teto definido.

## 🛠️ Arquitetura do Projeto

O projeto foi reestruturado de forma modular para garantir maior estabilidade, facilidade de manutenção e evitar bloqueios por sistemas anti-bot:

* **`config/targets.json`**: Centraliza os voos monitorados e os limites de preço.
* **`core/`**: Contém os módulos de scraping e o sistema de notificações (`notifier.py`).
* **`main.py`**: Script principal que gerencia o fluxo de execução do monitoramento.

## 🚀 Como Executar

1. Crie e ative o seu ambiente virtual (`uv venv` ou `venv`).
2. Instale as dependências necessárias.
3. Crie um arquivo `.env` na raiz do projeto com suas credenciais de e-mail (nunca adicione este arquivo ao Git).
4. Configure os destinos desejados em `config/targets.json`.
5. Execute o script principal:
   ```bash
   python main.py