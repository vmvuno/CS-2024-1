# Pesquisa sobre o tema "REST API"

Uma API REST engloba dois conceitos:
1. **API (*Application Programming Interface* - Interface de Programação de Aplicação):** Um mecanismo que permite que dois componentes de software se comuniquem usando um conjunto de definições e protocolos.

2. **REST (*Representational State Transfer* - Transferência de Estado Representacional):** Um estilo arquitetural baseado em um conjunto de princípios que descrevem como recursos em rede são definidos e endereçados.
  
  
O estilo arquitetural REST é projetado para uso em aplicações baseadas em rede e define as seguintes restrições:
1. Modelo cliente servidor - Clientes são separados de servidores por meio de uma interface bem definida;
2. Sem estado - Um cliente específico não deve consumir armazenamento do servidor enquanto estiver ocioso;
3. Cache - As respostas devem indicar a capacidade de serem armazenadas em cache.
4. Interface uniforme, que simplifica e desacopla a arquitetura:
   - Identificação de recursos nas requisições (por exemplo, por meio de URI);
   - Manipulação de recursos através de representações;
   - Mensagens auto-descritivas;
   - Hypermedia como motor de estado da aplicação (havendo acessado o URI inicial da aplicação, um cliente deve ser capaz de usar os links dinamicamente providos pelo servidor para descobrir todos os recursos disponíveis)
5. Sistema em camadas - Um cliente não deve ser capaz de distinguir se está conectado diretamente ao servidor final ou a um intermediário;
6. Código por demanda - Servidores podem extender ou customizar temporariamente as funcionalidades de um cliente por meio da transferência de lógica que pode ser executada por intermédio de uma máquina virtual padrão.

Essas restrições conferem ao sistema propriedades não-funcionais, como:
1. A performance da interação entre os componentes;
2. A escalabilidade da aplicação;
3. A simplicidade, ao prover uma interface uniforme;
4. Capacidade de modificação dos componentes;
5. Visibilidade de comunicação entre componentes por parte dos agentes de serviços;
6. Portabilidade de componentes, por mover código de programas junto aos dados;
7. Confiabilidade, sob a forma de resistência a falhas a nível de sistema.  
  




## Referências

- O que é uma API? Explicação sobre interfaces de programação de aplicação. [Amazon](https://aws.amazon.com/pt/what-is/api/#:~:text=API%20significa%20Application%20Programming%20Interface,de%20servi%C3%A7o%20entre%20duas%20aplica%C3%A7%C3%B5es.).
- RT Fielding. [Architectural styles and the design of network-based software architectures](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
- REST. [Wikipedia](https://en.wikipedia.org/wiki/REST)
- Representational State Transfer (REST). [Service Architecture](https://www.service-architecture.com/articles/web-services/representational-state-transfer-rest.html)
