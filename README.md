# 🚀 Ativador de APIs do Google Cloud

Um script Python simples projetado para automatizar a ativação de um conjunto predefinido de APIs no Google Cloud Platform (GCP). É ideal para padronizar e agilizar a configuração inicial de novos projetos, garantindo que todos os serviços necessários estejam habilitados antes de iniciar o desenvolvimento.

---

## ✨ Funcionalidades

-   **Seguro**: Lê o ID do projeto de um arquivo `.env` para não expor informações sensíveis no código.
-   **Eficiente**: Verifica o status de cada API antes de tentar ativá-la, evitando operações desnecessárias.
-   **Claro**: Fornece feedback no terminal sobre o status de cada operação.
-   **Flexível**: Permite customizar facilmente a lista de APIs a serem ativadas diretamente no script.

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha o seguinte:

-   Python 3.8+
-   Google Cloud SDK (`gcloud` CLI): Essencial para a autenticação. Se não tiver, [siga as instruções de instalação](https://cloud.google.com/sdk/docs/install).
-   Um Projeto GCP: Você precisa de um projeto criado no Google Cloud e do **ID do Projeto**.
-   Permissões no GCP: Sua conta precisa de permissões para habilitar APIs, como o papel `Service Usage Admin` (`roles/serviceusage.serviceUsageAdmin`).

---

## ⚙️ Instalação e Configuração

Siga os passos abaixo para preparar e rodar o projeto.

**1. Clone o repositório**
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git)
cd NOME-DO-SEU-REPOSITORIO
2. Crie e ative um ambiente virtual

No Windows (PowerShell):

PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1
No Linux ou macOS:

Bash

python3 -m venv venv
source venv/bin/activate
3. Instale as dependências

Bash

pip install -r requirements.txt
4. Configure suas credenciais

Copie o arquivo de exemplo para criar seu próprio arquivo de ambiente.

No Windows (PowerShell/CMD):

PowerShell

copy .env.example .env
No Linux ou macOS:

Bash

cp .env.example .env
Abra o novo arquivo .env e adicione o ID do seu projeto GCP:

Ini, TOML

# .env
GOOGLE_PROJECT_ID="seu-id-de-projeto-real-aqui"
5. Autentique-se no Google Cloud

Execute os dois comandos abaixo no seu terminal. O primeiro abre seu navegador para login, e o segundo vincula sua autenticação a um projeto para evitar erros de cota.

Bash

gcloud auth application-default login
gcloud auth application-default set-quota-project SEU-ID-DE-PROJETO-REAL-AQUI

▶️ Como Executar
Com tudo configurado, basta executar o script principal:

Bash

python main.py
A saída no terminal mostrará o progresso:

Verificando o serviço: run.googleapis.com...
O serviço run.googleapis.com já está ATIVADO.
Verificando o serviço: bigquery.googleapis.com...
Ativando o serviço: bigquery.googleapis.com...
Serviço bigquery.googleapis.com ativado com sucesso!
...
🛠️ APIs Habilitadas por Padrão
O script está configurado para habilitar as seguintes APIs:

run.googleapis.com (Cloud Run)

bigquery.googleapis.com (BigQuery)

pubsub.googleapis.com (Pub/Sub)

cloudscheduler.googleapis.com (Cloud Scheduler)

cloudbuild.googleapis.com (Cloud Build)

iam.googleapis.com (Identity and Access Management - IAM)

Para adicionar ou remover APIs, edite a lista services_to_enable no arquivo main.py.
