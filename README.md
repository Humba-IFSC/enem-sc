# Análise dos Microdados do ENEM: Desigualdade, Meritocracia e Propostas de Políticas Públicas

![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-blue)

## Resumo

Este repositório contém o código e a metodologia da pesquisa dedicada à análise dos microdados do Exame Nacional do Ensino Médio (ENEM). Nosso objetivo é investigar as profundas desigualdades sociais e raciais refletidas nos resultados do exame, utilizando evidências sólidas para questionar o conceito de meritocracia em avaliações de larga escala. A partir das análises, buscaremos desenvolver e propor políticas públicas direcionadas à inclusão e à redução da desigualdade, com contribuições diretas para o Ministério da Igualdade Racial e outros órgãos competentes do governo federal.

## Contextualização

O ENEM consolidou-se como a principal porta de entrada para o ensino superior no Brasil, influenciando a trajetória de milhões de jovens anualmente. No entanto, sob um discurso de "meritocracia", o exame pode mascarar e perpetuar desigualdades estruturais. Fatores como renda familiar, cor/raça, acesso a uma educação de qualidade e capital cultural são determinantes para o desempenho dos estudantes, mas frequentemente ignorados em análises superficiais.

Este projeto nasce da necessidade de aprofundar esse debate com dados, transformando a percepção pública e fornecendo subsídios técnicos para a construção de um sistema educacional verdadeiramente justo e equitativo.

## 🎯 Objetivos

- **Analisar** os microdados do ENEM para identificar disparidades de desempenho entre diferentes perfis socioeconômicos e raciais.
- **Investigar** a correlação entre variáveis de contexto (ex: renda, escolaridade dos pais, região, tipo de escola) e as notas obtidas no exame.
- **Debater** criticamente o modelo de avaliação do ENEM e seu papel na reprodução de desigualdades.
- **Desenvolver** sugestões de políticas públicas baseadas em evidências para promover a inclusão e a equidade no acesso ao ensino superior.
- **Contribuir** com análises e relatórios técnicos para o Ministério da Igualdade Racial e o Ministério da Educação.

## 🛠️ Metodologia

A análise é conduzida utilizando a linguagem de programação Python e suas principais bibliotecas de ciência de dados, como Pandas, Matplotlib, Seaborn e Scikit-learn.

1.  **Fonte de Dados:** Os microdados do ENEM são públicos e foram baixados do [portal oficial do INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem).
2.  **Limpeza e Pré-processamento:** Tratamento dos dados brutos para a criação de um dataset analítico coeso.
3.  **Análise Exploratória de Dados (AED):** Geração de estatísticas e visualizações para identificar padrões e tendências.
4.  **Modelagem Estatística:** (Se aplicável) Uso de modelos para entender o impacto de diferentes variáveis no desempenho.

## 🚀 Como Utilizar este Repositório

### Pré-requisitos

- Python 3.9+
- Gerenciador de pacotes `pip`

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Estrutura do Projeto (em desenvolvimento)

```
.
├── data/
├── notebooks/
│   ├── 01-Limpeza-de-Dados.ipynb
│   └── 02-Analise-Exploratoria.ipynb
├── src/
│   └── utils.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Se você tem interesse em colaborar com análises, visualizações de dados, ou na revisão da metodologia, por favor, siga os passos:

1.  Faça um "Fork" deste repositório.
2.  Crie uma nova "Branch" (`git checkout -b feature/sua-contribuicao`).
3.  Faça suas alterações e "Commits" (`git commit -m 'Adiciona nova análise X'`).
4.  Envie para a sua "Branch" (`git push origin feature/sua-contribuicao`).
5.  Abra um "Pull Request".

## 👥 Equipe

- [Seu Nome](link-para-seu-github-ou-linkedin) - Pesquisador(a) Principal

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
