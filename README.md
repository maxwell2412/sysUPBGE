# sysUPBGE
Sistema de veiculo para upbge, incluindo possibilidades de instancia dos objetos, e de comportamento para diferentes tipos de interação.
para poder usalo temos que ter:
*Um modelo que será um chassi do carro com a fisica em rigidbody, e o convexHull como collision bounds.
*As quatro rodas, cada roda tem que ter uma propriedade chamada "roda".e a fisica, tem que estar em no colission, e para cada roda tem que ter outra propriedade para a indentificação deles, 
("fd" para frente direita ),("fe" para frente esquerda ),("td" para tras direita ),("te" para tras esquerda ).
*Criar um crupo com todos esses objetos selecionados com ctrl+G, vamos selecionar o objeto chassi, e setar o centro do objeto chassi no centro da mass , em modo de objeto. Faça shift + ctrl + alt + c (e origem para centro da massa).
*Vai la na propriedade do objeto , ir ate a aba de grupo mudar  nome do grupo, e na setinha vai apertar e selecionar (set offset from cursor).
*Na cena principal onde vai rodar o game, podemos instanciar este objeto(shift + a) e o ultimo item é a instancia do grupo , apenas selecione o seu grupo da daquele carro .
