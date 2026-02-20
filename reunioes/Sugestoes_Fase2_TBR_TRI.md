# Proposta para Fase 2: A Ponte Quanti-Quali (TBR-2D-BO ↔ TRI)

**Contexto Prévio:** A reunião inicial de Triangulação (Fase 1) focou 100% na análise pedagógica (qualitativa) das 3 partes do item (Contexto, Enunciado, Distratores), utilizando a TBR como régua mediadora da Matriz de Referência (MR) e Situação-Problema (SP).

Para evitar sobrecarga cognitiva (Teoria de *John Sweller*), os parâmetros matemáticos do INEP foram omitidos da Fase 1. Agora, na **Fase 2 (Validação Ex-post)**, cruzaremos os dados gerados pelos especialistas com a realidade empírica do exame.

---

## O Problema na Pesquisa Atual
Muitos artigos acadêmicos fazem apenas estudos puramente estatísticos (focados nas curvas da TRI) ou puramente pedagógicos (focados em taxinomias). Raros são os modelos que criam uma **calibração bidirecional** consistente. O método TBR-2D-BO preenche essa lacuna.

---

## Como Propor a "Fase 2" na Próxima Reunião

**Objetivo da Reunião 2:** Apresentar aos especialistas que o julgamento pedagógico deles tem respaldo (ou gera anomalias reveladoras) quando testado contra o desempenho de milhões de candidatos.

### Sugestão 1: A "Prova dos Nove" com o Parâmetro 'b' (Dificuldade)
*   **A Abordagem:** Mostre o painel HTML (`Painel_ENEM_TRI_ML3P.html`) com a curva logística. Explique que o INEP mede o parâmetro *b* empiricamente.
*   **A Hipótese Principal:** "Se nós codificamos que um item exige *Avaliar (Nível 5)*, ele **deve** ter um parâmetro *b* matematicamente alto na planilha do INEP."
*   **A Ação:** Colar a coluna com os níveis da TBR acordados pelos especialistas ao lado da coluna do parâmetro *b* real do INEP. Calcular a correlação estatística (ex: Correlação de Spearman).
*   **O Valor:** Se der alta correlação, o método de vocês é incrivelmente robusto. Se der baixa correlação, não significa que vocês erraram, mas sim que pode haver uma **Variância Irrelevante (VIC) grave** no item (ex: a questão pede "Lembrar", mas o texto é tão mal escrito que o parâmetro *b* disparou para difícil).

### Sugestão 2: O Peso dos Distratores com o Parâmetro 'a' (Discriminação)
*   **A Abordagem:** O parâmetro *a* mede se a questão separa bem quem sabe de quem "chuta".
*   **A Hipótese Principal:** "Itens onde os especialistas notaram que a Situação-Problema (SP) exige um processo complexo graças a *distratores ardilosos* tendem a ter um parâmetro *a* alto."
*   **A Ação:** Revisitar a tabela individual das justificativas. Aquelas em que o especialista anotou "Atenção: o distrator induz ao erro" devem mapear diretamente para itens com alta inclinação na curva logística (alta discriminação).

### Sugestão 3: Revelando "Itens Patológicos" (O Fator 'c' - Chute)
*   **A Abordagem:** O parâmetro *c* indica acerto casual.
*   **Ação Mista:** Se a equipe classificou um item como nível de processamento alto (*Analisar/Avaliar*), mas a planilha do INEP mostra um limite assintótico alto (parâmetro *c* elevado), isso é um alerta. Significa que, apesar de pedagogicamente bem montada, na prática, a questão tem "gabarito vazado" ou alternativas absurdas que facilitam a eliminação sem raciocínio profundo.

### Sugestão 4: Análise Multivariada (Heatmap da Tripla Correlação)
*   **A Abordagem:** Criar um modelo visual integrado (mapa de calor / *heatmap*) que cruze simultaneamente múltiplas variáveis qualitativas e quantitativas.
*   **A Hipótese Principal:** "A combinação da Habilidade (ação MR), do Processo Cognitivo (TBR) e da Demanda Real (ação SP + Distratores) formará clusters (agrupamentos) específicos de dificuldade ('b') e discriminação ('a') com as notas dos itens."
*   **A Ação:** Construir uma matriz onde as linhas sejam os itens e as colunas sejam: `[Verbo MR] | [Verbo SP] | [Nível TBR (1-6)] | [Parâmetro 'a'] | [Parâmetro 'b'] | [Nota/Acerto %]`. Aplicar uma escala de cores (ex: gradiente verde-vermelho) ou uma análise de componentes principais (PCA) para revelar correlações ocultas.
*   **O Valor:** Permitirá visualizar de forma gráfica se uma desarmonia na tripla correlação (ex: MR pede nível 5, SP exige nível 2) "quebra" as previsões da TRI, fornecendo a prova cabal e visual da subjetividade que o modelo TBR-2D-BO consegue corrigir.

---

## Resumo do Convite para a Reunião 2:
*"Prezados, agora que o nosso cérebro especialista calibrou a intenção pedagógica (TBR) de cada questão, nós vamos confrontar o nosso parecer com o 'Tribunal dos Fatos': os parâmetros gerados por 4 milhões de candidatos (TRI).* 

*O objetivo não é reavaliar a questão, mas procurar **Padrões de Convergência** (nosso método prevê a dificuldade real do ENEM de forma consistente?) e **Itens Anômalos** (as discrepâncias onde a questão é teoricamente fácil, mas na prática foi um desastre devido a falhas na Situação-Problema)."*
