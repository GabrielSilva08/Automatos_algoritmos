class NFA:
    """Autômato Finito Não-determinístico (Nondeterministic Finite Automaton) dado pela definição clássica (Q, Σ, δ, q0, F).
    """
    def __init__(self,
                 states_set: set[str],
                 alphabet: set[str|int],
                 transition_table: dict[tuple[str, str|int], set[str]],
                 initial_state: str,
                 final_states_set: set[str]):
        """Método construtor da classe.

        Args:
            states_set (set[str]): Conjunto não vazio de estados.
            alphabet (set[str | int]): Alfabeto na qual o autômato irá operar. Ex: Σ = {a, b}.
            transition_table (dict[tuple[str, str | int], set[str]]): Tabela de transição. Estrutura responsável por modelar a função de transição δ : Q × Σ → P(Q).
            initial_state (str): Estado inicial. Ex: "q0".
            final_states (set[str]): Conjunto de estados finais, onde final_states ⊆ states_set.
        """
        self.states_set = states_set
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.final_states_set = final_states_set
        self._validate()

    def __repr__(self) -> str:
        """Representação do autômato para fins de depuração.

        Returns:
            str: Tupla contendo os elementos internos do NFA.
        """
        return f"NFA(Q = {self.states_set},\nΣ = {self.alphabet},\nδ = {self.transition_table},\nq0 = {self.initial_state},\nF = {self.final_states_set})"

    def eval(self, word: str) -> bool:
        """ Verifica se a palavra "word" faz parte da linguagem do autômato. Diferente do DFA onde só 
        existe uma execução possível para uma palavra w, aqui a ideia é simular todas as execuções possíveis 
        até encontrar um caminho de aceitação para w, caso não exista, temos então que w não faz parte da linguagem.

        Args:
            word (str): Palavra de entrada.

        Returns:
            bool: True se word ∈ L(M), False caso contrário.
        """
        if not self._check_word_in_alphabet(word):
            raise ValueError(f"word '{word}' contains symbols that is not in the automaton's alphabet.")
        return self._partial_eval(self.initial_state, word)

    def union(self):
        pass

    def intersection(self):
        pass

    def difference(self):
        pass

    def complement(self):
        pass

    def language(self):
        pass

    def is_empty(self):
        pass

    def is_equivalent_to(self):
        pass

    def _validate(self):
        """Realiza uma série de verificações para garantir que os argumentos passados no construtor formem um DFA consistente.
        """
        if not self.states_set:
            raise ValueError("The set of states cannot be empty.")
        
        if self.initial_state not in self.states_set:
            raise ValueError("The initial state must belong to the set of states.")
        
        if not (self.final_states_set <= self.states_set):
            raise ValueError("Final states must belong to the set of states.")

        for (state, symbol), states_set in self.transition_table.items():
            if state not in self.states_set:
                raise ValueError(f"Unknown source state: {state}")

            if symbol not in self.alphabet:
                raise ValueError(f"Unknown symbol: {symbol}")

            if not (states_set <= self.states_set):
                raise ValueError(f"Unknown destination states_set: {states_set}")

    def _check_word_in_alphabet(self, word: str) -> bool:
        """Verifica se os simbolos que compõem a palavra estão todos presentes no alfabeto do autômato.

        Args:
            word (str): Palavra a ser verificada

        Returns:
            bool: True se word ∈ Σ*, False caso contrário.
        """
        return all(symbol in self.alphabet for symbol in word)

    def _partial_eval(self, current_state: str, word: str) -> bool:
        """Realiza a avaliação da palavra word seguindo um possível caminho de execução.

        Args:
            current_state (str): Estado atual considerado
            word (str): Parte da palavra original

        Returns:
            bool: _description_
        """
        if not word:
            return current_state in self.final_states_set
        next_states_set = self.transition_table.get((current_state, word[0]), set())
        if len(word) == 1:
            return any(q in self.final_states_set for q in next_states_set)
        return any(self._partial_eval(q, word[1:]) for q in next_states_set)
