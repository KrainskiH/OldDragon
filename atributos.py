def interpretar_atributo(nome, valor):
    tabelas = {
        "Força": [
            (3, 8, "Fraco: você é franzino e tem dificuldade para tarefas físicas."),
            (9, 12, "Mediano: realiza tarefas comuns sem problemas, mas não se destaca."),
            (13, 16, "Forte: claramente forte, requisitado para trabalhos braçais."),
            (17, 18, "Muito Forte: um colosso, faz o impossível para pessoas comuns."),
        ],
        "Destreza": [
            (3, 8, "Letárgico: movimentos lentos e desajeitados."),
            (9, 12, "Mediano: coordenação aceitável, realiza tarefas simples."),
            (13, 16, "Ágil: movimentos graciosos e precisos."),
            (17, 18, "Preciso: movimentos fluidos, quase mágicos."),
        ],
        "Constituição": [
            (3, 8, "Frágil: aparência debilitada, saúde fraca."),
            (9, 12, "Mediano: saudável, tolera esforços e doenças leves."),
            (13, 16, "Resistente: aguenta impactos e esforços acima da média."),
            (17, 18, "Vigoroso: quase imune a doenças e fadiga."),
        ],
        "Inteligência": [
            (3, 8, "Inepto: dificuldade para aprender e memorizar."),
            (9, 12, "Mediano: aprende normalmente, memória razoável."),
            (13, 16, "Inteligente: aprende rápido, memória invejável."),
            (17, 18, "Gênio: raciocínio brilhante, memória quase perfeita."),
        ],
        "Sabedoria": [
            (3, 8, "Tolo: age por impulso, distraído e desatento."),
            (9, 12, "Mediano: bom senso e intuição normais."),
            (13, 16, "Intuitivo: percebe nuances e dá bons conselhos."),
            (17, 18, "Presciente: intuição certeira, quase sobrenatural."),
        ],
        "Carisma": [
            (3, 8, "Descortês: dificuldade de empatia, presença desconfortável."),
            (9, 12, "Mediano: sociável, educado e amigável."),
            (13, 16, "Influente: popular, sabe convencer e liderar."),
            (17, 18, "Ídolo: presença marcante, influência extrema."),
        ],
    }
    for minimo, maximo, descricao in tabelas[nome]: #Percorre a tabela de atributos para encontrar o intervalo correspondente
        if minimo <= valor <= maximo: #Verifica se o valor do atributo está dentro do intervalo definido
            return descricao #Retorna a descrição correspondente ao valor do atributo
    return "Valor fora da escala." #Se o valor não estiver dentro de nenhum intervalo, retorna uma mensagem padrão
