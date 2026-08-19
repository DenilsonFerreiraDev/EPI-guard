# 🛡️ EPI Guard

> Sistema inteligente para gestão e controle de entrega de Equipamentos de Proteção Individual (EPIs), com análise automatizada de estoque via Inteligência Artificial e contingência local.

---

## 📌 Sobre o Projeto

O **EPI Guard** foi desenvolvido para otimizar o fluxo de controle de EPIs em ambientes industriais e da construção civil. A aplicação monitora a disponibilidade de itens essenciais, registra entregas associadas a funcionários e oferece diagnósticos preditivos para evitar a falta de insumos de segurança na obra.

---

## 🚀 Funcionalidades Principais

* **Gestão de Estoque**: Cadastro, listagem e atualização de EPIs e seus respectivos Certificados de Aprovação (CA).
* **Controle de Entregas**: Registro de entregas vinculando funcionário e equipamento com baixa automática em estoque.
* **Dashboard em Tempo Real**: Métricas dos EPIs mais retirados, estoque crítico e total de entregas diárias.
* **Análise Inteligente (IA)**: Integração com **Google Gemini API** para diagnósticos preventivos de estoque com **mecanismo de contingência local automático** caso a rede/API esteja indisponível.

---

## 🛠️ Tecnologias Utilizadas

* **Backend**: Python 3.13 / FastAPI
* **Servidor ASGI**: Uvicorn
* **Banco de Dados**: MySQL Server
* **IA Generativa**: Google GenAI SDK (Gemini 1.5 Flash)
* **Frontend**: HTML5, CSS3, Jinja2 Templates

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/DenilsonFerreiraDev/EPI-guard.git](https://github.com/DenilsonFerreiraDev/EPI-guard.git)
cd EPI-guard